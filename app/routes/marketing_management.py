from flask import Blueprint
from ..controllers.marketing_management import disable_notifications

bp = Blueprint('marketing_management', __name__)

bp.route('/promotions/deactivate', methods=["GET"])(disable_notifications)