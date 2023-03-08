# 세션 (Session)

세션이란 서버가 자신에게 접근 요청 (request 메시지)를 보낸 클라이언트(사용자)를 구별하는 방법입니다. 

쿠키를 사용할 경우 네트워크 트랙픽이 증가할 수 있고, 보안에 취약하기 때문에 이를 보완하기 위해 세션이 등장하였습니다.

세션은 클라이언트(사용자 브라우저)에 정보를 저장하는 쿠키(cookie)와 다르게 서버에 정보를 저장합니다. 서버에 연결 정보가 저장되기 때문에 쿠키보다 관리가 용이하고 보안 측면에서 강력합니다.

세션은 클라이언트가 서버에 접속해서 브라우저를 종료할 때까지 인증상태를 유지합니다. 물론 세션도 유효 시간을 정할 수 있습니다. 일정 시간 동안 특별한 활동이 없다면 자동 로그아웃 되는 현상은 세션에 유효 시간이 설정되어 있기 때문입니다.

사용자별로 별도의 세션을 유지하기 위해 서버는 개별 클라이언트에게 고유한 번호를 부여하여 관리하게 됩니다. 이 때 발급되는 고유번호가 바로 `세션 아이디(Session ID)` 입니다.

## 세션의 장단점

모든 시스템에는 장단점이 있죠? 

장단점을 정리해 보았습니다.

|순번|구분|내용|
|:--|:--|:--|
|1 <td rowspan="5">장점</td> |서버에 저장하기 때문에 관리가 편리(클라이언트의 환경을 시시콜콜 신경쓰지 않아도 됩니다.)|
|2|어느정도 보안을 유지할 수 있음|
|3|웹 브라우저와 독립적으로 관리할 수 있음|
|4|세션의 저장 개수나 용량에 제약이 없음(서버 용량만 허용하면 모두 가능)|
|5|SessionID만 주고 받기 때문에 네트워크에 거의 부담을 주지 않음|
|6|단점|관리할 세션이 아주 많아지면 서버에 부담이 될 수도 있음|

## 세션과 쿠키 비교

세션은 쿠키와 유사하게 사용자를 구별하기 위해 만들어졌기 때문에 쿠키와 종종 비교하게 됩니다.

|구분|쿠키|세션|
|:--|:--|:--|
|저장위치|사용자 브라우저|서버 내부에 저장|
|보안|보통|우수|
|속도|빠름|보통(서버 처리시간 필요)|
|유효기간|장기간 살아있을 수 있음|시간 설정이 가능하지만 세션이 종료되면 무조건 만료|

여기서 이런 의문이 듭니다. 대부분의 경우 세션이 관리하기도 편하고 보안에도 강하지만 속도 차이가 별로 안 난다면 굳이 쿠키를 왜 쓸까요?

# 세션의 작동 방식

1. 클라이언트는 서버에게 웹사이트를 보여달라고 메시지를 보냅니다. `request` 메시지를 보내는 겁니다.

2. 만약 로그인을 하는 과정이라면 사용자 정보를 기반으로 사용자 DB에서 해당 정보를 찾아옵니다. 일반적이 접속이라면 request 헤더에서 클라이언트를 식별할 수 있는 정보를 활용할 수 있습니다. 로그인하는 경우를 살펴보면 다음과 같습니다.

    <div style="text-align:left">
        <figure>
            <img src="../imgs/session_01_basic_operation_login.png" width="80%">
            <figcaption>Request 접수하여 클라이언트 식별 정보 추출 (이미지 출처: 
            <a href="https://velog.io/@rlfrkdms1/%EC%BF%A0%ED%82%A4%EC%99%80-%EC%84%B8%EC%85%98%EC%9D%98-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC%EC%99%80-%EC%84%B8%EC%85%98%EC%9D%98-%EA%B5%AC%EC%A1%B0">Ddukddaki.log</a>)
            </figcaption>
        </figure>
    </div>

3. 클라이언트를 식별할 수 `sessionId`를 생성하고 `key`, `value` 쌍으로 구성하여 서버의 저장소에 저장합니다. 여기서 `key`는 `sessionID`이고, `value`는 클라이언트를 식별할 수 있는 객체가 됩니다. 만약 로그인 하는 상황이라면 사용자 `field`가 될 수 있습니다. 당연히 `sessionId`는 다른 사람이 `value` 값을 유추하지 못 하도록 만들어야 합니다.

    <div style="text-align:left">
        <figure>
            <img src="../imgs/session_02_basic_operation_gen_sessionId.png" width="80%">
            <figcaption>sessionId 생성하고 서버에 저장 (이미지 출처: 
            <a href="https://velog.io/@rlfrkdms1/%EC%BF%A0%ED%82%A4%EC%99%80-%EC%84%B8%EC%85%98%EC%9D%98-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC%EC%99%80-%EC%84%B8%EC%85%98%EC%9D%98-%EA%B5%AC%EC%A1%B0">Ddukddaki.log</a>)
            </figcaption>
        </figure>
    </div>

