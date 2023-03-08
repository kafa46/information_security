# HTTP 개념

하이퍼텍스트 전송 프로토콜(HTTP, Hyper Text Transmission Protocol)은 HTML과 같은 하이퍼미디어 문서를 전송하기 위한 애플리케이션 레이어 프로토콜입니다. 

웹 브라우저와 웹 서버간의 통신을 위해 설계되었지만 다른 목적으로도 사용할 수 있습니다. 

HTTP는 클라이언트가 요청을 하기 위해 연결을 연 다음 응답을 받을때 까지 대기하는 전통적인 `클라이언트-서버 모델`을 따릅니다. HTTP는 `무상태` 프로토콜이며, 서버가 두 요청 간에 어떠한 데이터(상태)도 유지하지 않습니다.

`무상태(Stateless)`는 서버가 사용자의 상태를 기억하지 않는다는 의미입니다. 

반대 개념으로 `Stateful` 이라는 개념도 있습니다. 

Stateless와 Stateful은 모두 서버-클라이언트 사이에서 발생하는 통신을 어떻게 처리할 것인가에 대한 통신 프로토콜 개념입니다.

먼저 Stateful부터 살펴보도록 하겠습니다.

대표적인 Stateful 프로토콜로써 `TCP(Transmission Control Protocol)`가 있습니다. TCP는 3-way handshake를 기반으로 서버와 클라이언트가 통신하는 방법입니다. 대표적인 예로써 인터넷 뱅킹을 들 수 있습니다. 은행은 사용자의 연결(session) 상태와 연결 정보(결재 내역 등)을 기억하고, 이 정보를 기반으로 서비스를 하게 됩니다.

Stateful 통신은 갑자기 통신이 중단되더라도 중단된 시점부터 서비스를 다시 시작할 수 있는 장점이 있습니다. 하지만, 시스템을 확장하려는 경우 이전 확장된 시스템에서는 이전 정보를 가지고 있지 않기 때문에 사용자의 이전 정보를 새로운 서버에 옮기는 작업이 필요합니다. 그만큼 확장성 면에서 좋지 않습니다.

Stateful 예를 들어 살펴볼까요?

여러분이 `CJU 학사관리 시스템`(이하 시스템이라고 간단히 부르겠습니다)에 접속하여 수강 신청한다고 가정해 보겠습니다. 여러분을 사용자라고 부르도록 하겠습니다.

1. 사용자: 서버 접속하여 연결 성공 (session 연결)
2. 시스템: 메뉴를 선택해 주세요
3. 사용자: 수강신청 선택 $\to$ `수강신청 하려는 것을 기억`
4. 시스템: 수강할 수 있는 과목을 시현
5. 사용자: 컴퓨터보안 수업 신청 $\to$ `컴퓨터보안 선택했다는 것을 기억`
6. 시스템: 대면수업과 온라인 수업 중 선택해 주세요.
7. 사용자: 온라인 선택 $\to$ `온라인 과목을 선호한다는 것을 기억`
8. 시스템: 수업 교재 정보를 확인하시겠습니까?
9. 사용자: 넵 $\to$  `교재 정보를 확인하려 했다는 것을 기억`
10. 시스템: 종이책 또는 전자책 중에서 자유롭게 선택할 수 있습니다.
11. 사용자: 전자책이 좋을 것 같아요 $\to$  `전자책을 선호한다는 것을 기억`

여기까지 보면 아주 자연스럽습니다. 

만약 다음에 동일한 사용자가 접속했을 경우 현재 정보를 기억하고 있다면 맞춤형 서비스를 제공할 수 있습니다. 

1. 사용자: 서버 접속하여 연결 성공 (session 연결)
2. 시스템: 컴퓨터조안 수업을 온라인으로 신청하셨네요. 교재는 전자책을 선호하시네요^^. 해당 사항을 수강 장바구니에 저장할까요?

하지만 수강신청이 집중되어 시스템 서버를 증설했을 경우는 어떨까요? 여러분은 동일한 주소로 접속한다고 해도 새로운 서버로 연결되 수 있습니다. Statefule 프로토콜을 사용한다면 아마도 다음과 같은 상황이 벌어질 겁니다.

1. 사용자: 서버 접속하여 연결 성공 (session 연결)
2. 시스템: 메뉴를 선택해 주세요
3. 사용자: 컴퓨터보안 수업을 신청할게요.
4. 시스템: 뭐라고요?
5. 사용자: 대면수업으로 변경할게요.
6. 시스템: 뭐라고요?
7. 사용자: 교재는 전자책을 사용할 거예요.
8. 시스템: 뭐라고요?

