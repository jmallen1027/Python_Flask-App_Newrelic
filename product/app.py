
from flask import Flask
from routes import book_blueprint
from models import db, init_app
from flask_migrate import Migrate



app = Flask(__name__)





app.config['SECRET_KEY'] = 'AWfi7qHc8pNYWmrwYt99CQ'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:$ENTER_YOUR_PW_HERE@db/book'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:$ENTER_YOUR_PW_HERE@localhost:3306/book'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/book.db'
app.register_blueprint(book_blueprint)
init_app(app)

migrate = Migrate(app, db)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
