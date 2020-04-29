from urllib.parse import parse_qs

from chalice import Chalice, Response

from chalicelib.com.dimageshare.demo.entity.student import Student
from chalicelib.com.dimageshare.demo.service import student_service
from chalicelib.com.dimageshare.demo.service.student_service import *

app = Chalice(app_name='helloworld')


@app.route('/student/{id}', methods=['GET','DELETE'])
def get_name(id):
    request = app.current_request
    if request.method == 'GET':
        name = get_namest(id)
        return Response(status_code=200, body={'hello': name})
    elif request.method == 'DELETE':
        delete_student(id)

@app.route('/student', methods=['POST'])
def creat_student():
    current_request = app.current_request
    json_body = current_request.json_body
    id = json_body.get('id')
    name = json_body.get('name')
    address = json_body.get('address')
    phone = json_body.get('phone')
    student = Student(id,name,address,phone)
    data_response = student_service.creat_student(student)
    body = data_response.get_body()
    return Response(status_code=200, body=body)

@app.route('/student', methods=['PUT'])
def update_student():
    current_request = app.current_request
    json_body = current_request.json_body
    id = json_body.get('id')
    name = json_body.get('name')
    address = json_body.get('address')
    phone = json_body.get('phone')
    student = Student(id,name,address,phone)
    data_response = student_service.update_student(student)
    body = data_response.get_body()
    return Response(status_code=200, body=body)


































# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
