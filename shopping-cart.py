from models import shopping_cart, db
from flask import Flask, render_template, request
from flask_migrate import Migrate
app = Flask(__name__)

db.init_app(app)
# create a Migrate object for migrations
migrate = Migrate(app, db)
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/cart.html', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        item = request.form['item-name']
        price = request.form['item-price']
        
        new_item = shopping_cart(item=item, price=price)
        db.session.add(new_item)
        db.session.commit()
        
        return render_template('index.html')

@app.route('/checkout.html', methods=['POST', 'GET'])
def checkout():
    return render_template('checkout.html')


@app.route('/cart.html', methods=['POST', 'GET'])
def cart():
    cursor.execute("SELECT item FROM shop_cart;")
    items = cursor.fetchall()

    return render_template('cart.html', items=items)


if __name__ == "__main__":
    app.run(debug=True)        