from flask import Flask, jsonify, request

app = Flask(__name__)
accounts = [
    {"id": 1, "name": "John", "balance": 123.0},
    {"id": 2, "name": "Steve", "balance": 234.0},
]


@app.route("/")
def hello_word():
    return "Hello World"


@app.route("/accounts", methods=["GET"])
def get_accounts():
    return jsonify(accounts)


@app.route("/accounts/<account_id>", methods=["GET"])
def get_account(account_id):
    for acct in accounts:
        if acct.get("id", None) == int(account_id):
            return jsonify(acct)
    return {}


@app.route("/account", methods=["POST"])
def add_account():
    name = request.json["name"]
    balance = request.json["balance"]
    account_id = len(accounts) + 1
    data = {"id": account_id, "name": name, "balance": round(float(balance), 1)}
    accounts.append(data)


if __name__ == "__main__":
    app.run(port=8080)
