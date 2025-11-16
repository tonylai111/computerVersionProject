# 免费测试模型推荐

## 1. ModelScope（魔搭）- 推荐 ⭐⭐⭐⭐⭐

**特点**：国内可用，免费额度充足，兼容 OpenAI 接口

### 配置信息：
- **Base URL**: `https://api-inference.modelscope.cn/v1/`
- **API Key**: 在 [ModelScope](https://www.modelscope.cn/) 注册获取
- **可用模型**:
  - `Qwen/Qwen2.5-72B-Instruct` (你当前使用的)
  - `Qwen/Qwen2.5-14B-Instruct`
  - `Qwen/Qwen2.5-7B-Instruct`
  - `Qwen/Qwen2-72B-Instruct`
  - `Qwen/Qwen2-14B-Instruct`
  - `Qwen/Qwen2-7B-Instruct`
  - `deepseek-ai/DeepSeek-V2.5`
  - `01-ai/Yi-34B-Chat`

### 获取 API Key：
1. 访问：https://www.modelscope.cn/
2. 注册/登录账号
3. 进入个人中心 -> API 管理
4. 创建 API Key

---

## 2. DeepSeek API - 推荐 ⭐⭐⭐⭐

**特点**：免费额度充足，响应速度快，兼容 OpenAI 接口

### 配置信息：
- **Base URL**: `https://api.deepseek.com/v1`
- **API Key**: 在 [DeepSeek](https://platform.deepseek.com/) 注册获取
- **可用模型**:
  - `deepseek-chat` (免费)
  - `deepseek-coder` (代码专用，免费)

### 获取 API Key：
1. 访问：https://platform.deepseek.com/
2. 注册/登录账号
3. 进入 API Keys 页面
4. 创建新的 API Key

### 免费额度：
- 每天有一定免费额度（具体查看官网）

---

## 3. OpenRouter - 推荐 ⭐⭐⭐⭐

**特点**：聚合多个模型，部分免费，兼容 OpenAI 接口

### 配置信息：
- **Base URL**: `https://openrouter.ai/api/v1`
- **API Key**: 在 [OpenRouter](https://openrouter.ai/) 注册获取
- **免费模型**:
  - `google/gemini-flash-1.5` (免费)
  - `meta-llama/llama-3.2-3b-instruct:free` (免费)
  - `mistralai/mistral-7b-instruct:free` (免费)
  - `huggingface/zephyr-7b-beta:free` (免费)

### 获取 API Key：
1. 访问：https://openrouter.ai/
2. 注册/登录账号
3. 进入 Keys 页面创建 API Key

---

## 4. Google Gemini API

**特点**：Google 官方，有免费额度

### 配置信息：
- **Base URL**: `https://generativelanguage.googleapis.com/v1beta/`
- **API Key**: 在 [Google AI Studio](https://aistudio.google.com/app/apikey) 获取
- **可用模型**:
  - `gemini-pro` (免费，有限额)
  - `gemini-1.5-flash` (免费，有限额)
  - `gemini-1.5-pro` (免费，有限额)

**注意**：不完全兼容 OpenAI 格式，需要使用官方 SDK 或适配层

---

## 5. Groq API - 推荐 ⭐⭐⭐⭐⭐

**特点**：速度极快，免费额度充足，兼容 OpenAI 接口

### 配置信息：
- **Base URL**: `https://api.groq.com/openai/v1`
- **API Key**: 在 [Groq](https://console.groq.com/) 注册获取
- **可用模型**:
  - `llama-3.1-70b-versatile` (免费)
  - `llama-3.1-8b-instant` (免费)
  - `mixtral-8x7b-32768` (免费)
  - `gemma2-9b-it` (免费)

### 获取 API Key：
1. 访问：https://console.groq.com/
2. 注册/登录账号
3. 进入 API Keys 页面创建

### 免费额度：
- 每分钟 30 次请求
- 每天有大量免费额度

---

## 6. Together AI

**特点**：提供多个开源模型，有免费额度

### 配置信息：
- **Base URL**: `https://api.together.xyz/v1`
- **API Key**: 在 [Together AI](https://www.together.ai/) 注册获取
- **免费模型**:
  - `meta-llama/Llama-3-8b-chat-hf` (有免费额度)
  - `mistralai/Mixtral-8x7B-Instruct-v0.1` (有免费额度)

---

## 快速测试建议

### 最推荐的测试模型（按优先级）：

1. **Groq** - 速度快，免费额度充足，完全兼容 OpenAI
2. **DeepSeek** - 国内可用，响应快，免费额度充足
3. **ModelScope** - 你已经在用，继续使用即可
4. **OpenRouter** - 可以尝试多个免费模型

### 故障排查

如果调用没有结果返回，检查：

1. **API Key 是否正确**
2. **Base URL 是否正确**
3. **模型 ID 是否正确**
4. **网络连接是否正常**
5. **查看错误信息**（代码中的异常处理会打印错误）