4. 서버는  response-header field인 `set-cookie` 값으로 `sessionId` 정보만 쿠키에 담아서 클라이언트에게 보냅니다. 클라이언트는 `sessionId`를 브라우저에 저장합니다. 이때 클라이언트에 저장되는 `sessionId` 값은 세션이 종료되면(브라우저를 닫으면) 같이 소멸되는 값입니다. 이를 `Memory cookie`라고 부릅니다. 일반적인 쿠키와는 좀 다릅니다.

    <div style="text-align:left">
        <figure>
            <img src="../imgs/session_03_basic_operation_send_sessionId.png" width="80%">
            <figcaption>sessionID를 클라이언트에게 전송 (이미지 출처: 
            <a href="https://velog.io/@rlfrkdms1/%EC%BF%A0%ED%82%A4%EC%99%80-%EC%84%B8%EC%85%98%EC%9D%98-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC%EC%99%80-%EC%84%B8%EC%85%98%EC%9D%98-%EA%B5%AC%EC%A1%B0">Ddukddaki.log</a>)
            </figcaption>
        </figure>
    </div>
    
    - 클라이언트(브라우저)에 저장된 `sessionId` 값은 개발자도구 -> 네트워크 -> All 에서 확인할 수 있습니다.

    <div style="text-align:left">
        <figure>
            <img src="../imgs/session_04_check_sessionId_in_browser.png" width="80%">
            <figcaption>개발자도구를 이용한 sessionID 확인</figcaption>
        </figure>
    </div>

    - 일반적으로 서버가 `set-cookie`로 설정해서 쿠키를 보내면 기본값으로 `HttpOnly` 옵션이 설정됩니다. 정확하게는 다음과 같이 세팅이 되어 클라이언트(브라우저)에게 보냅니다.
        ```{bash}
        Set-Cookie: <cookie-name>=<cookie-value>; HttpOnly
        ```
    - `HttpOnly`이 설정되면 자바스크립트를 통해 세션 쿠키값에 접근하는 것을 차단합니다. 우리들은 볼 수 없고, 브라우저만 알고 있다는 의미입니다. 이렇게 설정하는 이유는 cross-site scripting ([XSS](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting)) 공격의 위험을 감소시키기 위함입니다. XSS 공격은 나중에 배울 예정입니다.
    
    <div style="text-align:left">
        <figure>
            <img src="../imgs/session_06_session_cookie_warning.png" width="80%">
            <figcaption>set-cookie 옵션 사용에 대한 경고</figcaption>
        </figure>
    </div>    
    

4. 서버에서는 HTTP Request를 통해 쿠키에서 Session id를 확인을 한 후에 없으면 Set-Cookie를 통해 새로 발행한 Session-id 보냅니다. 

5. 클라이언트는 HTTP Request 헤더에 Session id를 포함하여 원하는 Resource를 요청을 합니다.

    <div style="text-align:left">
        <figure>
            <img src="../imgs/session_05_send_sessionId_to_server.png" width="80%">
            <figcaption>클라이언트는 자신의 sessionID 서버에 전송 (이미지 출처: 
            <a href="https://velog.io/@rlfrkdms1/%EC%BF%A0%ED%82%A4%EC%99%80-%EC%84%B8%EC%85%98%EC%9D%98-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC%EC%99%80-%EC%84%B8%EC%85%98%EC%9D%98-%EA%B5%AC%EC%A1%B0">Ddukddaki.log</a>)
            </figcaption>
        </figure>
    </div>

6. 서버는 Session id를 통해 해당 세션을 찾아 클라이언트 상태 정보를 유지하며 적절한 응답을 합니다.


# 세션 실습




# References
|Title|Author|Source|Link|
|:--|:--|:--|:--|
|Session, HttpSession 인터페이스, 쿠키|dmchoi.log|개인 블로그|[link](https://velog.io/@dmchoi224/Session-HttpSession-%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4.-%EC%BF%A0%ED%82%A4)|
|쿠키와 세션 개념|RyanGomdoriPooh|개인 블로그|[link](https://interconnection.tistory.com/74)|
|Set-Cookie|Mdn web docs|MDN 공식문서|[link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)|
|Set-Cookie|Mdn web docs|MDN 공식문서|[link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)|
|How to use Flask-Session in Python Flask?|GeeksforGeeks|블로그(외국)|[link](https://www.geeksforgeeks.org/how-to-use-flask-session-in-python-flask/)|