from ..models import db, Choice

def create_choice(question_id, text):
    choice = Choice(question_id=question_id, text=text)
    db.session.add(choice)
    db.session.commit()
    return choice

def get_choices(question_id):
    return Choice.query.filter_by(question_id=question_id).all()
