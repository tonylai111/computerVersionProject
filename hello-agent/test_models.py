# @Version :1.0
# @Author  :TonyLai
# @File    :test_models.py
# @Time    :2025/11/14
# 测试不同免费模型的脚本

import os
from dotenv import load_dotenv
from chapter04_react import HelloAgentsLLM

# 加载环境变量
load_dotenv()

# ========== 免费模型配置 ==========
FREE_MODELS_CONFIG = {
    # 1. Groq - 推荐，速度快，免费额度充足
    "groq": {
        "name": "Groq (Llama 3.1)",
        "model": "llama-3.1-70b-versatile",
        "base_url": "https://api.groq.com/openai/v1",
        "api_key_env": "GROQ_API_KEY",
        "get_key_url": "https://console.groq.com/",
        "description": "速度极快，免费额度充足"
    },
    
    # 2. DeepSeek - 推荐，国内可用
    "deepseek": {
        "name": "DeepSeek Chat",
        "model": "deepseek-chat",
        "base_url": "https://api.deepseek.com/v1",
        "api_key_env": "DEEPSEEK_API_KEY",
        "get_key_url": "https://platform.deepseek.com/",
        "description": "国内可用，响应快"
    },
    
    # 3. ModelScope - 你当前使用的
    "modelscope": {
        "name": "ModelScope (Qwen)",
        "model": "Qwen/Qwen2.5-72B-Instruct",
        "base_url": "https://api-inference.modelscope.cn/v1/",
        "api_key_env": "LLM_API_KEY",  # 使用你现有的环境变量
        "get_key_url": "https://www.modelscope.cn/",
        "description": "国内可用，你当前使用的"
    },
    
    # 4. OpenRouter - 多个免费模型
    "openrouter": {
        "name": "OpenRouter (Gemini Flash)",
        "model": "google/gemini-flash-1.5",
        "base_url": "https://openrouter.ai/api/v1",
        "api_key_env": "OPENROUTER_API_KEY",
        "get_key_url": "https://openrouter.ai/",
        "description": "聚合多个模型"
    },
    
    # 5. Together AI
    "together": {
        "name": "Together AI (Llama)",
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "base_url": "https://api.together.xyz/v1",
        "api_key_env": "TOGETHER_API_KEY",
        "get_key_url": "https://www.together.ai/",
        "description": "开源模型"
    }
}

def test_model(model_key: str, test_message: str = "你好，请用一句话介绍你自己"):
    """
    测试指定的模型
    
    :param model_key: 模型配置的 key（如 'groq', 'deepseek' 等）
    :param test_message: 测试消息
    """
    if model_key not in FREE_MODELS_CONFIG:
        print(f"错误：未知的模型 key '{model_key}'")
        print(f"可用的模型：{', '.join(FREE_MODELS_CONFIG.keys())}")
        return False
    
    config = FREE_MODELS_CONFIG[model_key]
    print("=" * 60)
    print(f"测试模型：{config['name']}")
    print(f"模型 ID：{config['model']}")
    print(f"Base URL：{config['base_url']}")
    print(f"描述：{config['description']}")
    print("=" * 60)
    
    # 获取 API Key
    api_key = os.getenv(config['api_key_env'])
    if not api_key:
        print(f"\n❌ 错误：未找到环境变量 {config['api_key_env']}")
        print(f"   请设置环境变量或在 .env 文件中添加：")
        print(f"   {config['api_key_env']}=your_api_key_here")
        print(f"   获取 API Key：{config['get_key_url']}")
        return False
    
    try:
        # 创建 LLM 客户端
        llm_client = HelloAgentsLLM(
            model=config['model'],
            apiKey=api_key,
            baseUrl=config['base_url'],
            timeout=60
        )
        
        # 测试消息
        messages = [
            {"role": "user", "content": test_message}
        ]
        
        print(f"\n📤 发送消息：{test_message}")
        print("\n📥 响应：")
        
        # 调用模型
        response = llm_client.think(messages=messages, temperature=0)
        
        if response:
            print(f"\n✅ 测试成功！")
            print(f"\n完整响应：\n{response}")
            return True
        else:
            print(f"\n❌ 测试失败：未收到响应")
            return False
            
    except ValueError as e:
        print(f"\n❌ 配置错误：{e}")
        return False
    except Exception as e:
        print(f"\n❌ 调用失败：{e}")
        print(f"\n可能的原因：")
        print(f"  1. API Key 无效或过期")
        print(f"  2. 模型 ID 不正确")
        print(f"  3. Base URL 不正确")
        print(f"  4. 网络连接问题")
        print(f"  5. 免费额度已用完")
        return False

def list_available_models():
    """列出所有可用的模型配置"""
    print("=" * 60)
    print("可用的免费测试模型：")
    print("=" * 60)
    
    for key, config in FREE_MODELS_CONFIG.items():
        api_key = os.getenv(config['api_key_env'])
        status = "✅ 已配置" if api_key else "❌ 未配置"
        
        print(f"\n[{key}] {config['name']}")
        print(f"   模型：{config['model']}")
        print(f"   Base URL：{config['base_url']}")
        print(f"   环境变量：{config['api_key_env']} {status}")
        print(f"   描述：{config['description']}")
        print(f"   获取 Key：{config['get_key_url']}")

def test_all_configured_models(test_message: str = "你好，请用一句话介绍你自己"):
    """测试所有已配置的模型"""
    print("=" * 60)
    print("测试所有已配置的模型")
    print("=" * 60)
    
    results = {}
    for key in FREE_MODELS_CONFIG.keys():
        config = FREE_MODELS_CONFIG[key]
        api_key = os.getenv(config['api_key_env'])
        
        if api_key:
            print(f"\n\n{'='*60}")
            print(f"正在测试：{config['name']}")
            print(f"{'='*60}")
            success = test_model(key, test_message)
            results[key] = success
        else:
            print(f"\n⏭️  跳过 {config['name']}（未配置 API Key）")
            results[key] = None
    
    # 汇总结果
    print("\n\n" + "=" * 60)
    print("测试结果汇总")
    print("=" * 60)
    for key, result in results.items():
        config = FREE_MODELS_CONFIG[key]
        if result is True:
            print(f"✅ {config['name']}: 成功")
        elif result is False:
            print(f"❌ {config['name']}: 失败")
        else:
            print(f"⏭️  {config['name']}: 未配置")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        # 测试指定的模型
        model_key = sys.argv[1]
        test_message = sys.argv[2] if len(sys.argv) > 2 else "你好，请用一句话介绍你自己"
        test_model(model_key, test_message)
    else:
        # 交互式菜单
        while True:
            print("\n" + "=" * 60)
            print("免费模型测试工具")
            print("=" * 60)
            print("\n请选择操作：")
            print("1. 列出所有可用模型")
            print("2. 测试指定模型")
            print("3. 测试所有已配置的模型")
            print("4. 退出")
            
            choice = input("\n请输入选项 (1-4): ").strip()
            
            if choice == '1':
                list_available_models()
            elif choice == '2':
                list_available_models()
                model_key = input("\n请输入要测试的模型 key: ").strip()
                test_message = input("请输入测试消息（直接回车使用默认）: ").strip()
                if not test_message:
                    test_message = "你好，请用一句话介绍你自己"
                test_model(model_key, test_message)
            elif choice == '3':
                test_message = input("请输入测试消息（直接回车使用默认）: ").strip()
                if not test_message:
                    test_message = "你好，请用一句话介绍你自己"
                test_all_configured_models(test_message)
            elif choice == '4':
                print("再见！")
                break
            else:
                print("无效的选项，请重新选择")

