# REST API

## HTTP(Hyper Text Transfer Protocol)
* HTTP
  * HTML 문서와 같은 리소스들을 가져올 수 있도록 하는 프로토콜
  * 웹상에서 컨텐츠를 전송하기 위한 약속
  * '클라이언트-서버 프로토콜'이라고도 부름
  * 요청(클라이언트에 의해 전송되는 메세지), 응답(서버에서 응답으로 전송하는 메세지)와 같은 개별적인 메세지 교환에 의해 통신
* HTTP 특징
  * Stateless(무상태) : 동일한 연결에서 연속적으로 수행되는 두 요청 사이에 링크가 없음. 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음.

* HTTP Requet Methods
  * GET : 서버 리소스의 표현을 요청, GET을 사용하는 요청은 데이터만 검색해야함.
  * POST : 데이터를 지정된 리소스에 제출. 서버의 상태를 변경
  * PUT : 요청한 주소의 리소스를 수정
  * DELETE : 지정된 리소스를 삭제

* HTTP response status codes
  * 100 - 199 : Informational response
  * 200 - 299 : Successful response
  * 300 - 399 : Redirection message
  * 400 - 499 : Cilent error response
  * 500 - 599 : Server error response 

## URI(Uriform Resource Identifier)
* URI
  * 인터넷에서 하나의 리소스를 가리키는 문자열
  * 가장 일반적인 URI는 웹 주소로 알려진 URL
  * URN : 특정 이름공간에서 이름으로 리소스를 식별하는 URI(ex. ISBN - 국제 표준 도서번호)
* URL(Uniform Resource Locator)
  * 웹에서 주어진 리소스의 주소
  * 네트워크 상에 리소스가 어디있는지를 알려주기 위한 약속
* URL 구조
  * Scheme(or protocol)
    * 브라우저가 리소스를 요청하는 데 사용해야하는 프로토콜
    * URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지 나타냄
    * 기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기위한 `mailto:`, 파일을 전송하기 위한 `ftp:` 등 다른 프로토콜도 존재
  * Authority
    * Scheme 다음은 문자 패턴 "://"으로 구분된 Authority이 작성
    * Athority는 domain과 port를 모두 포함하며 ":"으로 구분됨
    * Domain : 요청 중인 웹서버를 나타냄. 어떤 웹 서버가 요구되는 지를 가리키며 직접 IP 주소를 사용하는 것도 가능. 하지만 사람이 외우기 어렵기 때문에 주로 Domain Name으로 사용
    * Port : 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문. HTTP 프로토콜의 표준 포트는 (HTTP - 80, HTTPS - 433)이며 생략 가능(나머지는 생각 불가)
  * Path
    * 웹 서버의 리소스 경로
    * 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 현재는 실제 위치가 아닌 추상화된 형태의 구조를 표현
  * Parameters
    * 웹 서버에 제공하는 추가적인 데이터
    * 파라미터는 '&'기호로 구분되는 key-value 쌍 목록
    * 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음
  * Anchor 
    * 리소스의 다른 부분에 대한 앵커
    * 리소스 내부 일종의 "북마크"를 나타내며 브라우저에 대한 해당 북마크 지점에 있는 콘텐츠를 표시
    * fragment idenrifier(부분 식별자)라고 부르는 '#' 이후 부분은 서버에 전송되지 않음.

## API(Application Programming Interface)
* API : 애플리케이션과 프로그래밍으로 소통하는 방법. API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약.
* REST(Resptresentational State Trasnfer)
  * API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  * 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
  * 자원을 식별 - URI / 자원의 행위 - HTTP Method / 자원의 표현 - JSON

## Serialization
* Serialization
  * 직렬화
  * 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고, 나중에 재구성 할수 있는 포맷으로 변환하는 과정
  * json, xml, yaml이 있으며 json이 가장 보편적으로 쓰임