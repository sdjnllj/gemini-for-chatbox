# ChatBox Gemini Proxy

这是一个简单的代理服务器,用于让 ChatBox 能够使用 OpenRouter 提供的 Gemini 模型。

## 前提条件

- Python 3.x
- OpenRouter API 密钥 (从 https://openrouter.ai/keys 获取)
- ChatBox (从 https://github.com/Bin-Huang/chatbox/releases 下载)

## 快速开始

1. 克隆仓库:

## 安装

1. 克隆或下载此仓库
2. 运行 start_proxy.bat,它会自动安装必要的依赖:
   - flask
   - requests

## 使用方法

1. 运行代理服务器:
   - 双击 start_proxy.bat
   - 保持命令行窗口开着

2. 配置 ChatBox:
   - API 模式: OpenAI API 兼容
   - 名称: OpenRouterGemini
   - API 地址: http://localhost:8080/v1
   - API 路径: /chat/completions
   - API 密钥: 你的 OpenRouter API 密钥
   - 模型: google/gemini-2.0-flash-exp:free

3. 开始使用 ChatBox 与 Gemini 对话

## 文件说明

- `proxy.py`: 代理服务器主程序
- `start_proxy.bat`: 启动脚本,包含环境检查
- `test_api.py`: API 测试脚本(可选)

## 注意事项

- 使用 ChatBox 之前必须先运行代理服务器
- 代理服务器运行在 http://localhost:8080
- 确保你的 OpenRouter API 密钥足够的配额

## 常见问题

Q: 为什么需要代理服务器?  
A: OpenRouter API 需要特殊的请求头,而 ChatBox 无法直接添加这些头信息。代理服务器帮助添加必要的请求头。

Q: 如何关闭代理服务器?  
A: 直接关闭运行 proxy.py 的命令行窗口即可。

## 许可证

MIT 