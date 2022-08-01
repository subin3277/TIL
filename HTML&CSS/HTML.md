# HTML (Hyper Text Markup Language)
 : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트 + 태그등을 이용하여 문서나 데이터의 구조를 명시하는 언어

## 기본구조
* html : 문서의 최상위(root) 요소
* head : 문서 메타데이터 요소 (문서 제목, 인코딩, 스타일, 외부파일로딩등.. 일반적으로 브라우저에 나타나지 않는 나용)
* body : 문서 본문 요소 (실제 화면 구성과 관련된 내용)
``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset = "UTF-8">
    <title> Document</title>
</head>
<body>

</body>
</html>
```
* head 예시
    * `<title>` : 브라우저 상단 타이틀
    * `<meta>` : 문서 레벨 메타데이터 요소
    * `<link>` : 외부 리소스 연결 요소(CSS 파일, favicon 등)
    * `<script>` : 스크립트 요소(JavaScript 파일/코드)
    * `<style>` :  CSS 직접 작성
    
* 요소(element) : 태그와 내용으로 구성
`<h1>contents</h1>`
    * 요소는 태그로 컨텐츠를 감싸는 것으로 그 정보의 성격과 의미를 정의
    * 내용이 없는 태그들도 존재(닫는 태그 x) (ex. br, hr, img, input, link, meta)
    * 요소는 중첩될 수 있음

* 속성(attribute)
`<a herf="https://google.com"></a>`
    * 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
    * 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보 제공
* HTML Global Attribute : 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성(몇명 요소에는 아무 효과 없을 수 있음)
    * id : 문서 전체에서 유일한 고유 식별자 지정
    * class : 공백으로 구분된 해당 요소의 클래스의 목록(CSS, JS에서 요소를 선택하거나 접근)
    * data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
    * style : inline 스타일
    * title : 요소에 대한 추가 정보 지정
    * tabindex : 요소의 탭 순서
* 시멘틱 태그 : HTML 태그가 특정 목적, 역할 및 의미적 가치를 가지는 것
    * Non semantic 요소 : div, span
    * header : 문서 전체나 섹션의 헤더(머리말 부분)
    * nav : 내비게이션
    * aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
    * section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
    * article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
    * footer : 문서 전체나 섹션의 푸터(마지막 부분)

## 문서 구조화
* 인라인 / 블록 요소
    * HTML 요소는 크게 인라인/블록 요소로 나눔
    * 인라인 : 글자처럼 취급
    * 블록 요소 : 한 줄 모두 사용
* 텍스트 요소

| 태그 | 설명 |
| ------------ | -------------------- |
| `<a></a>` | herf 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성  |
| `<b></b>`, `<strong></strong>` | 굵은 글씨 요소 중요한 강조하고자 하는 요소(보통 굵은 글씨로 표현)  |
| `<i></i>`, `<em></em>` | 기울임 글씨 요소, 중요한 강조하고자 하는 요소 ( 보통 기울임 글씨로 표현)  |
| `<br>` | 텍스트 내에 줄바꿈 생성  |
| `<img></img>` | src 속성을 활용하여 이미지 표현  |
| `<span></span>` | 의미 없는 인라인 컨테이너  |

* 그룹 컨텐츠

| 태그 | 설명 |
| ------------ | -------------------- |
| `<p></p>` | 하나의 문단(paragraph) |
| `<hr>` | 문단 레벨 요소에서 주제의 분리를 의미, 수평선으로 표현 |
| `<ol></ol>`, `<ul></ul>` | 순서가 있는 리스트, 순서가 없는 리스트 |
| `<pre></pre>` | HTML에 작성한 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백문자를 유지 |
| `<blockquote></blockuote>` | 텍스트가 긴 인용문, 주로 들여쓰기를 한 것으로 표현됨 |
| `<div></div>` | 의미 없는 블록 레벨 컨테이너  |
* form
    * `<form>`은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
    * action : form을 처리할 서버의 URL(데이터를 보낼 곳)
    * method : form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
    * enctype : method가 post인 경우 데이터의 유형

* input
    * 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
    * name : form control에 적용되는 이름 (이름/값 페어로 전송됨)
    * value : form control에 적용되는 값(이름/값 페어로 전송됨)
    * required, readonly, autofocus, autocomplete, disabled 등...
* input 유형
    * text : 일반 텍스트 입력
    * password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
    * email : 이메일 형식이 아닌 경우 form 제출 불가
    * number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
    * file : accept 속성을 활용하여 파일 타입 지정 가능
    * checkbox : 다중 선택
    * radio : 단일 선택
    * color : color picker
    * date : date picker
    * hidden : 사용자에게 보이지 않는 input