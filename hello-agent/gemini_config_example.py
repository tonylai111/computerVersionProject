# @Version :1.0
# @Author  :TonyLai
# @File    :gemini_config_example.py
# @Time    :2025/11/14
# Gemini API 配置示例

"""
获取 Gemini API 配置信息的步骤：

1. API Key 获取：
   - 访问：https://aistudio.google.com/app/apikey
   - 登录 Google 账号
   - 点击 "Create API Key" 创建新的 API Key
   - 复制生成的 API Key

2. Base URL：
   - Google 官方 API: https://generativelanguage.googleapis.com/v1beta/
   - 注意：Gemini API 不完全兼容 OpenAI 格式

3. Model ID（常用模型）：
   - gemini-pro
   - gemini-1.5-pro
   - gemini-1.5-flash
   - gemini-1.5-pro-latest
"""

# ========== 方式一：使用 Google 官方 SDK（推荐） ==========
"""
安装依赖：
pip install google-generativeai

配置示例：
"""
import os
import google.generativeai as genai

# 设置 API Key
GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY_HERE'  # 替换为你的 API Key
genai.configure(api_key=GEMINI_API_KEY)

# 使用示例
def use_gemini_official_sdk():
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("你好，介绍一下你自己")
    print(response.text)

# ========== 方式二：通过 OpenAI 兼容接口使用（如果服务商支持） ==========
"""
某些第三方服务提供 OpenAI 兼容的 Gemini 接口，配置如下：
"""
GEMINI_CONFIG_OPENAI_COMPATIBLE = {
    'LLM_API_KEY': 'YOUR_GEMINI_API_KEY_HERE',
    'LLM_BASE_URL': 'https://generativelanguage.googleapis.com/v1beta/',  # 可能需要适配
    'LLM_MODEL_ID': 'gemini-pro',
    'LLM_TIMEOUT': 60
}

# ========== 方式三：使用 .env 文件配置 ==========
"""
在项目根目录创建 .env 文件，添加以下内容：

# Gemini API 配置
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL_ID=gemini-pro

# 如果使用 OpenAI 兼容接口
LLM_API_KEY=your_api_key_here
LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/
LLM_MODEL_ID=gemini-pro
LLM_TIMEOUT=60
"""

# ========== 实际使用示例 ==========
def example_with_your_code():
    """
    如果要使用你现有的 HelloAgentsLLM 类，需要注意：
    Gemini API 不完全兼容 OpenAI 格式，可能需要使用第三方适配服务
    或者修改 HelloAgentsLLM 类以支持 Gemini 的原生接口
    """
    from chapter04_react import HelloAgentsLLM
    
    # 注意：这可能需要第三方服务提供 OpenAI 兼容的 Gemini 接口
    # 或者你需要修改 HelloAgentsLLM 类来支持 Gemini 原生 API
    try:
        llm_client = HelloAgentsLLM(
            model='gemini-pro',
            apiKey='YOUR_GEMINI_API_KEY',
            baseUrl='https://generativelanguage.googleapis.com/v1beta/'
        )
    except Exception as e:
        print(f"错误：{e}")
        print("提示：Gemini API 不完全兼容 OpenAI 格式，建议使用官方 SDK")

if __name__ == '__main__':
    print("=" * 50)
    print("Gemini API 配置信息")
    print("=" * 50)
    print("\n1. API Key 获取地址：")
    print("   https://aistudio.google.com/app/apikey")
    print("\n2. 官方 Base URL：")
    print("   https://generativelanguage.googleapis.com/v1beta/")
    print("\n3. 常用 Model ID：")
    print("   - gemini-pro")
    print("   - gemini-1.5-pro")
    print("   - gemini-1.5-flash")
    print("\n4. 安装官方 SDK：")
    print("   pip install google-generativeai")
    print("=" * 50)

