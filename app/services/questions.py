from ..models import db, Question

def create_question(text):
    question = Question(text=text)
    db.session.add(question)
    db.session.commit()
    return question

def get_questions():
    return Question.query.all()
