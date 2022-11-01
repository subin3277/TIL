# Vue

## MVVM Pattern
* MVVM Pattern
  * 소프트웨어 아키텍처 패턴의 일종
  * 마크업 언어로 구현하는 그래픽 사용자 인터페이스(view)의 개발을 Back-end(model)로부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함.
  * View - 우리 눈에 보이는 부분 = DOM
  * Model - 실제 데이터 = JSON
  * View Model = View
    * View를 위한 Model
    * View와 연결되어 Action을 주고 받음
    * Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
    * View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨

## 문법
* vue instance
``` javascript
const vm = new Vue()
console.log(vm)
```
* el(element)
  * Vue instance와 DOM을 연결(mount)하는 옵션. View와 Model을 연결하는 역할. HTML id 혹은 class와 마운트 가능
  * Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음.
``` javascript
const app = new Vue({
  el: '#app' // DOM 연결
})
```
* data
  * Vue instance의 데이터 객체 혹은 인스턴스 속성
  * 데이터 객체는 반드시 기본 객체 '{}' 여야함
  * 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
  * 정의된 속성은 'interpolations {{}}'을 통해 view에 렌더링 가능함
``` javascript
const app = new Vue({
  el : '#app',
  data:{
    message: 'Hello, Vue!'
  },
})
```
* method
  * Vue instance의 method들을 정의하는 곳
  * method를 정의할때, Arrow Function을 사용하며 안됨
``` javascript
const app = new Vue({
  el : '#app',
  data:{
    message: 'Hello, Vue!'
  },

  methods :{
    bye: function () {
      this.message = 'Bye, Vue!'
    },
  }
})
```

## Basic of Syntax
* Basic of Syntax
  * 렌더링 된 DOM을 기본 Vue instance의 data에 선언적으로 바인딩 할 수 있는 HTML 기반 template syntax를 사용
  * 렌더링 된 DOM - 브라우저에 의해 보기 좋게 그려질 HTML 코드
  * HTML 기반 template syntax - HTML 코드에 직접 작성할 수 있는 문법 제공
  * 선언적으로 바인딩 - Vue instance와 DOM을 연결
* Template Interpolation
  * 가장 기본적인 바인딩(연결) 방법
  * 중괄호 2개로 표기
  * DTL과 동일한 형태로 작성
  * Template interpolation 방법은 HTML을 일반 텍스트로 표현
* RAW HTML
  * v-html directive을 사용하여 data와 바인딩
  * directive - HTML기반 template syntax
  * HTML의 기본 속성이 아닌 Vue가 제공하는 특수 속성의 값으로 data를 작성

## Directives
* Directives 기본 구성
  * v-접두사가 있는 특수 속성에는 값을 할당 할 수 있음.
  * 값에는 JS표현식을 작성할 수 있음.
  * directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것
  * `v-on:submit.prevent="onSubmit"`
    * `:` 을 통해 전달 인자를 받을 수 있음
    * `.`으로 표시되는 특수 접미사-directive를 특별한 방법으로 바인딩 해야함.
* v-text
  * Template Interpolation과 함께 가장 기본적인 바인딩 방법
  * {{}}와 동일한 역할
* v-html
  * RAW HTML을 표현할 수 있는 방법
  * 단, 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용금지
* v-show
  * 표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정. boolean 값이 변경 될 때마다 반은
  * 대상 element의 display 속성을 기본 속성과 none으로 toggle
  * 요소 자체는 항상 DOM에 렌더링 됨
  * 화면에서만 사라졌을 뿐, DOM에는 존재한다. display 속성이 변경되었을 뿐
* v-if
  * v-show와 사용 방법은 동일
  * isActive의 값이 변경될 때 반응
  * 단, 값이 false인 경우 DOM에서 사라짐
  * v-if, v-else-if, v-else 형태로 사용
* v-for
  * `for .. in ..` 형식으로 작성
  * 반복한 데이터 타입에 모두 사용가능
  * index를 함께 출력하고자 한다면 `(char, index)`형태로 사용 가능
  * 배열 역시 문자열과 동일하게 사용 가능
  * 각 요소가 객체라면 dot notation으로 접근 할 수 있음
* v-on
  * `:`을 통해 전달받은 인자를 확인
  * 값으로 JS 표현식 작성
  * addEventListener의 첫번째 인자와 동일한 값들로 구성
  * 대기하고 있던 이벤트가 발생하면 할당된 표현식 실행
  * method를 통한 data 조작도 가능
  * method에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일한 방식
  * `:`을 통해 전달된 인자에 따라 특별한 modifiers(수식어)가 있을 수 있음
  * `@` shortcut 제공
* v-bind
  * HTML 기본 속성에 Vue data를 연결
  * class의 경우 다양한 형태로 연결 가능
    * 조건부 바인딩 : `{'class Name':'조건 표현식'}`, 삼항 연산자도 가능
    * 다중 바인딩 : ['JS 표현식', 'JS 표현식', ...]
  * Vue data의 변화에 반응하여 DOM에 반영하므로 상황에 따라 유동적 할당 가능
  * `:`shortcut 제공
* v-model
  * Vue instance와 DOM의 방방향 바인딩
  * Vue data 변경시 v-model로 연결된 사용자 입력 element에도 적용

## Vue advanced
* computed
  * Vue instance가 가진 options 중 하나
  * computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산. 계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 계산된 값을 반환
* watch
  * 특정 데이터의 변화를 감지하는 기능
    1. watch 객체를 정의
    2. 감시할 대상 data를 지정
    3. data가 변할 시 실행 할 함수를 정의
  * 첫번째 인자는 변동 전 data
  * 두번째 인자는 변동 후 data
  * 실행 함수를 Vue method로 대체가능
    1. 감시 대상 data의 이름으로 객체 생성
    2. 실행하고자 하는 method를 handler에 문자열 형태로 할당
  * Array, Object의 내부 요소 변경을 감지를 위해서는 deep 속성 추가 필요
* filters
  * 텍스트 형식화를 적용할 수 있는 필터
  * interpolation 혹은 v-bind를 이용할 때 사용 가능
  * 필터는 자바스크립트 표현식 마지막에 `|`와 함께 추가되어야 함
  * 이어서 사용 가능   