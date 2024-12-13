from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/v1/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    url = f'https://openrouter.ai/api/v1/{path}'
    
    # 打印接收到的请求信息
    print(f"\n=== 收到请求 ===")
    print(f"Path: {path}")
    print(f"Method: {request.method}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Data: {request.get_data().decode()}")
    
    headers = {
        'Authorization': request.headers.get('Authorization'),
        'Content-Type': 'application/json',
        'HTTP-Referer': 'http://localhost:3000',
        'X-Title': 'ChatBox'
    }
    
    # 打印发送的请求信息
    print(f"\n=== 发送请求 ===")
    print(f"URL: {url}")
    print(f"Headers: {headers}")
    
    resp = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=request.get_data()
    )
    
    # 打印响应信息
    print(f"\n=== 收到响应 ===")
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text}")
    
    return Response(
        resp.content,
        status=resp.status_code,
        content_type=resp.headers['content-type']
    )

if __name__ == '__main__':
    app.run(port=8080) 