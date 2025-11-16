# @Version :1.0
# @Author  :TonyLai
# @File    :chapter04-plan-and-sovle.py
# @Time    :2025/11/16 13:57
import ast
import re

from llm_client import HelloAgentsLLM

PLANNER_PROMPT_TEMPLATE = """
你是一个顶级的AI规划专家，你的任务是将用户提出的辅助问题分解为有多个简单步骤组成的行动计划。
请确保每个步骤都是独立、可执行的子任务，并严格按照逻辑顺序排列。
你的输出必须是一个 Python 列表，每个元素是一个描述子任务的字符串。
请仅输出一个标准且唯一的 Python 代码块，且不要输出任何额外解释或文本。

问题：{question}
请严格按照以下格式输出（使用三反引号围栏，且语言标记必须是小写 python）：
```python
["步骤1","步骤2","步骤3"]
```
"""

EXECUTOR_PROMPT_TEMPLATE = """
你是一位顶级的AI执行专家，你的任务严格按照给定的计划，一步步的解决问题，
你将收到的原始问题，完整的计划，以及到目前为止已经完成的步骤和结果
请你专注于解决"当期的步骤"，并仅输出该步骤的最终答案，不雅输出任何额外的解释或对话
#原始问题：
{question}

#完整计划
{plan}

#历史步骤与结果
{history}

#当前步骤：
{current_step}

请仅输出针对"当前步骤"的回答

"""

class Planner:
    '''
    生成清晰的行动蓝图
    '''
    def __init__(self, llm_client:HelloAgentsLLM):
        self.llm_client = llm_client
    def plan(self, question:str) -> list[str]:

        '''
        根据用户问题生成一个行动计划
        '''
        prompt = PLANNER_PROMPT_TEMPLATE.format(question=question)

        messages = [{"role":"user","content":prompt}]

        print("--正在执行计划--")

        response_text = self.llm_client.think(messages = messages) or ""

        print(f"计划已经生成：\n{response_text}")


        #解析LLM输出的列表字符串
        try:
            # 更稳健：优先提取 ```python ... ``` 的第一段代码块
            code_block = None
            match = re.search(r"```python\s+([\s\S]*?)```", response_text, re.IGNORECASE)
            if match:
                code_block = match.group(1).strip()
            else:
                # 兼容少数模型使用三引号的情形
                if "'''python" in response_text:
                    code_block = response_text.split("'''python", 1)[1].split("'''", 1)[0].strip()
                elif '"""python' in response_text:
                    code_block = response_text.split('"""python', 1)[1].split('"""', 1)[0].strip()
            if not code_block:
                raise ValueError("未找到预期的Python代码块标记（```python ... ```）")

            #使用ast.literal_eval来安全地执行字符串，将其转换为python列表
            plan = ast.literal_eval(code_block)
            return plan if isinstance(plan,list) else []
        except(ValueError,SyntaxError,IndexError) as e:
            print(f"解析计划是出错:{e}\n 原始响应:{response_text}")
        except Exception as e:
            print(f'解析计划是发生未知错误{e}')




#规划器
class Executor:
    def __init__(self,llm_client):
        self.llm_client = llm_client

    def execute(self , question:str, plan: list[str]) -> str:
        """
        根据计划，逐步执行并解决问题
        """
        history = "" #用于存储历史步骤和结果的字符串

        print("\n--正在执行计划--")
        for i ,step in enumerate(plan):
            print(f'\n-->正在执行步骤{i + 1}/{len(plan)} :{step}')

            prompt = EXECUTOR_PROMPT_TEMPLATE.format(
                question = question,
                plan = plan,
                history = history if history else '无',
                current_step = step
            )
            messages = [{"role":"user","content":prompt}]

            response_text = self.llm_client.think(messages = messages) or ""

            history += f"步骤{i + 1}:{step}\n 结果：{response_text} \n"

            print(f"步骤{i+1}已完成，结果：{response_text}")
        #循环结束后，最后一步响应式最终答案
        final_answer = response_text
        return final_answer

#计划执行Agent
class PlanAndSolveAgent:
    def __init__(self , llm_client):
        """
        初始化智能体，同时创建规划期和执行器实例
        """
        self.llm_client = llm_client
        self.planner = Planner(llm_client)
        self.executor = Executor(llm_client)

    def run(self,question:str):
        print(f"开始处理问题 \n--{question}--")
        #1、调用规划器生成 计划
        plan = self.planner.plan(question)

        #检查计划是否生成成功
        if not plan:
            print("\n --任务终止--\n无法生成有效的计划")
            return #添加返回避免继续执行

        #2、调用执行器执行计划
        final_answer = self.executor.execute(question,plan)

        print(f"\n--任务完成 -- \n最终答案：{final_answer}")



if __name__ == '__main__':
    llm = HelloAgentsLLM()
    agent = PlanAndSolveAgent(llm)
    question = "一个水果店周一卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？"
    agent.run(question)

