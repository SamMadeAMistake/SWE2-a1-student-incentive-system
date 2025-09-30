from App.models import student
from App.database import db

def create_stu(username, password):
    newStu = student(username=username, password=password)
    db.session.add(newStu)
    db.session.commit()
    return newStu

def get_student_by_username(username):
    result = db.session.execute(db.select(student).filter_by(username=username))
    return result.scalar_one_or_none()

def get_stu(id):
    return db.session.get(student, id)

def get_all_stu():
    return db.session.scalars(db.select(student)).all()

def get_all_stu_json():
    users = get_all_stu()
    if not student:
        return []
    student = [student.get_json() for user in users]
    return student

def update_stu(id, username):
    user = get_stu(id)
    if student:
        student.username = username
        # user is already in the session; no need to re-add
        db.session.commit()
        return True
    return None
