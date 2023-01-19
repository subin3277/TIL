# SFC

## Component
* component
  * UI를 독립적이고 재사용 가능한 조각들로 나눈 것. 즉, 기능별로 분화한 코드 조각
  * CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
  * 하나의 app을 구성할 때 중첩된 컴포너트들의 tree로 구성하는 것이 보편적임.
  * 컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라 재사용성의 측면에서도 매우 강력한 기능을 제공.
* component based architecture 특징
  * 관리가 용이. 유지/보수 비용 감소
  * 재사용성
  * 확장 가능
  * 캡슐화
  * 독립적

## SFC
* SFC(Single File Component)
  * 하나의 `.vue` 파일이 하나의 Vue instance이고, 하나의 컴포넌트이다.
  * Vue instance에서는 HTML, CSS, JavaScript 코드를 한번에 관리
  * 컴포넌트 기반 개발의 핵심 기능

## Vue componenet
* 구조
  * 템플릿(HTML)
    * HTML이 body 부분
    * 눈으로 보여지는 요소 작성
    * 다른 컴포넌트를 HTML 요소처럼 추가 가능
  * 스크립트(JavaScript)
    * JavaScript 코드가 작성되는 곳
    * 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성 됨
  * 스타일(CSS)
    * CSS가 작성되며 컴포넌트의 스타일을 담당
  * 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦.
  * root에 해당하는 최상단 component가 App.vue
  * 이 App.vue를 index.html과 연결
  * 결국 index.html 파일 하나만을 rendering = SPA