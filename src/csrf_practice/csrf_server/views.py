from datetime import datetime
from flask import (
    flash,
    request,
    session,
    Blueprint,
    make_response,
    render_template,
    redirect,
)
from .models import Blog, User
from csrf_server import db
from csrf_server.utils import create_csrf_token
from csrf_server.forms import PersonalInfomationForm

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    '''초기 접속 시 실행할 함수'''
    # 쿠키 굽기(발행)
    posts = Blog.query.order_by(Blog.create_date.desc())
    context = posts.paginate(per_page=10)
    response = make_response(
        render_template(
            'index.html',
             context=context,
        ), # 템플릿 내용은 그대로 유지
    )

    if request.cookies.get('name'):
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
        max_time = 60*60*24*7 # 쿠키 유효 기간을 7일로 설정
        response.set_cookie('name', 'Hong Gil-dong', max_age=max_time) # 쿠키 굽기
        response.set_cookie('universtiy', 'Chongju University', max_age=max_time) # 또 다른 쿠키 굽기
        response.set_cookie('passwd', '1234', max_age=max_time)  # 쿠키 한개 더 굽기

    return response


@bp.route("/login", methods=["POST", "GET"])
def login():
    '''로그인 처리'''
    # 만약 form을 작성하여 제출하면 (POST 전송)
    if request.method == "POST":
        # 접속자 검증
        user_id = request.form.get('id')
        user_in_db = User.query.filter(User.user_id==user_id).first()
        print(f'user_in_db: {user_in_db}, type: {type(user_in_db)}')
        if not user_in_db:
            flash('존재하지 않는 아이디 입니다.')
            return render_template('login.html')
        passwd = request.form.get('passwd')
        if passwd != user_in_db.passwd:
            flash('비밀번호가 일치하지 않습니다.')
            return render_template('login.html')

    	# 접속세션 등록: 아이디와 비번을 세션에 등록
        session["id"] = request.form.get("id")
        session["passwd"] = request.form.get("passwd")

        # 로그인이 끝났으므로 메인 화면으로 이동
        return redirect("/")

	# 만약 일반 접속(GET 전송)이라면 로그인 페이지를 제공
    return render_template("login.html")


@bp.route("/logout")
def logout():
    '''로그아웃 처리'''
    # 세션 초기화
    session["id"] = None
    session["passwd"] = None

    # 메인 화면으로 안내
    return redirect("/")


@bp.route("/create", methods=["POST", "GET"])
def create():
    '''게시글 작성'''
    if request.method=='POST':
        '''게시글 저장'''
        title = request.form.get('title')
        content = request.form.get('content')
        blog = Blog()
        blog.title = title
        blog.content = content
        blog.writer = session.get('id')
        blog.create_date = datetime.now()

        db.session.add(blog)
        db.session.commit()

        print(content)
        print(session.get('id'))
        return redirect('/')

    # GET 요청일 경우 작성 양식 제공
    return render_template(
        'create.html',
    )


@bp.route("/detail/<int:post_id>")
def detail(post_id):
    '''게시글 제목을 클릭할 경우 세부내용 보여주기'''
    post = Blog.query.get(post_id)
    return render_template(
        'detail.html',
        context=post,
    )

@bp.route("/modify/<int:post_id>", methods=["POST", "GET"])
def modify(post_id):
    '''게시글 내용 수정'''
    if request.method=='POST':
        post = Blog.query.get(post_id)
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        post.writer = session.get('id')
        post.create_date = datetime.now()
        db.session.commit()
        return redirect('/')

    post = Blog.query.get(post_id)
    return render_template(
        'modify.html',
        context=post,
    )

@bp.route("/delete/<int:post_id>")
def delete(post_id):
    '''게시글 제목을 클릭할 경우 세부내용 보여주기'''
    post = Blog.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/')

