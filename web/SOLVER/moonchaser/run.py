from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'], defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    return open('index.html').read()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="1234", ssl_context='adhoc')