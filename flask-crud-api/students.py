from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app1 = Flask(__name__)
if __name__ == '__main__':
    app1.run(debug=True)
db = SQLAlchemy(app1)
import tables
_tables = tables.Students
class StudentsDataAccess:
    
    def get_item(id):
         students = _tables.query.get(id)
         if(students != None):
          del students.__dict__['_sa_instance_state']
          return jsonify(students.__dict__)
         else: 
            return "No Data Found"

    def get_items():
        students = []
        for item in db.session.query(_tables).all():
            del item.__dict__['_sa_instance_state']
            students.append(item.__dict__)
        return jsonify(students)

    def create_item(body):
        body = request.get_json()
        db.session.add(_tables(body['name'], body['std'], body['regno']))
        db.session.commit()
        return "Data created"

    def update_item(id, body):
        body = request.get_json()
        db.session.query(_tables).filter_by(id=id).update(
            dict(name=body['name'], std=body['std'], regno=body['regno']))
        db.session.commit()
        return "Data updated"

    def delete_item(id):
        db.session.query(_tables).filter_by(id=id).delete()
        db.session.commit()
        return "Data deleted"