Stateful 프로토콜을 이용하던 사용자는 평소와는 다른 서비스를 받게 될 것입니다.

이러한 단점을 보완하는 것이 Stateless 통신입니다. 

1. 사용자: 서버 접속하여 연결 성공 (session 연결)
2. 시스템: 메뉴를 선택해 주세요
3. 사용자: 수강신청 선택 $\to$ `정보를 기억하지 않음`
4. 시스템: 수강할 수 있는 과목을 시현
5. 사용자: 컴퓨터보안 수업 신청 $\to$ `정보를 기억하지 않음`
6. 시스템: 대면수업과 온라인 수업 중 선택해 주세요.
7. 사용자: 온라인 선택 $\to$ `정보를 기억하지 않음`
8. 시스템: 수업 교재 정보를 확인하시겠습니까?
9. 사용자: 넵 $\to$  `정보를 기억하지 않음`
10. 시스템: 종이책 또는 전자책 중에서 자유롭게 선택할 수 있습니다.
11. 사용자: 전자책이 좋을 것 같아요 $\to$  `정보를 기억하지 않음`
12. 시스템: 수강 장바구니에 저장할까요?

Stateless는 사용자의 상태를 아무것도 기억하지 않는다는 특징이 있습니다. HTTP가 바로 Stateful 방식을 사용하고 있습니다.

# HTTP 구성

클라이언트와 서버들은 (데이터 스트림과 대조적으로) 개별적인 메시지 교환에 의해 통신합니다. 


<div style="text-align:center">
    <figure>
        <img src="https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview/fetching_a_page.png" style="align center" width="50%">
        <figcaption>HTTP 연결 구조</figcaption>
    </figure>
</div>

HTTP에서 클라이언트라고 하면 대부분의 경우 여러분이 인터넷 웹사이트를 방문하기 위해 사용하는 브라우저를 의미합니다. 

서버는 방문하려는 웹사이트의 내용을 제공하는 컴퓨터라고 볼 수 있습니다. 네이버를 방문하기 위해서 브라우저 주소창에 www.naver.com 이라고 입력하면 네이버 화면을 볼 수 있습니다. 이 화면을 제공하는 컴퓨터가 바로 서버가 됩니다. 

브라우저에 의해 전송되는 메시지를 요청(requests)이라고 부르며, 그에 대해 서버에서 응답으로 전송되는 메시지를 응답(responses)이라고 부릅니다.

클라이언트의 구조는 다음과 같습니다.

<div style="text-align:center">
    <figure>
        <img src="https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview/http-layers.png" style="align center" width="50%">
        <figcaption>HTTP 연결 구조</figcaption>
    </figure>
</div>

위 그림에서와 같이 HTTP를 이용하는 클라이언트는 HTML, CSS, JavaScript, Web APIs 구성되어 있습니다. 우리는 컴퓨터 보안에 관심이 있으므로 클라이언트를 구성하는 개별 기술에 대해 깊이 살펴보지는 않을 것입니다. 관심있는 독자라면 관련 서적이나 웹사이트 튜토리얼을 참고하여 학습하시기 바랍니다.


# HTTP 메시지

HTTP 메시지는 서버와 클라이언트 간에 데이터가 교환되는 방식입니다. 

메시지 타입은 두 가지가 있습니다. 
- 요청(request): 클라이언트가 서버로 전달해서 서버의 액션이 일어나게 하는 메시지
- 응답(response): 요청에 대한 서버의 답변 메시지

HTTP 메시지는 ASCII로 인코딩된 텍스트 정보이며 여러 줄로 되어 있습니다. 다시 말하면 여러 줄(line)로 구성된 글자라는 의미입니다. 

