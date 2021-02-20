from flask import Flask, request, jsonify

from facebook_acount import FacebookAccount

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Welcome"

@app.route('/fetch', methods=['POST'])
def fetch():
    email = request.form['email']
    password = request.form['password']

    my_account = FacebookAccount(email, password)
    my_account.login()
    cookies = my_account.get_cookies()
    # print(cookies)
    # print(my_account.get_cookie('c_user') or "No cookie")
    token = my_account.get_token()

    result = {'cookies': cookies, 'token': token}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 
