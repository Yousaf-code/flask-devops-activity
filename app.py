# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

students = {}
next_id = 1


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify(data), 201


@app.route('/student', methods=['POST'])
def create_student():
    global next_id
    data = request.get_json(force=True)

    student_id = next_id
    next_id += 1

    students[student_id] = data

    return jsonify({
        "message": "Student created",
        "student_id": student_id,
        "data": data
    }), 201


@app.route('/student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json(force=True)
    students[student_id] = data  # overwrite or create

    return jsonify({
        "message": "Student updated",
        "student_id": student_id,
        "data": data
    }), 200


@app.route('/student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    students.pop(student_id, None)  # remove if exists

    return jsonify({
        "message": "Student deleted",
        "student_id": student_id
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
