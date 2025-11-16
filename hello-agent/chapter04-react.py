# @Version :1.0
# @Author  :TonyLai
# @File    :chapter04-react.py
# @Time    :2025/11/14 20:36

import os
from openai import  OpenAI
from dotenv import load_dotenv
from typing import  List,Dict

#加载环境变量
load_dotenv()

class HelloAgentsLLM:
    # LLM客户端，用于调用任何兼容OpenAI接口的LLM服务
    def __init__(self, model:str = None, apiKey : str = None, baseUrl:str = None, timeout : int = None ):
        '''
        初始化客户端，优先使用传入参数，如果为提供，则从环境变量中加载
        '''
        self.module = model or os.getenv('LLM_MODEL_ID')
        apiKey = apiKey or os.getenv('LLM_API_KEY')
        baseUrl = baseUrl or os.getenv('LLM_BASE_URL')
        timeout = timeout or int(os.getenv('LLM_TIMEOUT',60))

        if not all([self.module ,apiKey ,baseUrl]):
            raise ValueError('模型ID，API秘钥和服务地址必须被提供或在.env文件中定义')
        self.client = OpenAI(api_key = apiKey , base_url= baseUrl, timeout= timeout)

    def think(self ,messages:List[Dict[str,str]] , temperature: float = 0) -> str:
        print(f'正在调用{self.module}模型')
        try:
            response = self.client.chat.completions.create(
                model=self.module,
                messages=messages,
                temperature=temperature,
                stream=True
            )

            print('大语言模型响应成功！')
            collected_content = []
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                print(content,end='',flush=True)
                collected_content.append(content)
            print()
            return ''.join(collected_content)
        except Exception as e:
            print(f'调用LLM API时发生错误：{e}')
            return  None

# if __name__ == '__main__':
#     try :
#         # llmClient = HelloAgentsLLM()
#         # exapleMessages = [
#         #     {"role":"system" , "content":"You are a helpful assistant that writes Python code"},
#         #     {"role":"user" , "content":"写一个冒泡排序"}
#         # ]
#         #
#         # print("---调用LLM---")
#         # responseText = llmClient.think(exapleMessages)
#         # if responseText:
#         #     print(f'\nLLM输出：{responseText}')
#         # else:
#         #     print('LLM输出为空')
#         search('如何使用Python进行机器学习')
#     except Exception as e:
#         print(f'程序发生错误：{e}')


from serpapi import SerpApiClient

def search(query:str) -> str:
    """
    一个基于SerpAPI的实现网页搜索的工具，它会智能的解析搜索结果，优先返回直接答案和知识图谱信息
    :param query:
    :return:
    """
    print(f'正在使用SerpAPI搜索：{query}')

    try:
        api_key = os.getenv('SERPAPI_API_KEY')
        if not api_key:
            return '错误：未在.env 配置SERPAPI_API_KEY'
        params = {
            "engine" : "google",
            "q":query,
            "api_key" : api_key,
            "gl":"jp", # 设置国家代码
            "hl":"ja" # 设置语言代码
        }
        client = SerpApiClient(params)
        result = client.get_dict()

        if 'answer_box' in result: #Google的答案摘要框
            answer = result['answer_box']['answer']
            print(f'直接答案：{answer}')
            return answer
        if 'knowledge_graph' in result:  #知识图谱
            knowledge_graph = result['knowledge_graph']["description"]
            print(f'知识图谱信息：{knowledge_graph}')
            return knowledge_graph
        if 'organic_results' in result and result["organic_results"] : #返回前三个常规搜索结果的摘要

            # 如果没有直接答案，则返回前三个有机结果的摘要
            snippets = [
                f"[{i + 1}] {res.get('title', '')}\n{res.get('snippet', '')}"
                for i, res in enumerate(result["organic_results"][:3])
            ]
            return "\n\n".join(snippets)
            print(f' organic_results:{organic_results}')
            return organic_results
        return '未找到答案'
    except Exception as e:
        return f'搜索时发生错误:{e}'

#构建通用的智能体工具执行器

from typing import Dict,Any
class ToolExecutor:
    def __init__(self):
        self.tools:Dict[str,Dict[str,Any]] = {}
    def registerTool(self, name:str ,description:str ,func:callable):
        if name in self.tools:
            print(f'工具{name}已存在,将被覆盖')
        self.tools[name] = {'description':description ,'func':func}
        print(f'已注册工具：{name}')
    def getTool(self, name:str) -> callable:
        return self.tools.get(name,{}).get("func")

    def getAvailableTools(self) -> str:
        return "\n".join([f"{name}: {tool['description']}" for name, tool in self.tools.items()])


