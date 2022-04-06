from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app1 = Flask(__name__)
if __name__ == '__main__':
    app1.run(debug=True)
db = SQLAlchemy(app1)
import tables
_tables = tables.Books
class BookDataAccess:

    def get_item(id):
         books = _tables.query.get(id)
         if(books != None):
          del books.__dict__['_sa_instance_state']
          return jsonify(books.__dict__)
         else: 
            return 'No Data found'

    def get_items():
        books = []
        for item in db.session.query(_tables).all():
            del item.__dict__['_sa_instance_state']
            books.append(item.__dict__)
        return jsonify(books)

    def create_item(body):
        body = request.get_json()
        db.session.add(_tables(body['name'], body['author'], body['price'], body['maxcount'], body['curstock']))
        db.session.commit()
        return "Data created"

    def update_item(id, body):
        body = request.get_json()
        db.session.query(_tables).filter_by(id=id).update(
            dict(name=body['name'], author=body['author'], price=body['price'], maxcount=body['maxcount'], curstock=body['curstock']))
        db.session.commit()
        return "Data updated"
        
    def delete_item(id):
        db.session.query(_tables).filter_by(id=id).delete()
        db.session.commit()
        return "Data deleted"
