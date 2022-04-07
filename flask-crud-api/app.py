from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import items
import students
import tables
import Books
import Summary
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/Item?user=postgres&password=@gk11051996@'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
object = items.ItemsDataAccess
object1 = students.StudentsDataAccess
object2 = Books.BookDataAccess
object3 = Summary.SummaryDataAccess
tables.Students
tables.Item
tables.Books
tables.Summary

# items crud methods
@app.route('/items/<id>', methods=['GET'])
def get_item(id):
    return object.get_item(id)

@app.route('/items', methods=['GET'])
def get_items():
    return object.get_items()

@app.route('/items', methods=['POST'])
def create_item():
  body = request.get_json()
  return object.create_item(body)

@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
  body = request.get_json()
  return object.update_item(id,body)

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
   return object.delete_item(id)

# items crud methods end

# students crud methods
@app.route('/student/<id>', methods=['GET'])
def get_student(id):
    return object1.get_item(id)

@app.route('/students', methods=['GET'])
def get_students():
    return object1.get_items()

@app.route('/student', methods=['POST'])
def create_student():
  body = request.get_json()
  return object1.create_item(body)

@app.route('/student/<id>', methods=['PUT'])
def update_student(id):
  body = request.get_json()
  return object1.update_item(id,body)

@app.route('/student/<id>', methods=['DELETE'])
def delete_student(id):
   return object1.delete_item(id)
# students crud methods end

# Books crud methods

@app.route('/book/<id>', methods=['GET'])
def get_book(id):
    return object2.get_item(id)

@app.route('/books', methods=['GET'])
def get_books():
    return object2.get_items()

@app.route('/book', methods=['POST'])
def create_book():
  body = request.get_json()
  return object2.create_item(body)

@app.route('/book/<id>', methods=['PUT'])
def update_book(id):
  body = request.get_json()
  return object2.update_item(id,body)

@app.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
   return object2.delete_item(id)
# Books crud methods end   

# summary crud methods 

@app.route('/summary/<id>', methods=['GET'])
def get_summary(id):
    return object3.get_item(id)

@app.route('/summarys', methods=['GET'])
def get_summarys():
    return object3.get_items()

@app.route('/summary', methods=['POST'])
def create_summary():
  body = request.get_json()
  return object3.create_item(body)

@app.route('/summary/<id>', methods=['PUT'])
def update_summary(id):
  body = request.get_json()
  return object3.update_item(id,body)

@app.route('/summary/<id>', methods=['DELETE'])
def delete_summary(id):
   return object3.delete_item(id)
@app.route('/cur_available', methods=['GET'])
def cur_available():
    return object3.cur_available()

@app.route('/Allocate_Book', methods=['GET'])
def Allocate_Book():
    return object3.Allocate_Book() 

@app.route('/Most_read_Book/<frmdate>/<todate>', methods=['GET'])
def Most_read_Book(frmdate,todate):
    return object3.Most_read_Book(frmdate,todate) 

@app.route('/Return_Book', methods=['GET'])
def Return_Book():
    return object3.Return_Book()               
# summary crud methods end   