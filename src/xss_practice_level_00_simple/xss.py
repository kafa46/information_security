'''
Reference:
    https://www.youtube.com/watch?v=DoN7bkdQBXU
    https://www.youtube.com/watch?v=cehEkpWl7fg
    https://www.youtube.com/watch?v=YvmetHjjPek
    
'''

# import markdown
from flask import Flask, redirect, request, session, render_template, flash, make_response

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route("/", methods=['GET', 'POST'])
def index():
    response = make_response(
        render_template('index.html')
    )
    max_age = 60*60*24*7
        
    if request.method == "POST":
        session['id'] = request.form['id']
        if not session['id']:
            flash('아이디를 입력해야 합니다.')
            return redirect(request.referrer)

        session['passwd'] = request.form['passwd']
        if not session['passwd']:
            flash('비밀번호를 입력해야 합니다.')
            return redirect(request.referrer)
        
        session['content'] = request.form['content']
        return redirect('/show')
    

    response.set_cookie('name', 'Hong Gil-dong', max_age=max_age) # 쿠키 굽기
    response.set_cookie('universtiy', 'Chongju University', max_age=max_age) # 또 다른 쿠키 굽기
    response.set_cookie('passwd', '1234', max_age=60*60*24*7) # 쿠키 유효 기간을 7일로 설정

    return response


@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')
    

@app.route("/show")
def show():
    
    # return f'''
    # <p>로그인에 성공하였습니다.</p>
    # <p>아이디: { session['id'] }</p>
    # <p>비밀번호: { session['passwd'] }</p>
    # <p>인사말: { session['content'] }</p>
    # <a href="/logout">로그아웃</a>
    # '''
    
    # Solution 1. 직접 함수를 만드는 방법
    def js_sanitizer(content: str) -> str:
        '''Java Script 문자열 치환'''
        return content.replace('<', '&lt;').replace('<', '&lt;')
    
    id = js_sanitizer(session['id'])
    passwd = js_sanitizer(session['passwd'])
    content = js_sanitizer(session['content'])
    return f'''
    <p>로그인에 성공하였습니다.</p>
    <p>아이디: {id}</p>
    <p>비밀번호: {passwd }</p>
    <p>인사말: {content}</p>
    <a href="/logout">로그아웃</a>
    '''
    
    # Solution 2. 보안 전문가들이 만든 모듈 사용(플러그인 Approach)
    # Reference: 
    #   1. https://opentutorials.org/module/3357/19936 (생활코딩)
    #   2. Google search -> "python html sanitizer"
    #   3. PyPi -> search "html sanitizer" -> "html-sanitizer1.x.x"
    # pip install html-sanitizer
    from html_sanitizer import Sanitizer
    sanitizer = Sanitizer()
    id = sanitizer.sanitize(session['id'])
    passwd = sanitizer.sanitize(session['passwd'])
    content = sanitizer.sanitize(session['content'])
    return f'''
    <p>로그인에 성공하였습니다.</p>
    <p>아이디: {id}</p>
    <p>비밀번호: {passwd }</p>
    <p>인사말: {content}</p>
    <a href="/logout">로그아웃</a>
    '''  
    
    return f'''
    <p>로그인에 성공하였습니다.</p>
    <p>아이디: {id}</p>
    <p>비밀번호: {passwd }</p>
    <p>인사말: {content}</p>
    <a href="/logout">로그아웃</a>
    '''    
    # Solution 3. 프레임워크에서 지원하는 template 엔진 사용
    # return render_template(
    #     'success.html'
    # ) 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5004', debug=True)