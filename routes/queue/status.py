from flask import Blueprint, jsonify
from db.crud.get import get_queue

# Blueprintを作成
queue_status_bp = Blueprint("queue_status", __name__)

@queue_status_bp.route('/queue', methods=['GET'])
def current_queue():
    """現在のキューの状況を取得するエンドポイント"""
    queue = get_queue()
    return jsonify(queue)
