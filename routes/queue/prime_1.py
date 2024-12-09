from flask import Blueprint, jsonify, request
from db.crud.prime_1 import prime_to_queue

# Blueprintを作成
queue_prime_bp = Blueprint("queue_prime_1", __name__)

@queue_prime_bp.route('/prime_1', methods=['POST'])
def prime_1_to_queue():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    people_count = data.get('people_count')

    # 必須フィールドが埋まっていない場合エラーを返す
    if not all([name, email, people_count]):
        return jsonify({"error": "All fields (name, email, people_count) are required."}), 400
    
    # 待ち時間を計算し、キューに追加
    waiting_time = people_count * 5
    
    prime_to_queue(name, email, people_count, waiting_time)
    return jsonify({"message": "Added to queue"}), 201

