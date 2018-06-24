# coding=utf-8

from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema


# create the flask application
app = Flask(__name__)

# generate database schema
Base.metadata.create_all(engine)


@app.route('/exams')
def get_exams():
    # fetch from the database
    session = Session()
    exam_objects = session.query(Exam).all()

    # transforming into JSON serializable objects
    schema = ExamSchema(many=True)
    exam = schema.dump(exam_objects)

    session.close()
    return jsonify(exam.data)


@app.route('/exams', methods=['POST'])
def add_exam():
    # mount an exam object
    posted_exam = ExamSchema(only=('title', 'description')).load(request.get_json())

    exam = Exam(**posted_exam.data, created_by="HTTP Post request")

    # persist exam
    session = Session()
    session.add(exam)
    session.commit()

    new_exam = ExamSchema().dump(exam).data

    session.close()

    return jsonify(new_exam), 201