# if __name__ == '__main__':
#     try :
#         #1、工具的初始化语使用
#         toolExe = ToolExecutor()
#         #2、注册搜索类工具
#         search_description = "使用SerpAPI进行网页搜索，并返回结果"
#         toolExe.registerTool('search', search_description, search)
#         #打印可用的工具
#         print("\n--可用的工具--")
#         print(toolExe.getAvailableTools())
#         #智能体的Action调用，
#         tool_name = 'search'
#         tool_input = '人工智能深度学习最新的课程有哪些'
#
#         tool_function = toolExe.getTool(tool_name)
#         if tool_function:
#             observation = tool_function(tool_input)
#             print('===观察（Observation）===')
#             print(observation)
#         else:
#             print(f'未找到工具：{tool_name}')
#     except Exception as e:
#         print(f'程序发生错误：{e}')
REACT_PROMPT_TEMPLATE = """
请注意，你是一个有能力调用外部工具的智能助手。

可用工具如下：
{tools}

请严格按照以下格式进行回应：

Thought: 你的思考过程，用于分析问题、拆解任务和规划下一步行动。
Action: 你决定采取的行动，必须是以下格式之一：
- `{{tool_name}}[{{tool_input}}]`：调用一个可用工具。
- `Finish[最终答案]`：当你认为已经获得最终答案时。
- 当你收集到足够的信息，能够回答用户的最终问题时，你必须在`Action:`字段后使用 `finish(answer="...")` 来输出最终答案。


现在，请开始解决以下问题：
Question: {question}
History: {history}
"""

import re
class ReactAgent:
    def __init__(self, llm_client:HelloAgentsLLM, tool_executor:ToolExecutor,max_steps:int =5):
        self.llm_client = llm_client
        self.tool_executor = tool_executor
        self.max_steps = max_steps
        self.history = []
    # def _parse_output(self ,text : str):
    #     thought_match = re.search(r'Thought:(.*)',text)
    #     action_match = re.search(r'Action:(.*)',text)
    #     thought = thought_match.group(1).strip() if thought_match else None
    #     action = action_match.group(1).strip() if action_match else None
    #     return thought,action
    # def _parse_action(self,action_text:str):
    #     match = re.match(r"(\w+)\[(.*)\]", action_text)
    #     if match:
    #         return match.group(1),match.group(2)
    #     return None,None
    def _parse_output(self, text: str):
        thought_match = re.search(r"Thought: (.*)", text)
        action_match = re.search(r"Action: (.*)", text)
        thought = thought_match.group(1).strip() if thought_match else None
        action = action_match.group(1).strip() if action_match else None
        return thought, action

    def _parse_action(self, action_text: str):
        match = re.match(r"(\w+)\[(.*)\]", action_text)
        return (match.group(1), match.group(2)) if match else (None, None)

    def _parse_action_input(self, action_text: str):
        match = re.match(r"\w+\[(.*)\]", action_text)
        return match.group(1) if match else ""
    # ReAct 提示词模板

    def run(self, question: str):
        self.history = []
        current_step = 0

        while current_step < self.max_steps:
            current_step += 1
            print(f"\n--- 第 {current_step} 步 ---")

            tools_desc = self.tool_executor.getAvailableTools()
            history_str = "\n".join(self.history)
            prompt = REACT_PROMPT_TEMPLATE.format(tools=tools_desc, question=question, history=history_str)

            messages = [{"role": "user", "content": prompt}]
            response_text = self.llm_client.think(messages=messages)
            if not response_text:
                print("错误：LLM未能返回有效响应。");
                break

            thought, action = self._parse_output(response_text)
            if thought: print(f"🤔 思考: {thought}")
            if not action: print("警告：未能解析出有效的Action，流程终止。"); break

            if action.startswith("Finish"):
                final_answer = self._parse_action_input(action)
                print(f"🎉 最终答案: {final_answer}")
                return final_answer

            tool_name, tool_input = self._parse_action(action)
            if not tool_name or not tool_input:
                self.history.append("Observation: 无效的Action格式，请检查。");
                continue

            print(f"🎬 行动: {tool_name}[{tool_input}]")
            tool_function = self.tool_executor.getTool(tool_name)
            observation = tool_function(tool_input) if tool_function else f"错误：未找到名为 '{tool_name}' 的工具。"

            print(f"👀 观察: {observation}")
            self.history.append(f"Action: {action}")
            self.history.append(f"Observation: {observation}")

        print("已达到最大步数，流程终止。")
        return None

if __name__ == '__main__':
    # llmClient = HelloAgentsLLM()
    # toolExe = ToolExecutor()
    # search_desc = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具"
    # toolExe.registerTool('search',search_desc,search)
    # #1、工具的初始化语使用
    # agent = ReactAgent(llmClient,toolExe,max_steps=3)
    # question = "最近深圳天气怎么样"
    # agent.run(question)
    llm = HelloAgentsLLM()
    tool_executor = ToolExecutor()
    search_desc = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
    tool_executor.registerTool("search", search_desc, search)
    agent = ReactAgent(llm_client=llm, tool_executor=tool_executor)
    question = "Agent当下最热门的技术有哪些？"
    agent.run(question)
