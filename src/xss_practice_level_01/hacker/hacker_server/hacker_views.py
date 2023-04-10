from datetime import datetime
from flask import request, session, Blueprint, make_response, render_template, redirect
from .models import Hacker
from hacker_server import db

bp = Blueprint('hacker_main', __name__, url_prefix='/')

@bp.route('/', methods=["POST", "GET"])
def index():
    '''초기 접속 시 실행할 함수'''
    return redirect('/hacker_home')

@bp.route('/hacker_home', methods=["POST", "GET"])
def hacker_home():
    '''해커 홈'''
    hacker = Hacker.query.order_by(Hacker.create_date.desc())
    context = hacker.paginate(per_page=10)
    return render_template(
        'index.html',
        context=context,
    )

@bp.route('/xss/', methods=["POST", "GET"])
def xss():
    hacker = Hacker()
    hacker.create_date = datetime.now()
    hacker.title = request.args.get('title')
    hacker.content = request.args.get('content')
    db.session.add(hacker)
    db.session.commit()
    return redirect(request.referrer)