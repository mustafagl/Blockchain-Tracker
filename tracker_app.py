from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
    url = "http://localhost:8080/blockchain"
    response = requests.get(url)
    if response.status_code == 200:
        blocks = response.json()["Blocks"]
        return render_template('index.html', blocks=blocks)
    else:
        return f"Error: Unable to fetch data from {url}", 500

@app.route('/transactions/<hash>')
def block(hash):
    if hash == "c1cb35e763084bcfe4815e2a77a7df4fcdcac9fcdb76aef972f91753b731fc3f":
        return render_template('transactions.html', transactions=[{"Sender":"This is a Genesis Block"}])

    url = f"http://localhost:8080/transactions?blockHash={hash}"
    response = requests.get(url)
    transactions = response.json()
    print(transactions)

    return render_template('transactions.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
