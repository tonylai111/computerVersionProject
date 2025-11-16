# @Version :1.0
# @Author  :TonyLai
# @File    :chapter01.py
# @Time    :2025/11/9 08:35
from http.client import responses
from pyexpat.errors import messages

import requests
import json
import os
from dotenv import load_dotenv
from tavily import TavilyClient
from torch.cpu import stream

from python.py5_1 import answer

# 加载环境变量
load_dotenv()


def get_weather(city:str) -> str:
    url = f'https://wttr.in/{city}?format=j1'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        current_condition = data['current_condition'][0]
        weather_desc = current_condition['weatherDesc'][0]['value']
        temp_c = current_condition['temp_C']

        return f'{city}当前的天气{weather_desc},气温{temp_c}摄氏度'
    except requests.exceptions.RequestException as e:
        return f'错误：查询天气时遇到网络问题-{e}'
    except (KeyError,IndexError) as e:
        return f'解析天气数据失败，可能是城市名称无效-{e}'


def get_attraction(city : str,weather : str ) -> str:
    '''
    :param city: 城市
    :param weather: 天气
    :return:  使用tavily search搜索返回后的景点推荐
    '''
    # 1、从环境变量中获取api秘钥
    api_key = os.environ.get("TAVILY_API_KEY")

    if not api_key:
        return '错误：未配置TAVILY_API_KEY'
    # 2、初始化客户端
    tavily = TavilyClient(api_key = api_key)
    # 3、构造一个精确的查询
    query = f'{city}在{weather}天气下最值得去的旅游景点推荐及理由'
    try:
    #4、调用api,include_answer=True会返回一个综合性的回答
        response = tavily.search(query=query,search_depth='basic',include_answer=True)
    #5、Tavily返回的结果可以直接使用
        if response.get('answer'):
            return response.get('answer')

        formatted_results = []
        for result in response.get('result',[]):
            formatted_results.append(f"- {result['title']}: {result['content']}")

        if not formatted_results:
            return '抱歉，没有找到相关的旅游景点推荐'

        return '根据搜索，为您找到以下信息：\n'+'\n'.join(formatted_results
                                                    )
    except Exception as e:
        return f'错误，执行Tavily搜索时出现问题-{e}'


# print(get_weather('北京'))
# print(get_attraction('香港', '雨天'))
#在雨天，香港迪士尼乐园和LOHAS Rink是最佳选择。迪士尼乐园提供独特的雨天体验，而LOHAS Rink是全港最大的溜冰场。

available_tools = {
    'get_weather':get_weather,
    'get_attraction':get_attraction
}

from openai import OpenAI
class OpenAICompatibleClient:
    '''
    一个用于调用任何兼容OpenAI接口的LLM服务法客户端
    '''
    def __init__(self ,model : str, api_key : str, base_url : str):
        self.model = model
        self.client = OpenAI(api_key = api_key, base_url= base_url)

    def generate(self , prompt : str , system_prompt : str) -> str:
        '''调用LLM API来生成回应'''
        print("正在调用大预言模型...")
        try:
            messages = [
                {'role': 'system' ,'content' : system_prompt},
                {'role': 'user','content' : prompt}
            ]
            response = self.client.chat.completions.create(
                model = self.model,
                messages = messages,
                stream = False
            )
            answer =  response.choices[0].message.content
            print('大语音模型响应成功')
            return answer
        except Exception as e:
            print(f'调用LLM API时发生错误：{e}')
            return '错误：调用预言模型服务时出现错误'



import re
# 1、配置LLM客户端（从环境变量读取）
API_KEY = os.getenv('LLM_API_KEY')
BASE_URL = os.getenv('LLM_BASE_URL')
MODLE_ID = os.getenv('LLM_MODEL_ID') or 'Qwen/Qwen2.5-72B-Instruct'
if not all([API_KEY, BASE_URL]):
    raise ValueError('缺少必要环境变量：请在 .env 中设置 LLM_API_KEY 和 LLM_BASE_URL')
AGENT_SYSTEM_PROMPT= """
你是一个智能助手，必须严格按照以下格式回答：
Thought: 分析当前情况和下一步行动
Action: 调用工具(get_weather/get_attraction)或finish(answer="最终答案")

调用工具时必须提供完整参数：
- get_weather(city="城市名")
- get_attraction(city="城市名", weather="天气描述")

示例：
Thought: 用户想了解北京天气
Action: get_weather(city="北京")
"""

llm = OpenAICompatibleClient(
    model=MODLE_ID,
    api_key=API_KEY,
    base_url=BASE_URL
)

# 2、初始化
user_prompt = "你好，请帮我查询一下九寨沟今天的天气，然后根据天气推荐一个合适的旅游景点"
prompt_history = [f'用户请求：{user_prompt}']

print(f'用户输入：{user_prompt}\n' + '='*40)

#3、运行主循环
for i in range(10):
    print(f'--循环{i+1}--\n')
    #3.1 构建prompt
    full_prompt = '\n'.join(prompt_history)
    #3.2 调用LLM进行思考
    llm_output = llm.generate(full_prompt, system_prompt=AGENT_SYSTEM_PROMPT)
    match = re.search(r'(Thought:.*?Action:.*?)(?=\n\s*(?:Thought:|Action:|Observation:)|\Z)',llm_output,re.DOTALL)
    if match:
        truncated = match.group(1).strip()
        if truncated != llm_output.strip():
            llm_output = truncated
            print('已截取多余的Thought -Action对')
    print(f'模型输出：\n{llm_output}\n')
    prompt_history.append(llm_output)
    #3.3 解析并执行行动
    action_match = re.search(r'Action:(.*)', llm_output, re.DOTALL)
    if not action_match:
        print("解析错误：模型输出中未找到Action")
        break
    action_str = action_match.group(1).strip()

    if action_str.startswith("finish"):
        final_answer = re.search(r'finish\(answer="(.*)"\)', action_str).group(1) # 这里为什么要这样写
        print(f'任务完成，最终答案是：{final_answer}')
        break
    # 修改参数解析部分，确保正确提取所有参数
    tool_name = re.search(r"(\w+)\(", action_str).group(1)
    args_str = re.search(r"\((.*)\)", action_str).group(1)
    # 改进参数提取逻辑
    kwargs = dict(re.findall(r'(\w+)="([^"]*)"', args_str))

    # 添加调试信息
    print(f"工具名称: {tool_name}")
    print(f"参数字符串: {args_str}")
    print(f"解析后的参数: {kwargs}")
    if tool_name in available_tools:
        # 检查必需参数
        if tool_name == 'get_attraction':
            if 'city' not in kwargs or 'weather' not in kwargs:
                observatin = '错误：get_attraction需要city和weather参数'
            else:
                observatin = available_tools[tool_name](**kwargs)
        elif tool_name == 'get_weather':
            if 'city' not in kwargs:
                observatin = '错误：get_weather需要city参数'
            else:
                observatin = available_tools[tool_name](**kwargs)
        else:
            observatin = available_tools[tool_name](**kwargs)
    else:
        observatin = f'错误：未定义的工具：{tool_name}'
    #3.4 记录观察结果

    observation_str = f'Observation:{observatin}'
    print(f'{observation_str}\n' + '='*40)
    prompt_history.append(observation_str)











