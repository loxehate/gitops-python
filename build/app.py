from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello():
    env = os.getenv("APP_ENV", "dev")  # 默认为 dev
    if env == "prod":
        return "Hello gitops prod qqemail update"
    else:
        return "Hello gitops dev 2"

@app.route('/api')
def api_response():
    env = os.getenv("APP_ENV", "dev")  # 默认为 dev
    if env == "prod":
        return "api gitops prod qqemail update"
    else:
        return "api gitops dev 2"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
