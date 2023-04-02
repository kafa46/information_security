'''청주대학교 정보보안 실습코드
XSS (Cross Script Scripting) 공격 실습
    - 공격대상 웹 서버: 블로그 서버로 실습
    ** 주의: 코딩을 단순화 하기 위해 애플리케이션 팩토리 구현은 생략
            (실제 서버 구축 시 블루프린트(blueprint)를 사용해야 함)
'''

from flask import Flask, render_template, redirect, request, session, make_response
from flask_session import Session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

# Flask config (app.config) 에서 설정 -> Session 객체 생성 시 업로드
app.config["SESSION_PERMANENT"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = 30  # 세션 유효기간 30초 설정
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

# Flask app을 Session 객체에 로딩
Session(app)

# DB 생성 및 초기화
db = SQLAlchemy()
db.init_app(app)

migrate = Migrate()
migrate.init_app(app)


@app.route('/')
def index():
    '''초기 접속 시 실행할 함수'''
    # return render_template(
    #     'index.html'
    # )

    # 쿠키 굽기(발행)
    response = make_response(
        render_template('index.html') # 템플릿 내용은 그대로 유지
    )

    if request.cookies:
        # 사용자의 쿠키 정보 읽어오기
        print('쿠키 정보가 있습니다. 방문한 적이 있습니다.')
        name = request.cookies.get('name')
        universtiy = request.cookies.get('universtiy')
        passwd = request.cookies.get('passwd')

        # 쿠키 정보 확인 -> 터미널에 출력
        print(f'name: {name}')
        print(f'university: {universtiy}')
        print(f'passwd: {passwd}')
    else:
        print('첫 방문자입니다. 쿠키를 굽습니다.')
        response.set_cookie('name', 'Hong Gil-dong') # 쿠키 굽기
        response.set_cookie('universtiy', 'Chongju University') # 또 다른 쿠키 굽기
        response.set_cookie('passwd', '1234', max_age=60*60*24*7) # 쿠키 유효 기간을 7일로 설정

    return response


@app.route("/login", methods=["POST", "GET"])
def login():
    '''로그인 처리'''
    # 만약 form을 작성하여 제출하면 (POST 전송)
    if request.method == "POST":

        # DB에서 id/passwd 확인을 마쳤다고 가정

    	# 접속세션 등록: 아이디와 비번을 세션에 등록
        session["id"] = request.form.get("id")
        session["passwd"] = request.form.get("passwd")

        # 로그인이 끝났으므로 메인 화면으로 이동
        return redirect("/")

	# 만약 일반 접속(GET 전송)이라면 로그인 페이지를 제공
    return render_template("login.html")


@app.route("/logout")
def logout():
    '''로그아웃 처리'''

    # 세션 초기화
    session["id"] = None
    session["passwd"] = None

    # 메인 화면으로 안내
    return redirect("/")


@app.route("/create")
def create():
    '''게시글 작성'''
    return render_template('create.html')


@app.route("/detail")
def detail():
    '''게시글 제목을 클릭할 경우 세부내용 보여주기'''

if __name__=='__main__':
    # app.run()
    app.run(host='0.0.0.0', port='5003', debug=True)
