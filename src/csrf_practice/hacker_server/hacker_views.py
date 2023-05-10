from datetime import datetime
from flask import request, session, Blueprint, render_template, redirect
from .models import Hacker

bp = Blueprint('hacker_main', __name__, url_prefix='/')

@bp.route('/csrf', methods=["POST", "GET"])
def csrf():
    return render_template(
        # # Secure coding 적용되지 않은 페이지 공격
        # 'hack_unsecure.html',
        
        # # 개발자가 구현한 referrer, csrf_token 적용된 페이지 공격
        # 'hack_secure_coding.html',
        
        # flask-form 적용된 페이지 공격
        'hack_flask_form.html',
    )