@bp.route("/register", methods=["POST", "GET"])
def register():
    if request.method=='POST':
        required_info = []
        user_id = request.form.get('user_id')
        check_user = User.query.filter(User.user_id==user_id).first()
        if check_user:
            flash('이미 존재하는 아이디 입니다.')
            return redirect('/register')
        required_info.append(user_id)
        passwd = request.form.get('passwd')
        required_info.append(passwd)
        name = request.form.get('name')
        required_info.append(name)
        email = request.form.get('email')
        required_info.append(email)
        university = request.form.get('university')
        required_info.append(university)
        print(f'user_id: {user_id}\tpasswd: {passwd}\tname: {name}\tuniversity: {university}')
        if not all(required_info):
            flash('모든 정보를 입력하지 않았습니다.')
            return redirect('/register')
        user = User()
        user.user_id = user_id
        user.passwd = passwd
        user.name = name
        user.email = email
        user.university = university
        db.session.add(user)
        db.session.commit()
        flash(f'회원가입에 성공했습니다. 로그인 해주세요')
        return redirect('/login')
    return render_template(
        'register.html',
    )

@bp.route("/person_info", methods=["POST", "GET"])
def person_info():
    user_id = session.get('id')
    print(f'user_id: {user_id}')
    user = User.query.filter(User.user_id==user_id).first()

    if request.method=='POST':
        # # referrer 검증 코드
        # referrer = request.referrer
        # our_domain = request.host_url
        # print(f'\nreferrer: {referrer}')
        # print(f'our domain: {our_domain}')
        # # 현재 서버(도메인) 이외의 request는 차단
        # if not our_domain in referrer:
        #     flash(f'정당한 페이지 요청이 아닙니다.\
        #         <br>우리 도메인: {our_domain}\
        #         <br>요청 도메인: {referrer}\
        #         <br>수정 요청이 거부되었습니다!!')
        #     return redirect('/') # 메인으로 이동

        # csrf_token 검증 코드
        # csrf_token = request.form.get('csrf_token')
        # print(f'\nreferrer: {request.referrer}')
        # print(f'referrer csrf_token: {csrf_token}')
        # print(f'session csrf_token: {session["csrf_token"]}')
        # if csrf_token != session['csrf_token']:
        #     flash('csrf 토큰이 일치하지 않습니다.\
        #         <br>수정요청이 거부되었습니다.')
        #     return redirect('/') # 메인으로 이동
        # # csrf_token 초기화
        # session['csrf_token'] = None

        # form에서 필요한 정보 추출
        user_id = request.form.get('user_id')
        passwd = request.form.get('passwd')
        name = request.form.get('name')
        email = request.form.get('email')
        university = request.form.get('university')
        print(f'\nuser_id: {user_id}\tpasswd: {passwd}\tname: {name}\tuniversity: {university}')

        user = User.query.filter(User.user_id==user_id).first()
        user.user_id = user_id
        user.passwd = passwd
        user.name = name
        user.email = email
        user.university = university
        db.session.commit()
        flash('개인정보 수정을 완료하였습니다.')
        return redirect('/')

    csrf_token = create_csrf_token()
    session['csrf_token'] = csrf_token
    return render_template(
        'person_info_hack.html',
        # 'person_info_secure.html',
        user=user,
        csrf_token = csrf_token
    )


@bp.route("/person_info_secure", methods=["POST", "GET"])
def person_info_secure():
    user_id = session.get('id')
    user = User.query.filter(User.user_id==user_id).first()
    form = PersonalInfomationForm()
    
    if request.method=='POST' and form.validate_on_submit():
        print('test')
        # form에서 필요한 정보 추출
        user_id = request.form.get('user_id')
        passwd = request.form.get('passwd')
        name = request.form.get('name')
        email = request.form.get('email')
        university = request.form.get('university')
        print(f'\nuser_id: {user_id}\tpasswd: {passwd}\tname: {name}\tuniversity: {university}')
        # DB update
        user = User.query.filter(User.user_id==user_id).first()
        user.user_id = user_id
        user.passwd = passwd
        user.name = name
        user.email = email
        user.university = university
        db.session.commit()
        flash('개인정보 수정을 완료하였습니다.')
        return redirect('/')

    return render_template(
        'person_info_flask_form.html',
        user=user,
        form=form,
    )
