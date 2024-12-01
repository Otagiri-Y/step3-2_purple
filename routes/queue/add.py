from flask import Blueprint, request, jsonify
from db.crud.add import add_to_queue

# Blueprintを作成
queue_add_bp = Blueprint("queue_add", __name__)

@queue_add_bp.route('/join', methods=['POST'])
def join_queue():
    """列にユーザーを追加するエンドポイント"""
    data = request.json
    name = data.get('name')
    email = data.get('email')
    people_count = data.get('people_count')

    # 必須フィールドが埋まっていない場合エラーを返す
    if not all([name, email, people_count]):
        return jsonify({"error": "All fields (name, email, people_count) are required."}), 400

    # 待ち時間を計算し、キューに追加
    waiting_time = people_count * 5
    add_to_queue(name, email, people_count, waiting_time)
    return jsonify({"message": "Added to queue"}), 201
