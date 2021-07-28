from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    req_type = request.method
    if req_type == 'GET':
        return render_template('login.html')
    else:
        un = request.form('username')
        pw = request.form('password')
        if un == 'admin' & pw == 'admin':
            return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/visuals')
def visuals():
    return render_template('visuals.html')


if __name__ == '__main__':
    app.run()
