from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def index(user):
    return render_template('ameya.html',name=user)

if __name__ == '__main__':
    app.run(debug=True)