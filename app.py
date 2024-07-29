from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for users
users = {
    'user1': {'pin': '1234', 'balance': 1000},
    'user2': {'pin': '5678', 'balance': 500},
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    pin = request.form['pin']

    if username in users and users[username]['pin'] == pin:
        return redirect(url_for('dashboard', username=username))
    else:
        return 'Invalid username or PIN'



@app.route('/dashboard/<username>')
def dashboard(username):
    if username in users:
        user = users[username]
        return render_template('dashboard.html', username=username, balance=user['balance'])
    else:
        return 'User not found'


@app.route('/withdraw/<username>', methods=['POST'])
def withdraw(username):
    if username in users:
        amount = int(request.form['amount'])
        if users[username]['balance'] >= amount:
            users[username]['balance'] -= amount
            return redirect(url_for('dashboard', username=username))
        else:
            return 'Insufficient funds'
    else:
        return 'User not found'

@app.route('/deposit/<username>', methods=['POST'])
def deposit(username):
    if username in users:
        amount = int(request.form['amount'])
        users[username]['balance'] += amount
        return redirect(url_for('dashboard', username=username))
    else:
        return 'User not found'


if __name__ == '__main__':
    app.run(debug = True)