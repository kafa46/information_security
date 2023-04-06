'''청주대학교 정보보안 실습코드
XSS (Cross Script Scripting) 공격 실습
    - 공격대상 웹 서버: 블로그 서버로 실습
    ** 주의: 코딩을 단순화 하기 위해 애플리케이션 팩토리 구현은 생략
            (실제 서버 구축 시 블루프린트(blueprint)를 사용해야 함)
'''

from flask import Flask, render_template, redirect, request, session, make_response
# from models import Blog
from flask_session import Session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()   # DB 객체 생성
migrate = Migrate() # Migrateion 객체

def create_app():
    app = Flask(__name__)
    app.config.from_object(config) # config.py 내용을 설정에 적용
    app.config["SESSION_PERMANENT"] = True
    app.config["SESSION_TYPE"] = "filesystem"

    # 블루프린트 등록
    from .views import bp
    app.register_blueprint(bp)
    
    # Flask app을 Session 객체에 로딩
    Session(app)

    # DB 초기화
    db.init_app(app)
    
    # Migration 초기화
    migrate.init_app(app, db)
    from . import models
    
    # 필터 등록
    from .filters import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    return app
