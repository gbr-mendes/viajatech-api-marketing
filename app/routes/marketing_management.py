from crypt import methods
from flask import Blueprint
from ..controllers.marketing_management import disable_notifications, create_marketing_capaing, list_emails_marketing

bp = Blueprint('marketing_management', __name__)

bp.route('/promotions/deactivate', methods=["GET"])(disable_notifications)
bp.route('/promotions/create-campaing', methods=["POST"])(create_marketing_capaing)
bp.route('/promotions/campaigns', methods=["GET"])(list_emails_marketing)