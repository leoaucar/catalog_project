from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

import datetime

app = Flask(__name__)

engine = create_engine('sqlite:///catalogproject.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/home')
def showHome():
    return render_template('home.html')


#############Routes for categories#############

@app.route('/category/')
def allCategories():
    categories = session.query(Category).order_by(asc(Category.name))
    return render_template('categories.html', categories=categories)

@app.route('/category/<int:category>/')
def showCategory(category):
    return 'category'

@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        if 'spotlight' in request.form:
            spotlight = True
        else:
            spotlight = False
        newCategory = Category(name=request.form['name'],
                               description=request.form['description'],
                               last_edit=datetime.datetime.now(),
                               user_id='1',
                               spotlight= spotlight)
        session.add(newCategory)
        session.commit()
        return redirect(url_for('showHome'))
    else:
        return render_template('newcategory.html')

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
