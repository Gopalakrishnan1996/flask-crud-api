from msilib.schema import Class
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
db = SQLAlchemy(app)
import tables
_tables = tables.Item
   
class ItemsDataAccess:
    def get_item(id):
        item = _tables.query.get(id)
        del item.__dict__['_sa_instance_state']
        return jsonify(item.__dict__)

    def get_items():
        items = []
        for item in db.session.query(_tables).all():
            del item.__dict__['_sa_instance_state']
            items.append(item.__dict__)
        return jsonify(items)

    def create_item(body):
        body = request.get_json()
        db.session.add(_tables(body['title'], body['content']))
        db.session.commit()
        return "item created"

    def update_item(id,body):
        body = request.get_json()
        db.session.query(_tables).filter_by(id=id).update(
            dict(title=body['title'], content=body['content']))
        db.session.commit()
        return "item updated"
        
    def delete_item(id):
        db.session.query(_tables).filter_by(id=id).delete()
        db.session.commit()
        return "item deleted"