HTTP 프로토콜 초기 버전과 HTTP/1.1에서는 클라이언트와 서버 사이의 연결을 통해 공개적으로 전달되었습니다. 누구든지 메시지를 볼 수 있었다는 의미입니다. 한 때 사람이 읽을 수 있었던 메시지는 HTTP/2에서는 최적화와 성능향상을 위해 모든 메시지를 바이너리 프레임으로 나누고 캡슐화하여 전송합니다. HTTP/2에 대한 보다 자세한 내용은 wiostz98kr님의 블로그 [HTTP1.1과 HTTP2.0의 차이](https://velog.io/@wiostz98kr/HTTP1.1%EA%B3%BC-HTTP2.0%EC%9D%98-%EC%B0%A8%EC%9D%B4-e2v4x4t1)를 참고하기 바랍니다.

개발자가 직접 HTTP 메시지를 작성하는 일은 거의 없습니다. 사용자들이 이용하는 브라우저나 웹 서버가 자동으로 작성해 줍니다. 

하지만 기본적인 HTTP 구조는 알고 있어야 겠죠?

HTTP 메시지는 다음과 같은 규칙을 가지고 작성합니다.

1. 시작 줄(start-line)에는 실행되어야 할 요청, 또는 요청 수행에 대한 성공 또는 실패가 기록되어 있습니다. 이 줄은 항상 한 줄로 끝납니다.
2. 옵션으로 HTTP 헤더 세트가 들어갑니다. 여기에는 요청에 대한 설명, 혹은 메시지 본문에 대한 설명이 들어갑니다.
3. 요청에 대한 모든 메타(헤더) 정보가 전송되었음을 알리는 빈 줄(blank line)이 삽입됩니다.
4. 요청과 관련된 내용(HTML 폼 콘텐츠 등)이 옵션으로 들어가거나, 응답과 관련된 문서(document)가 들어갑니다. 본문의 존재 유무 및 크기는 첫 줄과 HTTP 헤더에 명시됩니다.

<div style="text-align:center">
    <figure>
        <img src="https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages/httpmsgstructure2.png" style="align center" width="80%">
        <figcaption>HTTP 연결 구조</figcaption>
    </figure>
</div>

## HTTP Request
HTTP Request는 서버가 어떤 동작을 하도록 클라이언트에서 전송하는 메시지입니다.

Request 메시지를 구성하는 것은 크게 시작줄(start line), 헤더(header), 본문(body)로 구성됩니다.
각각의 요소에 대해 살펴보도록 하겠습니다.

### 시작 줄(start line): 3가지 요소로 구성
   1. HTTP 메서드: 영어 동사(GET, PUT,POST) 혹은 명사(HEAD, OPTIONS)를 사용해 서버가 수행해야 할 동작을 나타냅니다. 예를 들어, GET은 리소스를 클라이언트로 가져다 달라는 이미로, POST는 데이터가 서버로 들어갸야 한다는 의미로 사용합니다.
   2. 요청(Host) 타겟: 서버의 주소를 적습니다. 주로 URL, 또는 프로토콜, 포트, 도메인의 절대 경로를 기록합니다.
   3. HTTP 버전: 클라이언트가 사용하는 버전에 따라 구조가 메시지 구조가 달라질 수 있기 때문에 서버에게 클라이언트의 버전을 알려줘야 합니다.
   - 시작 줄의 몇 가지 예를 들면 다음과 같습니다.
     - `POST / HTTP/1.1`
     - `GET /background.png HTTP/1.0`
     - `HEAD /test.html?query=alibaba HTTP/1.1`
     - `OPTIONS /anypage.html HTTP/1.0`
     - `GET https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages HTTP/1.1`
     - 

### Request 헤더

요청에 들어가는 HTTP 헤더는 HTTP 헤더의 기본 구조를 따릅니다. 대소문자 구분없는 문자열 다음에 콜론('`:`')이 붙으며, 그 뒤에 오는 값은 헤더에 따라 달라집니다. 헤더는 값까지 포함해 한 줄로 구성되지만 꽤 길어질 수 있습니다. 

HTTP 헤더는 클라이언트와 서버가 요청 또는 응답으로 부가적인 정보를 전송할 수 있도록 해줍니다. HTTP 헤더는 대소문자를 구분하지 않는 이름과 콜론 ':' 다음에 오는 값(줄 바꿈 없이)으로 이루어져있습니다. 값 앞에 붙은 빈 문자열은 무시됩니다.

Request 헤더는 크게 3가지로 분류할 수 있습니다.

- General 헤더: Request 메시지 전체에 공통적으로 적용할 내용을 기록합니다.
- Request 헤더: `User-Agent`와 `Accept`와 같이 Request 메시지 내용을 구체화 하거나, `Accept-Language`와 같이 클라이언트 언어를 구체화하거나, `Referer`와 같이 클라이언트의 주소를 제공하거나, `If-None`와 같이 조건에 따른 요청 내용을 기록합니다.
- Representation 헤더: `Content-Type`와 같이 메시지에 담긴 데이터의 양식을 정의하거나 본문에 사용할 인코딩 방법을 기록합니다.

<div style="text-align:center">
    <figure>
        <img src="https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages/http_request_headers3.png" style="align center" width="80%">
        <figcaption>HTTP 요청(Request) 메시지</figcaption>
    </figure>
</div>


### Request 본문

Request 메시의 헤더 부분에서 빈 줄(empty line) 다음에 기록되는 내용입니다. Request 메시지의 본문(body)입니다. 

일반적으로 `GET`, `HEAD`, `DELETE`, `OPTIONS`처럼 리소스를 가져오는 요청은 보통 본문을 작성하지 않습니다. 

하지만 일부 Request에서는 업데이트를 하기 위해 데이터를 전송합니다. HTML의 `form`에 담아서 요청하는 경우가 많은데 주로 `POST` 요청일 경우가 많습니다.

## HTTP Response
HTTP Response는 클라이언트 요청에 따라 서버가 어떤 동작을 수행한 결과를 클라이언트로 전송하는 메시지입니다.

Response 메시지를 구성하는 것은 크게 상태줄(status line), 헤더(header), 본문(body)로 구성됩니다.

각각의 요소에 대해 살펴보도록 하겠습니다.

### 상태 줄(Status Line)

HTTP 응답의 시작 줄은 `상태 줄(status line)` 이라고 부르며, 다음과 같은 3가지 정보를 가지고 있습니다.

간단히 살펴볼까요?

1. 프로토콜 버전: 통신에 사용되는 프로토콜 이름과 버전을 기록합니다. 일반적으로 `HTTP/1.1` 입니다.
2. 상태 코드: Request에 대한 성공 여부를 기록합니다. 일반적으로 `200`, `404`, `302` 입니다.
3. 상태 텍스트: 사용자들이 HTTP 메시지를 이해할 수 있도록 간단하게 상태 코드에 대한 설명을 기록합니다. 

시작 줄의 몇 가지 예를 들면 다음과 같습니다.
- `HTTP/1.1 200 OK.`
- `HTTP/1.1 404 Not Found.`
- `HTTP/1.1 302 Temporary Moved.`

### Response 헤더

Response 메시지에 들어가는 HTTP 헤더는 Request 헤더와 비슷한 구조입니다. 

대소문자를 구분하지 않는 문자열 다음에 콜론(':')이 오며, 그 뒤에 오는 값은 구조가 헤더에 따라 달라집니다. 헤더는 값을 포함해 전체를 한 줄로 표시합니다.

다양한 종류의 Response 헤더가 있지만 일반적으로 3가지로 분류할 수 있습니다.
- General 헤더: Response 메시지 전체에 공통적으로 적용할 내용을 기록합니다.
- Response 헤더: `Vary`, `Accept-Ranges`와 같이 상태 줄에 포함하지 못했던 서버의 추가 정보를 기록합니다.
- Representation 헤더: `Content-Type`과 같이 Request 메시지 본문의 포맷이나 인코딩에 사용했던 정보를 기록합니다.

<div style="text-align:center">
    <figure>
        <img src="https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages/http_response_headers3.png" style="align center" width="80%">
        <figcaption>HTTP 요청(Request) 메시지</figcaption>
    </figure>
</div>

헤더의 자세한 목록을 살펴보려면 IANA((Internet Assigned Numbers Authority)에서 제공하는 [메시지 헤더 레지스트리](https://www.iana.org/assignments/message-headers/message-headers.xhtml) 목록을 찾아보면 됩니다.

### Response 본문

Response 메시의 헤더 부분에서 빈 줄(empty line) 다음에 기록되는 내용입니다. Response 메시지의 본문(body)입니다. 

상태코드 `200 Created`, `204 No Content`를 보내는 경우에는 본문을 보내지 않기도 합니다.

본문은 일반적으로 3 종류로 구분할 수 있습니다.

- Response 헤더의 `Content-Type`와 `Content-Length`에 의해 단일 파일의 길이가 알려진 단일 파일 리소스 본문
- Response 헤더의 `Transfer-Encoding`이 `chuncked`로 설정되어 단일 파일을 덩어리로 나누어 전송하는 길이를 모르는 단일 파일로 구성된 단일 리소스 본문
- 서로 다른 정보를 담고 있는 멀티 파트로 구성된 다중 리소스 본문

# 실습

여러분이 사용하는 브라우저를 통해 쉽게 Request/Response 메시지를 확인할 수 있습니다.

## 클라이언트 브라우저 이용
크롬의 경우 `메뉴` $\to$ `개발자 도구` $\to$ `네트워크 메뉴`를 이용하여 쉽게 확인할 수 있습니다.

## 프로그래밍 활용
프로그래밍을 이용할 경우 Python `requests` 모듈을 이용하면 편리하게 확인할 수 있습니다.
- 가상환경 구축(생략) $\to$ 가상환경에서 실습할 것을 `강력히 권고`드립니다.
- `requests` 모듈 설치
    ```{python}
    pip install requests
    ```

- 모듈 임포트
    ```{python}
    import requests
    ```

- Request 보내기
    ```{python}
    response =  requests.get('https://www.naver.com')
    ```

- 상태코드 확인하기
    ```{python}
    response.status_code

    # 상태 코드에 따른 처리
    if response:
        print('Success!')
    else:
        print('An error has occurred.')
    ```

- Response 헤더 확인하기
    ```{python}
    response.headers
    ```
 

- Response 본문(body) 확인하기
    ```{python}
    # 바이너리 데이터 확인
    response.content

    # 텍스트로 변환된 데이터 확인
    response.text

    # 텍스트 인코딩 지정하고 데이터 확인
    response.encoding = 'utf-8'
    response.text
    ```

- Json 형태로 받은 데이터를 사전 형태로 받아오기
    ```{python}
    # 참고 사이트: https://m.stock.naver.com/
    response =  requests.get('https://polling.finance.naver.com/api/realtime/worldstock/futures/YMcv1%2CNQcv1')

    # Json 데이터 확인
    response.json()

    # 자료구조 확인
    type(response.json())
    ```

- Query string 적용하기: `params` 파라미터의 인자로 전달
    ```{python}
    # Github 저장소(repository) 검색 (참고 -> https://github.com)
    # 참고 블로그: https://realpython.com/python-requests/
    
    response = requests.get(
        'https://api.github.com/search/repositories',
        
        # Query string을 사전형태로 보낼 수 있음
        params={'q': 'requests+language:python'},
        
        # Query string을 튜플을 저장한 리스트로 보낼 수도 있음
        # params=[('q', 'requests+language:python')],
        
        # Query string을 byte 자료형으로 보낼 수도 있음
        # params=b'q=requests+language:python',
    )

    # Inspect some attributes of the `requests` repository
    json_response = response.json()
    repository = json_response['items'][0]
    print(f'Repository name: {repository["name"]}')
    print(f'Repository description: {repository["description"]}')
    ```

- Request 헤더를 추가: `headers` 파라미터의 인자로 전달
    ```{python}
    # 참고 사이트: "https://www.cju.ac.kr/site/search/search.jsp?query=기숙사"
    response = requests.get(
        'https://www.cju.ac.kr/site/search/search.jsp',
        params={'query': '기숙사'},
        headers={
            'Sender': 'Professor',
            'Org': 'CJU computer security',
        },
    )
    # Response를 통해 내가 보낸 헤더 확인하기
    print(response.request.headers)
    print(response.request.headers['Sender'])
    ```

- Request 메시지 본문 보내기: `POST` 방식, `data` 파라미터의 인자로 보냄
  ```{python}
  # 사전 형태로 보내기
  response = requests.post('https://www.cju.ac.kr', data={'name':'Hong Gildong'})

  # 튜플의 리스트 형태로 보내는 것도 가능
  # response = requests.post('https://www.cju.ac.kr', data=[('name', 'Hong Gildong')])
  
  # Response를 통해 내가 보낸 본문(body) 확인하기
  response = requests.post('https://httpbin.org/post', json={'name':'Hong Gildong'})
  print(response.request.url)
  print(response.request.body)
  ```

- 다양한 방식으로 보내기
    ```{python}
    requests.post('https://httpbin.org/post', data={'name':'value'})
    requests.put('https://httpbin.org/put', data={'key':'value'})
    requests.delete('https://httpbin.org/delete')
    requests.head('https://httpbin.org/get')
    requests.patch('https://httpbin.org/patch', data={'key':'value'})
    requests.options('https://httpbin.org/get')
    ```

# References
|Title|Author|Source|Link|
|:--|:--|:--|:--|
|[주요 개념] Stateful 과 Stateless|운호[Noah]|블로그|[link](https://wooono.tistory.com/366)|
|HTTP|HTTP 자습서|MDNB web docs|[link](https://developer.mozilla.org/ko/docs/Web/HTTP)|
|HTTP 메시지|HTTP 자습서|MDNB web docs|[link](https://developer.mozilla.org/ko/docs/We)|
|HTTP 헤더|HTTP 자습서|MDNB web docs|[link](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers)|
|HTTP1.1과 HTTP2.0의 차이|wiostz98kr|블로그|[link](https://velog.io/@wiostz98kr/HTTP1.1%EA%B3%BC-HTTP2.0%EC%9D%98-%EC%B0%A8%EC%9D%B4-e2v4x4t1)|
|Python’s Requests Library (Guide)|Alex Ronquillo|Real Python|[link](https://realpython.com/python-requests/)|
