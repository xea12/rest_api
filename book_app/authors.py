from flask import jsonify, request
from webargs.flaskparser import use_args
from book_app import app, db
from book_app.models import Authors, AuthorsSchema, authors_schema

@app.route('/api/v1/authors', methods=['GET'])
def get_authors():
    authors = Authors.query.all()
    authors_scheme = AuthorsSchema(many= True)
    return jsonify({
        'success': True,
        'data': authors_scheme.dump(authors),
        'number_of_records' : len(authors)
        })

@app.route('/api/v1/authors/<int:author_id>', methods=['GET'])
def get_author(author_id: int):
    author = Authors.query.get_or_404(author_id, description=f'Author with id {author_id} not found')
    return jsonify({
        'success': True,
        'data': authors_schema.dump(author)
        })


@app.route('/api/v1/authors', methods=['POST'])
@use_args(authors_schema)
def create_author(args: dict):
    author = Authors(**args)
    db.session.add(author)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': authors_schema.dump(author)
        }), 201

@app.route('/api/v1/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Author with id {author_id} has been updated'
        })

@app.route('/api/v1/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Author with id {author_id} has been deleted'
        })