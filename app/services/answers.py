from ..models import db, Answer

def create_answer(user_id, question_id, choice_id):
    answer = Answer(user_id=user_id, question_id=question_id, choice_id=choice_id)
    db.session.add(answer)
    db.session.commit()
    return answer

def get_answers():
    return Answer.query.all()
