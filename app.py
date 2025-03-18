from flask import Flask,jsonify



todo=Flask('__name__')

students = [
    {
        'id': '1',
        'student_name': 'std1',
        'age': 21,
        'email': 'hi@gmail.com'
    },
    {
        'id': '2',
        'student_name': 'std2',
        'age': 22,
        'email': 'hello@gmail.com'
    },
    {
        'id': '3',
        'student_name': 'std3',
        'age': 23,
        'email': 'hi5@gmail.com'
    },
    {
        'id': '4',
        'student_name': 'std4',
        'age': 21,
        'email': 'hi6@gmail.com'
    },
    {
        'id': '5',
        'student_name': 'std5',
        'age': 21,
        'email': 'hi7@gmail.com'
    }
]


@todo.route('/students_list')
def students_list():
    return jsonify(students)


@todo.route('/students_list/get/<int:id>')
def student_get_by_id(id):
    for id in students:
        print(id)
        return "I will get student id"

if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )