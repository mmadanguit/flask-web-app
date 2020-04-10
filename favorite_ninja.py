from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('questions.html')


@app.route('/login', methods=['GET', 'POST'])
def response(name=None):
    if request.method == 'POST':
        if not request.form['name'] or not request.form['age'] or not request.form['ninja']:
            return redirect(url_for('error'))
        return render_template('response.html', name=request.form['name'], age=request.form['age'])


@app.route('/error')
def error():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
