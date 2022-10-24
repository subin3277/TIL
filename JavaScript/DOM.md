# DOM

## DOM
* Brower APIs
  * 웹 브라우저에 내장된 API로, 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러가지 유용하고 복잡한 일을 수행.
  * DOM, Geolocation API, WebGL etc..

* DOM
  * 문서 객체 모델(Document Object Model)
  * 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
  * 문서가 구조화되어 있으며 각 요소는 객체로 취급
  * 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
  * DOM은 문서를 논리 트리로 표현
  * DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고, 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음.
  
* `window` object
  * DOM을 표현하는 창
  * 가장 최상위 객체
  * 탭 기능이 있는 브라우저는 각각의 탭을 각각의 window 객체로 나타냄
  * 메서드
    * 새탭 열기 `window.open()`
    * 경고 대화 상자 표시 `window.print()`
    * 인쇄 대화 상자 표시 `window.alert()`

  * `document` object
    * 브라우저가 불러온 웹 페이지
    * 페이지 컨텐츠의 진입점 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함.

## DOM 조작
* 선택 관련 메서드
  * `document.querySelector(selector)`
    * 제공한 선택자와 일치하는 element 한개 선택
    * 제공한 CSS selector를 만족하는 첫번째 element 객체를 반환 (없다면 null 반환)
  * `document.querySelectorAll(selector)`
    * 제공한 선택자와 일치하는 여러 element를 선택
    * 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    * 제공한 CSS selector를 만족하는 NodeList를 반환

* 조작 관련 메서드
  * `document.createElement(tagName)` : 작성한 tagName의 HTML 요소를 생성하여 반환
  * `Node.innerText`
    * Node 객체와 그 자손의 텍스트 컨텐츠를 표현
    * 사람이 읽을 수 있는 요소만 남김
    * 즉, 줄바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
  * `Node.appendChild()`
    * 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
    * 한번에 오직 하나의 Node만 추가할 수 있음
    * 추가된 Node 객체를 반환
  * `Node.removeChild()`
    * DOM에서 자식 Node를 제거
    * 제거된 Node를 반환
  * `Element.getAttribute(attributeName)`
    * 해당 요소의 지정된 값(문자열)을 반환
    * 인자(attributeName)는 값을 얻고자하는 속성의 이름
  * `Element.setAttribute(name, value)`
    * 지정된 요소의 값을 설정
    * 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가