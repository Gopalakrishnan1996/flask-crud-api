from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app1 = Flask(__name__)
if __name__ == '__main__':
    app1.run(debug=True)
db = SQLAlchemy(app1)
import tables
_books = tables.Books
_tables = tables.Summary

class SummaryDataAccess:

    def get_item(id):
         summary = _tables.query.get(id)
         if(summary != None):
          del summary.__dict__['_sa_instance_state']
          return jsonify(summary.__dict__)
         else: 
          return "No Data Found"

    def get_items():
        summary = []
        for item in db.session.query(_tables).all():
            del item.__dict__['_sa_instance_state']
            summary.append(item.__dict__)
        return jsonify(summary)

    def create_item(body):
        body = request.get_json()
        # Books stock update
        lsbookdet = _books.query.get(body['bookid'])
        if(lsbookdet.curstock <= 0):
            return "Book not available"
        if(body['type'] == 'I'):
          db.session.query(_books).filter_by(id=body['bookid']).update(
            dict(curstock=_books.curstock + 1))
        elif(body['type'] == 'O'):
           db.session.query(_books).filter_by(id=body['bookid']).update(
            dict(curstock= _books.curstock - 1)) 
        # summary create
        db.session.add(_tables(body['bookid'], body['studentid'], body['studentname'], body['bookname'], body['getdate'], body['retdate'], body['type']))
        db.session.commit()
        return "Data created"

    def update_item(id, body):
        body = request.get_json()
        # Books stock update
        if(body['type'] == 'I'):
          db.session.query(_books).filter_by(id=body['bookid']).update(
            dict(curstock=body['curstock'] + 1))
        elif(body['type'] == 'O'):
           db.session.query(_books).filter_by(id=body['bookid']).update(
            dict(curstock=body['curstock'] - 1))   
        
        # summary stock insert
        db.session.query(_tables).filter_by(id=id).update(
            dict(bookid=body['bookid'], studentid=body['studentid'], studentname=body['studentname'], bookname=body['bookname'], getdate=body['getdate'], retdate=body['retdate'], type=body['type']))
        db.session.commit()
        return "Data updated"

    def delete_item(id):
        db.session.query(_tables).filter_by(id=id).delete()
        db.session.commit()
        return "Data deleted"

    def cur_available():
        lsava = db.session.query(_books).filter_by(_books.curstock >=0)
        # db.session.commit()
        return jsonify(lsava)

