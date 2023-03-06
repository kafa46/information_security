# 쿠키 (Cookie)

## 개념

쿠키(HTTP cookie)란 하이퍼 텍스트의 기록서(HTTP)의 일종으로서 인터넷 사용자가 어떠한 웹사이트를 방문할 경우 사용자의 웹 브라우저를 통해 인터넷 사용자의 컴퓨터나 다른 기기에 설치되는 `작은 기록 정보 파일`을 의미합니다. 쿠키, 웹 쿠키, 브라우저 쿠키라고도 부르기도 합니다 (자료출처: [Design ＆ Implementation of License-based Digital Rights Management System](10.3745/kipstc.2004.11c.1.055)). 

<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Cookie_stack.jpg/1920px-Cookie_stack.jpg' width="50%" textalign="center">

쿠키 파일에 담긴 정보는 인터넷 사용자가 같은 웹사이트를 방문할 때마다 읽히고 수시로 새로운 정보로 바뀐다. 이 수단은 넷스케이프의 프로그램 개발자였던 루 몬툴리(Lou Montulli)가 고안한 뒤로 오늘날 많은 서버 및 웹사이트들이 브라우저의 신속성을 많이 사용하고 있습니다 (자료출처: [Giving the Web a Memory Cost Its Users Privacy](https://www.semanticscholar.org/paper/Giving-the-Web-a-Memory-Cost-Its-Users-Privacy-Schwartz/77c388be3f57c80889e5291dc103f8f375718f56)).

## `쿠키`, 이름의 유래

"쿠키"라는 용어는 웹 브라우저 프로그래머 루 몬툴리가 만들었습니다. 쿠키는 유닉스 프로그래머들이 사용한, 프로그램이 수신 후 변경하지 않은 채로 반환하는 데이터의 패킷을 의미하는 `매직 쿠키`라는 용어에서 비롯되었습니다. (자료출처: [Where cookie comes from](http://dominopower.com/article/where-cookie-comes-from/))

[루 몬툴리](https://en.wikipedia.org/wiki/Lou_Montulli) 라는 컴퓨터 프로그래머가 웹 통신에서 쿠키를 사용하려는 아이디어를 갖게 된 1994년에 이미 `매직 쿠키`라는 개념은 사용되고 있었습니다.

당시 넷스케이프 케뮤니케이션사의 직원이었던 몬툴리는 [MCI](https://en.wikipedia.org/wiki/MCI_Inc.)사의 전자상거래 애플리케이션을 개발하고 있었습니다.

MCI사의 기술 대표인 [빈 서프(Vint Cerf)](https://en.wikipedia.org/wiki/Vint_Cerf)와 [존 클렌신(John Klensin)](https://en.wikipedia.org/wiki/John_Klensin)은 넷스케이프사와 회의를 하고 있었습니다. 그 회의에서 MCI사 서프와 클렌신은 거래 상태 정보를 서버에 남기고 싶어하지 않았고, 거래 상태 정보를 사용자의 개인 컴퓨터에 남길수 있는 방법을 넷스케이프사에 요청하였습니다. 이런 MCI사의 요청으로 신뢰성 있는 온라인 쇼핑 카트를 구현할 수 있는 해결책으로 `쿠키`라는 것이 제시되었습니다.

그 즈음에 넷스케이프의 [루 몬툴리](https://en.wikipedia.org/wiki/Lou_Montulli)와 [존 지안드레아(John Giannandrea)](https://en.wikipedia.org/wiki/John_Giannandrea) 1994년 10월에 출시된 [베타 버전의 Mosaic Netscape](https://en.wikipedia.org/wiki/Netscape_Navigator) 라는 브라우저에서 사용할 네스케이프 쿠키 스펙을 작성하였습니다.

쿠키를 처음 사용한 것은 넷스케이프 웹사이트를 방문하는 사용자들이 사이트를 이전에 방문했었는지를 확인(check)하는 것이었습니다.

몬툴리는 1995년에 쿠키 기술에 대한 특허를 출원하였고 1998년에 특허를 승인(등록) 받았습니다.

1998년 특허가 승인되자 쿠키 기술은 1995년에 출시된 인터넷 [익스플로러 버전 2](https://en.wikipedia.org/wiki/Internet_Explorer_2)에 추가되었습니다.

쿠키 기술은 처음에는 잘 알려지지 않았습니다. 특히 인터넷 기술에 기본적으로 채용되었지만 사용자들은 자신들이 쿠키를 사용하고 있는지도 모르고 있었습니다. 

일반 사용자들은 쿠키의 존재를 [파이낸셜 타임즈](https://en.wikipedia.org/wiki/Financial_Times)가 1996년 2월에 쿠키 관련 기사를 발표하면서 본격적으로 알려지게 되었습니다.

이후 쿠키는 언론의 뜨거운 관심을 받는 기술이 되었으며, 특히 개인 정보에서 문제의 소지가 있다는 것이 알려지게 되었습니다.

쿠키 기술에 대한 스펙은 1995년 `Internet Engineering Task Force` [(IETF)](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)에서 이미 논의되고 있었습니다. 그 당시 2가지 기술이 각각 IETF에 제안되었습니다.

- `오픈소스 스프트웨어 운동`([open source software movement](https://en.wikipedia.org/wiki/Open-source-software_movement)) 진영의 브라이언 벨렌도르프[(Brian Behlendorf)](https://en.wikipedia.org/wiki/Brian_Behlendorf)가 제안한 쿠키 기술

<div style="text-align:center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Brian_Behlendorf_at_INTEROP.jpg/220px-Brian_Behlendorf_at_INTEROP.jpg" width="50%">
</div>

-  New Jersey Institute of Technology (NJIT) 대학의 명예교수였던 데이비드 크리스톨[(David Kristo)](https://en.wikipedia.org/wiki/David_Kristol)이 제안한 쿠키 기술
<div style="text-align:center">
    <img src="../imgs/David_Kristol.jpg" width="50%" style>
</div>

하지만 `데이비드 크리스톨`과 `루 몬툴리`가 지휘하던 IETF는 곧바로 자신들이 제안한 넷스케이프의 쿠키 기술을 쿠키 초기 기술로 채택하게 됩니다.

IETF의 Working Group은 1996년에 제3자에 의해 제공되는 쿠키 기술이 개인정보 침해의 잠재적 위험성이 있다는 것을 식별해 냅니다.

IETF는 1997년 제3자 쿠키를 허용하지 않거나 최소한 기본 설정으로 지원하는 것을 금지하는 내용이 담긴 기술표준 [RFC 2109](https://www.ietf.org/rfc/rfc2109.txt)를 발표합니다. 

`제3자 쿠키`란 주로 광고 플랫폼(애드 테크) 회사들이 여러 사이트에 걸쳐 일어나는 사용자의 행동 데이터를 수집하고 광고 타겟팅에 사용하기 위해 추가하는 쿠키로 제3자 쿠키, 서드파티 쿠키, 3사 쿠키 등으로 불리기도 합니다(출처: [서드파티 쿠키 종말을 대비하는 10가지 방법](https://www.digiocean.co.kr/p/blog?p=cookieless-world-10-ways)). 즉 제3자 쿠키는 방문한 웹사이트가 아닌 다른 웹사이트에서 발행한 쿠키를 의미합니다(출처: [쿠키 그리고 서드파티 쿠키란 무엇일까 (Cookie) - RS Team](https://blog.rs-team.com/12)). 방문한 웹사이트에서 발행한 쿠키는 `퍼스트 파티 쿠키`(First-party Cookie)라고 부릅니다.

제3자 쿠키는 각기 다른 도메인으로 이루어진 사이트의 사용내역에 대한 정보를 쿠키로부터 가져와 활용할 수 있기 때문에 사용자의 온라인상 행동을 추적 및 데이터를 분석하여 광고 등에 사용할 수 있습니다. 웹사이트 운영자에게는 매력적이지만 개인에게는 소중한 개인정보가 유출되는 심각한 상황에 이를 수 있습니다.

[RFC 2109](https://www.ietf.org/rfc/rfc2109.txt)가 발표될 당시에는 이미 많은 광고 회사들이 이미 제3자 쿠키를 사용하고 있었기 때문에 넷스케이프와 익스플로러 이용자들에게 적용될 수 없었으며 2000년 10월에 [RFC 2965](https://www.ietf.org/rfc/rfc2965.txt) 표준으로 대체되기에 이릅니다.

[RFC 2965](https://www.ietf.org/rfc/rfc2965.txt)에서는 HTTP 헤더에 `Set-Cookie2`를 설정하는 방법을 추가하였습니다(비공식적으로는 "`RFC 2965 style 쿠키`"라고 부릅니다). 

하지만 `Set-Cookie2` 방식 역시 개발자들에게 외면 받게 되고 결국 2011년 4월에 [RFC-6265](https://datatracker.ietf.org/doc/rfc6265/) 표준으로 대체됩니다.

<iframe src="https://datatracker.ietf.org/doc/rfc6265/" width="50%"></iframe>

결국 1994년 시작된 쿠키는 [RFC-6265](https://datatracker.ietf.org/doc/rfc6265/) 표준에 이르러 안정을 찾게 되고, 현재 우리가 사용하고 있는 쿠키는 모두 [RFC-6265](https://datatracker.ietf.org/doc/rfc6265/) 표준을 따르고 있습니다.


## Cookie 용도

그렇다면 왜 쿠키를 사용하는 걸까요?

쿠키는 주로 3가지 목적을 위해 사용합니다.

- 세션 관리(Session Management): 서버에 저장해야 할 로그인, 장바구니, 게임 사용자 정보 등을 저장하여 세션 관리를 편하게 하려고 사용합니다.
- 개인화(Personalize): 웹 사용자의 선호도를 관리하고 개인 취향에 맞는 테마 등과 같은 사용자 맞춤형 환경을 제공하기 위해 사용합니다.
- 트래킹(Tracking): 웹 사용자의 사용 패턴을 추적, 기록, 분석하기 위해 사용합니다.

쿠키는 여러모로 웹사이트 운영자와 사용자들에게 편리함을 줍니다. 하지만, 그에 따른 부작용도 항상 존재합니다.

예전에는 쿠키를 항상 사용자의 웹 브라우저에 저장하였지만, 최근에는 [웹 스토리지 API](https://developer.mozilla.org/ko/docs/Web/API/Web_Storage_API) 기술을 이용하여 세션이 연결되었을 경우에만 쿠키를 사용하는 `sessionStorage`와 옛날과 같이 사용자 웹 브라우저에 저장하는 `localStorage` 기술을 모두 사용할 수 있게 되었습니다.


# Cookie 실습
## 브라우저에서 쿠키 확인하기
웹 브라우저를 이용하면 쉽게 쿠키를 확인할 수 있습니다. 

우리는 크롬 브라우저를 이용해 


## 쿠키 만들기






# References

|Title|Author|Source|Link|
|:--|:--|:--|:--|
|RFC 2965| Barth|IETF|[link](https://datatracker.ietf.org/doc/rfc6265/)|
|서드파티 쿠키 종말을 대비하는 10가지 방법|DIGOCEAN|블로그|[link](https://www.digiocean.co.kr/p/blog?p=cookieless-world-10-ways)|
|쿠키 그리고 서드파티 쿠키란 무엇일까(Cookie)|RS Team 하승범|블로그|[link](https://blog.rs-team.com/12)|
|HTTP 쿠키|MDN|MDN Web Docs|[link](https://developer.mozilla.org/ko/docs/Web/HTTP/Cookies)|
|Flask Cookies – Setting Cookies on Web Applications|Vinayak Nishant|AskPython|[link](https://www.askpython.com/python-modules/flask/flask-cookies)|
|Flask Cookies|Not appeared|JavaTpoint|[link](https://www.javatpoint.com/flask-cookies)|