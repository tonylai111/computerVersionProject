# @Version :1.0
# @Author  :TonyLai
# @File    :llm_client.py
# @Time    :2025/11/16 14:02

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
