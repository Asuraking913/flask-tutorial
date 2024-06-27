from models import db, Author, Books
from flask import request, redirect, url_for, render_template

def roout_route(app):
    
    @app.route("/")
    def home(): 
        return "This is the home page"
    
    @app.route("/create", methods = ['POST', 'GET'])
    def create_usr(): 
        if request.method == "POST":
            authorname = request.form['author']
            bookname = request.form['book']

            new_author = Author(name = authorname)
            db.session.add(new_author)
            db.session.commit()
            if authorname != "":
                new_book = Books(name = bookname, author = new_author)
                db.session.add(new_book)
                db.session.commit()
            


            return "Done"
        else:
            return render_template("index.html")