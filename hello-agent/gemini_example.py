# @Version :1.0
# @Author  :TonyLai
# @File    :gemini_example.py
# @Time    :2025/11/14
# Gemini API 使用示例

import os
from dotenv import load_dotenv
import google.generativeai as genai

# 加载环境变量
load_dotenv()

# ========== 配置 Gemini API ==========
# 方法1：从环境变量读取（推荐）
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# 方法2：直接设置（仅用于测试，生产环境请使用环境变量）
# GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY_HERE'

if not GEMINI_API_KEY:
    print("错误：请设置 GEMINI_API_KEY 环境变量")
    print("获取 API Key：https://aistudio.google.com/app/apikey")
    exit(1)

# 配置 Gemini
genai.configure(api_key=GEMINI_API_KEY)

# ========== 可用的模型列表 ==========
AVAILABLE_MODELS = [
    'gemini-pro',
    'gemini-1.5-pro',
    'gemini-1.5-flash',
    'gemini-1.5-pro-latest'
]

# ========== 基本使用示例 ==========
def basic_example():
    """基本使用示例"""
    print("=" * 50)
    print("Gemini 基本使用示例")
    print("=" * 50)
    
    # 创建模型实例
    model = genai.GenerativeModel('gemini-pro')
    
    # 生成内容
    response = model.generate_content("用一句话介绍 Python 编程语言")
    print(f"\n响应：{response.text}")

# ========== 对话示例 ==========
def chat_example():
    """对话示例"""
    print("\n" + "=" * 50)
    print("Gemini 对话示例")
    print("=" * 50)
    
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    
    # 第一轮对话
    response1 = chat.send_message("你好，我是小明")
    print(f"\n用户：你好，我是小明")
    print(f"Gemini：{response1.text}")
    
    # 第二轮对话（带上下文）
    response2 = chat.send_message("我刚才说我叫什么名字？")
    print(f"\n用户：我刚才说我叫什么名字？")
    print(f"Gemini：{response2.text}")

# ========== 流式输出示例 ==========
def stream_example():
    """流式输出示例（类似你代码中的 stream=True）"""
    print("\n" + "=" * 50)
    print("Gemini 流式输出示例")
    print("=" * 50)
    
    model = genai.GenerativeModel('gemini-pro')
    
    print("\n正在生成内容...")
    response = model.generate_content(
        "写一首关于人工智能的短诗",
        stream=True
    )
    
    print("\n响应：", end='', flush=True)
    for chunk in response:
        if chunk.text:
            print(chunk.text, end='', flush=True)
    print()

# ========== 与你的代码兼容的封装类 ==========
class GeminiLLM:
    """封装 Gemini API，使其接口与你的 HelloAgentsLLM 类似"""
    
    def __init__(self, model: str = 'gemini-pro', api_key: str = None):
        """
        初始化 Gemini 客户端
        :param model: 模型名称，默认 'gemini-pro'
        :param api_key: API Key，如果为 None 则从环境变量读取
        """
        api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError('请提供 GEMINI_API_KEY 或在环境变量中设置')
        
        genai.configure(api_key=api_key)
        self.model_name = model
        self.model = genai.GenerativeModel(model)
        self.chat = None
    
    def think(self, messages: list, temperature: float = 0, stream: bool = True) -> str:
        """
        思考方法，兼容你的代码接口
        :param messages: 消息列表，格式：[{"role": "user", "content": "..."}]
        :param temperature: 温度参数
        :param stream: 是否流式输出
        :return: 响应文本
        """
        print(f'正在调用 {self.model_name} 模型')
        
        try:
            # 将消息格式转换为 Gemini 格式
            # Gemini 使用简单的文本输入，或者使用 chat 模式
            user_message = None
            system_message = None
            
            for msg in messages:
                if msg['role'] == 'system':
                    system_message = msg['content']
                elif msg['role'] == 'user':
                    user_message = msg['content']
            
            # 如果有对话历史，使用 chat 模式
            if len(messages) > 1 or (system_message and user_message):
                if not self.chat:
                    # 设置系统提示词
                    if system_message:
                        generation_config = {
                            'temperature': temperature,
                        }
                        self.model = genai.GenerativeModel(
                            self.model_name,
                            generation_config=generation_config,
                            system_instruction=system_message
                        )
                    self.chat = self.model.start_chat(history=[])
                
                response = self.chat.send_message(user_message or "", stream=stream)
            else:
                # 单次对话
                prompt = user_message or ""
                if system_message:
                    prompt = f"{system_message}\n\n{prompt}"
                
                response = self.model.generate_content(
                    prompt,
                    generation_config={'temperature': temperature},
                    stream=stream
                )
            
            print('大语言模型响应成功！')
            
            if stream:
                collected_content = []
                for chunk in response:
                    content = chunk.text if hasattr(chunk, 'text') else str(chunk)
                    if content:
                        print(content, end='', flush=True)
                        collected_content.append(content)
                print()
                return ''.join(collected_content)
            else:
                result = response.text if hasattr(response, 'text') else str(response)
                print(result)
                return result
                
        except Exception as e:
            print(f'调用 Gemini API 时发生错误：{e}')
            return None

# ========== 使用示例 ==========
if __name__ == '__main__':
    # 示例1：基本使用
    # basic_example()
    
    # 示例2：对话
    # chat_example()
    
    # 示例3：流式输出
    # stream_example()
    
    # 示例4：使用封装的类（兼容你的代码）
    try:
        gemini_llm = GeminiLLM(model='gemini-pro')
        
        example_messages = [
            {"role": "system", "content": "You are a helpful assistant that writes Python code"},
            {"role": "user", "content": "写一个冒泡排序"}
        ]
        
        print("\n" + "=" * 50)
        print("使用 GeminiLLM 类（兼容你的代码接口）")
        print("=" * 50)
        response_text = gemini_llm.think(example_messages, temperature=0, stream=True)
        
        if response_text:
            print(f'\n完整响应：{response_text}')
        else:
            print('响应为空')
            
    except Exception as e:
        print(f'错误：{e}')
        print("\n提示：")
        print("1. 请先安装：pip install google-generativeai")
        print("2. 在 .env 文件中设置：GEMINI_API_KEY=your_api_key")
        print("3. 或访问获取 API Key：https://aistudio.google.com/app/apikey")

