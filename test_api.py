import requests
import json

def test_openrouter_api():
    # 测试配置
    url = "http://localhost:8080/v1/chat/completions"
    headers = {
        "Authorization": "Bearer sk-or-v1-xxx", # 替换为你的 API 密钥
        "Content-Type": "application/json"
    }
    
    # 测试数据
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ],
        "model": "google/gemini-2.0-flash-exp:free",
        "temperature": 0.7,
        "stream": True
    }

    try:
        # 发送请求
        response = requests.post(url, headers=headers, json=data)
        
        # 检查响应状态码
        print(f"Status Code: {response.status_code}")
        
        # 如果是流式响应
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    # 移除 "data: " 前缀
                    line = line.decode('utf-8')
                    if line.startswith("data: "):
                        line = line[6:]
                    if line == "[DONE]":
                        break
                    try:
                        # 解析 JSON 响应
                        resp_data = json.loads(line)
                        if "choices" in resp_data:
                            content = resp_data["choices"][0].get("delta", {}).get("content", "")
                            if content:
                                print(f"Response: {content}")
                    except json.JSONDecodeError:
                        print(f"Failed to parse JSON: {line}")
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    test_openrouter_api()