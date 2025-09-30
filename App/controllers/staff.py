from App.models import staff
from App.database import db

def create_staff(username, password):
    newuser = staff(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_staff_by_username(username):
    result = db.session.execute(db.select(staff).filter_by(username=username))
    return result.scalar_one_or_none()

def get_staff(id):
    return db.session.get(staff, id)

def get_all_staff():
    return db.session.scalars(db.select(staff)).all()

def get_all_staff_json():
    users = get_all_staff()
    if not staff:
        return []
    staff = [staff.get_json() for user in users]
    return staff

def update_user(id, username):
    staff = get_staff(id)
    if staff:
        staff.username = username
        # user is already in the session; no need to re-add
        db.session.commit()
        return True
    return None
