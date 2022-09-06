# Django Form

## Form에 대한 Django의 역할
* Form은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
* Django는 Form과 관련한 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공하여, 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성 가능

## Form에 대한 작업
* 렌더링을 위한 데이터 준비 및 재구성
* 데이터에 대한 HTML forms 생성
* 클라이언트로부터 받은 데이터 수신 및 처리

## Form Class 선언
* Form Class를 선언하는 것은 Model Class를 선언하는 것과 비슷. 비슷한 이름의 필드 타입을 많이 가지고 있다(이름만 같을 뿐 다른 필드)
* Model과 마찬가지로 상속을 통해 선언

## Form rendering options
* `as_p()` : 각 필드가 단락`<p> 태그`으로 감싸져서 렌더링
* `as_ul()` : 각 필드가 목록 항목`<li> 태그`으로 감싸져서 렌더링. `<ul>`태그는 직접 작성.
* `as_table()` : 각 필드가 테이블`<tr> 태그` 행으로 감싸져서 렌더링
* 특별한 상황아니면 `as_p()`를 사용

## HTML input 요소 표현
* Form fields
    * 입력에 대한 유효성 검사 로직을 처리
    * 템플릿에서 직접 사용됨
* Widgets
    * 웹 페이지의 HTML input 요소 렌더링을 담당(input 요소의 단순한 출력 부분을 담당)
    * Widgets은 반드시 form fields에 할당됨

## Widgets
* Django의 HTML input element의 표현을 담당
* 단순히 HTML 렌더링을 처리하는 것이며 유효성 검증과 아무런 관계가 없음
`content = forms.ChrField(widget=forms.Textarea)`

