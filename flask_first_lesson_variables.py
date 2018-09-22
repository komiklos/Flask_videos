from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Return this to the user who visited this page. The browser will render it.
    return 'Hello World!'

@app.route('/goat')
def goat():
    return '<h2> Goats shouldn\'t be eaten, as they represent the gods </h2>'


@app.route('/profile/<username>/<int:product_ID>')
def profile(username, product_ID):
    return "<h1>Dear {0}, your product ID is: {1}</h2>".format(username, product_ID)

if __name__ == '__main__':
    app.run()
