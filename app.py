from flask import Flask, request, Response

from deepseek_ai import DeepSeekAI

app = Flask(__name__)


client = DeepSeekAI(api_key="")


def chat_response(model, messages):
    response = client.chat(model, messages)
    if not response:
        yield "请求失败"
        
    for chunk in response:
        yield chunk.choices[0].delta.content


@app.route('/chat', methods=['POST'])
def index():
    data = request.get_json()
    model = data.get("model")
    messages = data.get("messages")
    # 流式响应
    return Response(chat_response(model, messages), content_type='text/plain; charset=utf-8')
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
