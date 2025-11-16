# @Version :1.0
# @Author  :TonyLai
# @File    :openai_api.py
# @Time    :2025/11/9 11:19

from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_TYPE = os.getenv('LLM_MODEL_ID') or "Qwen/Qwen2.5-72B-Instruct"
BASE_URL = os.getenv('LLM_BASE_URL')
API_KEY = os.getenv('LLM_API_KEY')

if not all([BASE_URL, API_KEY]):
    raise ValueError("缺少必要环境变量：请在 .env 中设置 LLM_BASE_URL 与 LLM_API_KEY")

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type=MODEL_TYPE,
    url=BASE_URL,
    api_key=API_KEY
)

agent = ChatAgent(
    model=model,
    output_language='中文'
)

response = agent.step("你有那些通用能力？")
print(response.msgs[0].content)
