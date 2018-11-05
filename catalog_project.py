from flask import Flask
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

app = Flask(__name__)

engine = create_engine('sqlite:///catalogproject.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/home')
def showHome():
    return 'it works'


#############Routes for categories#############

@app.route('/category/')
def allCategories():
    return 'categories'

@app.route('/category/<int:category>/')
def showCategory(category):
    return 'category'

@app.route('/category/new/')
def newCategory():
    return 'new category'

@app.route('/category/<int:category>/edit/')
def editCategory(category):
    return 'edit category'

@app.route('/category/<int:category>/delete/')
def deleteCategory(category):
    return 'delete category'

#########Routes for itens#################

@app.route('/category/<int:category>/<int:item>/')
def showItem(category, item):
    return 'Item'

@app.route('/category/<int:category>/new/')
def newItem(category):
    return 'new item'

@app.route('/category/<int:category>/<int:item>/edit/')
def editItem(category, item):
    return 'edit item'

@app.route('/category/<int:category>/<int:item>/delete/')
def deleteItem(category, item):
    return 'delete item'



##################webserver#######################

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
