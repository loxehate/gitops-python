from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello():
    env = os.getenv("APP_ENV", "dev")  # 默认为 dev
    if env == "prod":
        return "Hello gitops prod applications latest"
    else:
        return "Hello gitops dev applications latest"

@app.route('/api')
def api_response():
    env = os.getenv("APP_ENV", "dev")  # 默认为 dev
    if env == "prod":
        return "api gitops prod applications latest"
    else:
        return "api gitops dev applications latest"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
