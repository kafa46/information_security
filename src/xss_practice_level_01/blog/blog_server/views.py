from datetime import datetime
from flask import (
    request, 
    session,
    Blueprint, 
    make_response, 
    render_template, 
    redirect,
)
from .models import Blog
from blog_server import db

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

        # 서버는 DB를 검색해서 id/passwd 확인을 마쳤다고 가정

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