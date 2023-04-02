'''청주대학교 세션 실습 코드: session_server.py'''

from flask import Flask, render_template, redirect, request, session
from flask_session import Session

app = Flask(__name__)
# Flask config (app.config) 에서 설정 -> Session 객체 생성 시 업로드
app.config["SESSION_PERMANENT"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = 30  # 세션 유효기간 30초 설정
app.config["SESSION_TYPE"] = "filesystem"

# Flask app을 Session 객체에 로딩

# Session 객체 초기화 방법 1
Session(app)

# Session 객체 초기화 방법 2
# sess = Session()
# sess.init_app(app)


@app.route("/")
def index():
    '''메인화면 index.html 처리'''
    return render_template('index.html')


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


if __name__=='__main__':
    # app.run()
    app.run(host='0.0.0.0', port='5002', debug=True)
