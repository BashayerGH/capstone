import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Book, Category
from auth import AuthError, requires_auth


BOOKS_PER_PAGE = 10
BASE = '/api/booksgallery/v1';


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)



  @app.route('/')
  def get_greeting():
    excited = os.getenv('EXCITED', 'true')
    greeting = "Hello, welcome to Book Gallery" 
    if excited == 'true': greeting = greeting + "!!!"
    return greeting

  # GET all available categories
  @app.route(BASE+'/categories')
  @requires_auth('get:categories')
  def all_categories(self):
    try:
      all_categories = Category.query.all()
      categories_list = [category.format() for category in all_categories]
      if len(categories_list) == 0:
        abort(404)
      categories_formatted = {}
      for category in categories_list:
        categories_formatted.update({category.get("id"): category.get("type")})
      return jsonify({
        'categories': categories_formatted,
        'success': True
      })
    except Exception:
      abort(500)


  # GET all available books
  @app.route(BASE+'/books')
  @requires_auth('get:books')
  def all_books(self):
    try:
      all_books = Book.query.all()
      books_list = books_list_paginated(request, all_books)
      if len(books_list) == 0:
        abort(404)

      return jsonify({
        'books': books_list,
        'total': len(all_books),
        'totalPerRequest': len(books_list),
        'success': True
      })
    except Exception:
      abort(500)


  @app.route(BASE+'/books', methods=['POST'])
  @requires_auth('post:books')
  def post_new_book(self):
    try:
        data = request.json
        category = int(data['category'])
        title = data['title']
        sub_title = data['sub_title']
        author = data['author']
        publisher = data['publisher']
        pages = int(data['pages'])
        publish_date = data['publish_date']
        description = data['description']

        if (title == '' or author == '' or publish_date == ''):
          abort(422)

        Book(title=title, sub_title=sub_title, author=author, category=category, publisher=publisher, pages=pages, publish_date=publish_date, description=description).insert()

        return jsonify({
          'book': title,
          'description': description,
          'category': category,
          'success': True
        })

    except Exception:
      abort(422)


  @app.route(BASE+'/books/<int:id>', methods=['DELETE'])
  @requires_auth('delete:books')
  def remove_book(id):
    try:
      deleted_book = Book.query.filter(Book.id == id).one_or_none()
      if deleted_book is None:
        abort(404)
      else:
        deleted_book.delete()
        return jsonify({
          'success': True
        })
    except Exception:
        abort(422)


  @app.route(BASE+'/categories/<int:category>/books')
  @requires_auth('get:booksByCategory')
  def books_by_category_id(category):
    filtered_books = Book.query.filter(Book.category == category).all()
    page_books = books_list_paginated(request, filtered_books)
    if (page_books == None):
        abort(404)

    try:
        total = len(page_books)

        if total == 0:
          abort(404)

        else:
          return jsonify({
            'books': page_books,
            'total': total,
            'category_id': category,
            'success': True
          })
    except Exception:
        abort(422)



  # Search for a book by its (title, author)
  @app.route(BASE+'/books/search', methods=['POST'])
  @requires_auth('get:booksBySearchTerm')
  def search(self):
    data = request.json
    searchTerm = data['searchTerm']
    if (searchTerm == ''):
      abort(404)
    else:
      books = Book.query.filter(Book.title.ilike('%{}%'.format(searchTerm))).all()
      if (data == None):
        abort(404)

      try:
        books = [book.format() for book in books]
        total = len(books)
        category = books[0]['category']
        return jsonify({
              'books': books,
              'total': total,
              'category_id': category,
              'success': True
        })
      except Exception:
        abort(422)


  @app.route(BASE+'/books/<int:book_id>', methods=['PATCH'])
  @requires_auth('edit:books')
  def update_existing_book(book_id):
    data = request.json
    title = data['title']
    subtitle = data['sub_title']
    description = data['description']


    book = Book.query.filter(Book.id == book_id).first()
    if (data is {} or book == None):
        abort(404)


    # the user can only edit title, subtitle, description
    try:
        book.title = title
        book.sub_title = subtitle
        book.description = description
        book.update()

        return jsonify({
            "success": True,
            "book": book.format()
        }), 200
    except Exception:
        abort(422)


  # Common methods
  def books_list_paginated(request, list):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * BOOKS_PER_PAGE
    end = start + BOOKS_PER_PAGE
    books_list = [book.format() for book in list]
    books_paginated = books_list[start:end]
    return books_paginated



  # Error handler for expected error 404
  @app.errorhandler(404)
  def not_found(error):
        return (
            jsonify({
              'error': 404,
              'message': 'Resource not found',
              'success': False }),
            404,
        )

  # Error handler for expected error 422
  @app.errorhandler(422)
  def unprocessable(error):
      return (
            jsonify({
              'error': 422,
              'message': 'Unprocessable',
              'success': False }),
            422,
        )

  # Error handler for expected error 500
  @app.errorhandler(500)
  def server_error(error):
      return (
            jsonify({
              'error': 500,
              'message': 'Internal server error',
              'success': False }),
            500,
        )

  @app.errorhandler(AuthError)
  def auth_error(error):
      print(error)
      return jsonify({
          'success': False,
          'error': error.status_code,
          'message': error.error['description']
      }), error.status_code

  return app

app = create_app()

if __name__ == '__main__':
    app.run()