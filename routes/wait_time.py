from flask import Blueprint, jsonify
from db.crud.reset import reset_queue_on_threshold
from db.crud.total import get_total_waiting_time

# Blueprintを作成
wait_time_bp = Blueprint("wait_time", __name__)


@wait_time_bp.route('/wait-time', methods=['GET'])
def wait_time():
    """
    待機時間を取得し、条件に応じて列データをリセット
    """
    try:
        # 合計待機時間を取得
        total_waiting_time = get_total_waiting_time()

        # 条件を満たしていればリセット
        reset_queue_on_threshold()

        return jsonify({"total_waiting_time": total_waiting_time}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

