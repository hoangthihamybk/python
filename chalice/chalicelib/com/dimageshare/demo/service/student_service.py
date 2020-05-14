from chalicelib.com.dimageshare.demo.connector.mysql_connection import conn

def get_namest(id):
    cursor = conn.cursor()
    query = "SELECT name FROM student WHERE id = %s" %(id)
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def delete_student(id):
    cursor = conn.cursor()
    query = "DELETE FROM student WHERE id = %s" % (id)
    cursor.execute(query)


def creat_student(student):
    cursor = conn.cursor()
    id = student.id
    name = student.name
    address = student.address
    phone = student.phone
    student_tuple = [id, name, address, phone]
    cursor.execute('INSERT INTO `student`(`id`, `name`, `address`,`phone`) '
                   'values (%s, %s, %s, %s)', student_tuple)

def update_student(student):
    cursor = conn.cursor()
    id = student.id
    name = student.name
    address = student.address
    phone = student.phone
    update_student_tuple = [name, address, phone,id]
    cursor.execute('UPDATE student SET name = %s, address = %s, phone = %s WHERE id = %s ', update_student_tuple)
