from flask import Flask, request, jsonify

app = Flask(__name__)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},

    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"},
    {"id": 4, "title": "Book 4", "author": "Author 4"},
    {"id": 5, "title": "Book 5", "author": "Author 5"},
]


@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if "title" in data and "author" in data:
        new_book = {
            "id": len(books) + 1,
            "title": data["title"],
            "author": data["author"]
        }
        books.append(new_book)
        return jsonify({"message": "Book created successfully"}), 201
    else:
        return jsonify({"error": "Title and author are required"}), 400


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((book for book in books if book["id"] == book_id), None)
    if book is not None:
        book["title"] = data.get("title", book["title"])
        book["author"] = data.get("author", book["author"])
        return jsonify({"message": "Book updated successfully"})
    else:
        return jsonify({"error": "Book not found"}), 404


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is not None:
        books.remove(book)
        return jsonify({"message": "Book deleted successfully"})
    else:
        return jsonify({"error": "Book not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
