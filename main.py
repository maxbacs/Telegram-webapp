from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Бот запущен и сервер работает!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
