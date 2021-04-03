from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
## import the sqlache file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# Declared db instance
db = SQLAlchemy(app)


# created db table
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1050), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    ## use this array on items if no actual database needed
    ## [
    ## {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    ## {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    ## {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ## ]
    return render_template('market.html', items=items)
