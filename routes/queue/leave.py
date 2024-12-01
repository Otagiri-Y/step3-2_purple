from flask import Blueprint, request, jsonify
from db.crud.remove import remove_from_queue

# Blueprintを作成
queue_leave_bp = Blueprint("queue_leave", __name__)

@queue_leave_bp.route('/leave', methods=['DELETE'])
def leave_queue():
    """キューからユーザーを削除するエンドポイント"""
    user_id = request.json.get('id')

    # ユーザーIDが提供されていない場合エラーを返す
    if not user_id:
        return jsonify({"error": "User ID is required."}), 400

    # キューから削除
    remove_from_queue(user_id)
    return jsonify({"message": f"User {user_id} has been removed from the queue"}), 200
