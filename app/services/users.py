from ..models import db, User

def create_user(name, email, gender, age_group):
    user = User(name=name, email=email, gender=gender, age_group=age_group)
    db.session.add(user)
    db.session.commit()
    return user

def get_users():
    return User.query.all()

def update_user(user_id, name=None, email=None, gender=None, age_group=None):
    user = User.query.get(user_id)
    if not user:
        return None
    if name:
        user.name = name
    if email:
        user.email = email
    if gender:
        user.gender = gender
    if age_group:
        user.age_group = age_group
    db.session.commit()
    return user

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return None
    db.session.delete(user)
    db.session.commit()
    return True