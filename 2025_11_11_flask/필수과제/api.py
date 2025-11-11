from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema

book_list = [
    {"title" : "그리스로마신화", "author": "이지훈"},
    {"title" : "그리스로마신화2", "author": "강지훈"}
]

blp = Blueprint("books", "books", url_prefix="/books", description="Operations on books")

@blp.route("/")
class BookList(MethodView):
    @blp.response(200)
    def get(self):
        return book_list

    @blp.arguments(ItemSchema)
    @blp.response(201)
    def post(self, data):
        book_title = data["title"]

        if any(book for book in book_list if book["title"] == book_title):
            abort(400, message="Item already exists")

        book_list.append(data)
        return data, 201

@blp.route("/<string:book_title>")
class Book(MethodView):
    @blp.response(200)
    def get(self, book_title):
        book = next((book for book in book_list if book["title"] == book_title), None)
        if book is None:
            abort(404, message="Book not found")
        return book

    @blp.arguments(ItemSchema)
    @blp.response(200)
    def put(self, data, book_title):
        book = next((book for book in book_list if book["title"] == book_title), None)
        if book is None:
            abort(404, message="Book not found")
        book.update(data)

    @blp.response(200)
    def delete(self, book_title):
        global book_list
        if not any(book for book in book_list if book["title"] == book_title):
            abort(404, message="Book not found")

        book_list = [book for book in book_list if book["title"] != book_title]
        return ''


