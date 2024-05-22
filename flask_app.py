from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'


email_address = "shmulikeller@gmail.com"

@app.route('/page')
def index():
    return render_template('main.html', email_address=email_address)

if __name__ == '__main__':
    app.run(debug=True)