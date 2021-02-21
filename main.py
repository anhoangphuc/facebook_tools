from flask import Flask, request, jsonify

from facebook_acount import FacebookAccount

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Welcome"

@app.route('/fetch', methods=['POST'])
def fetch():
    try:
        email = request.form['email']
        password = request.form['password']

        my_account = FacebookAccount(email, password)
        my_account.login()
        cookies = my_account.get_cookies()
        token = my_account.get_token()

        result = {'status': 0, 'cookies': cookies, 'token': token}
    except Exception as err:
        result = {'status': 1, 'error': err}
    finally:
        my_account.close()
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 
