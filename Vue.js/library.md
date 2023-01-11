# A505 김수빈 230111

# Vue의 라이브러리
### Vuebar
* 스크롤 디자인을 변경할 수 있다
* 화면 안쪽에 overflow를 넣어 만든 element에 시스템 Scroll이 생길 경우 디자인을 해칠 수도 있다.
* 이때 Vuebar을 사용하면 Scroll 디자인을 커스텀할 수 있다
* `npm install vuebar --save`
* JS
  * element에 `v-bar`을 추가하고 바로 밑에 `<div></div>`를 추가한다.
* CSS
  * `background-color`을 이용해 원하는 색상을 넣을 수 있다

### vue-number-animation
* 페이지 랜더링 시 숫자가 올라가는 애니메이션 효과를 넣어준다.
* 지정된 숫자까지 숫자가 증가하는 애니메이션 생성
* `npm install vue-number-anmination --save`
* JS
  * `<number>` element 안에 속성을 넣어준다
  * from : 시작할 번호
  * to : 끝날 번호
  * duration : animation 진행 시간

### Simple Vue Validation
* 회원가입, 게시판 등 등록시 밸리데이션 체크
* `npm install simple-vue-validation --save`
* JS
  * input v-model로 바인딩 된 값으로 validation을 확인한다
  * required() : 필수 입력항목일 경우 사용
  * digit() : 숫자만 사용
* 오류 메세지도 custom 가능하다!!

### vue-number-format
* 숫자의 형태를 고정(Ex. 123,456,789)
* number component 사용. main.js에 아래 코드 추가
``` vue
createApp(App).use(number,{
    "decimal": ".",
    "separator": ",",
    "prefix": "한화 ",
    "suffix": " 원",
    "precision": 3
}).mount('#app')
```
* `<number></number>`태그를 이용하여 사용

### V-viewer
* 이미지 뷰어로 이미지 확대, 축소, 회전 등이 가능
* `import Viewer from 'v-viewer'`, `import 'viewerjs/dist/viewer.css'`
* `<viewer></viewer>`을 사용하여 구현
* title, movable, loop, initialViewIndex 활용 가능

### vue-drawing-canvas
* 그림판 생성후 그릴 수 있다
* `npm install --save-dev vue-drawing-canvas`
* `vue-drawing-canvas`태그를 이용하여 활용
* props
  * canvasId, width, height, image, strokeType, fillshape, eraser, color 등