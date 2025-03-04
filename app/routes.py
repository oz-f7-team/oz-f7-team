from flask import Blueprint, request, jsonify
from .services.users import create_user, get_users
from .services.questions import create_question, get_questions
from .services.choices import create_choice, get_choices
from .services.images import create_image, get_images
from .services.answers import create_answer, get_answers

api_bp = Blueprint("api", __name__)

@api_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    user = create_user(data["name"], data["email"], data["gender"], data["age_group"])
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

@api_bp.route("/users", methods=["GET"])
def list_users():
    users = get_users()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@api_bp.route("/questions", methods=["POST"])
def add_question():
    data = request.get_json()
    question = create_question(data["text"])
    return jsonify({"id": question.id, "text": question.text}), 201

@api_bp.route("/questions", methods=["GET"])
def list_questions():
    questions = get_questions()
    return jsonify([{"id": q.id, "text": q.text} for q in questions])

@api_bp.route("/choices", methods=["POST"])
def add_choice():
    data = request.get_json()
    choice = create_choice(data["question_id"], data["text"])
    return jsonify({"id": choice.id, "text": choice.text}), 201

@api_bp.route("/choices/<int:question_id>", methods=["GET"])
def list_choices(question_id):
    choices = get_choices(question_id)
    return jsonify([{"id": c.id, "text": c.text} for c in choices])

@api_bp.route("/images", methods=["POST"])
def add_image():
    data = request.get_json()
    image = create_image(data["url"])
    return jsonify({"id": image.id, "url": image.url}), 201

@api_bp.route("/images", methods=["GET"])
def list_images():
    images = get_images()
    return jsonify([{"id": i.id, "url": i.url} for i in images])

@api_bp.route("/answers", methods=["POST"])
def add_answer():
    data = request.get_json()
    answer = create_answer(data["user_id"], data["question_id"], data["choice_id"])
    return jsonify({"id": answer.id}), 201

@api_bp.route("/answers", methods=["GET"])
def list_answers():
    answers = get_answers()
    return jsonify([{"id": a.id, "user_id": a.user_id, "question_id": a.question_id, "choice_id": a.choice_id} for a in answers])

@api_bp.route("/users/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    data = request.get_json()
    user = update_user(user_id, data.get("name"), data.get("email"), data.get("gender"), data.get("age_group"))
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email})

@api_bp.route("/users/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    success = delete_user(user_id)
    if not success:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200
