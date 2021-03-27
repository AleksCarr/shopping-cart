
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/cart.html', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        
        return render_template('index.html')

@app.route('/checkout.html', methods=['POST', 'GET'])
def checkout():
    return render_template('checkout.html')


@app.route('/cart.html', methods=['POST', 'GET'])
def cart():

    return render_template('cart.html', items=items)


if __name__ == "__main__":
    app.run(debug=True)        