# CSS (Cascading Style Sheets)
: 스타일을 지정하기 위한 언어

* CSS 기본 구조
  * 중괄호 안에서 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
  * 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미(속성 : 어떤 스타일 기능을 변경할지 결정, 값 : 어떻게 스타일 기능을 변경할지 결정)
``` css
h1 {
  color : blue;
  font-size : 15px;
}
```

* CSS 정의 방법
  * 인라인 : 실수가 잦아짐(중복도 있고, 찾기가 어려워서)
  * 내부 참조(embedding) - `<style>` (코드가 너무 길어짐)
  * 외부 참조(link file) - 분리된 CSS (가장 많이 쓰는 방식)
--- 
## CSS Selector
* 선택자 유형
  * 기본 선택자 : 전체 선택자, 요소 선택자, 클래스 선택자, 아이디 선택자, 속성 선택자
  * 결합자(Conbinators) : 자손 결합자( ), 자식 결합자(>), 일반 형제 결합자(~), 인접 형제 결합자(+)
  * 의사 클래스/요소(Pseudo Class) : 링크, 동적 의사 클래스, 구조적 의사 클래스, 의사 엘리먼트, 속성 선택자
* 기본 선택자
  * 요소 선택자 : HTML 태그를 직접 선택
  * 클래스 선택자 : 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
  * 아이디 선택자 : # 문자로 시작ㅎ하며, 해당 아이디가 적용된 항목을 선택, 일반적으로 하나의 문서에 1번만 사용, 여러번 사용해도 동작하지만 단일 id 사용을 권장
``` CSS
<style>
/* 전체 선택자 */
  * {
    color : red;
  }
/* 요소 선택자 */
  h2 {
    color : orange;
  }
/* 클래스 선택자 */
  .green {
    color : green;
  }
/* id 선택자 */
  #purple {
    color : purple;
  }
/* 자식 결합자 */
  .box > p {
    font-size : 30px
  }
/* 자손 결합자 */
  .box p {
    color : blue;
  }
</style>
```
* CSS 적용 우선순위
  1. 중요도(Importance) - 사용시 주의 : !important
  2. 우선 순위 (Specificity) : 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
  3. CSS 파일 로딩 순서
* CSS 상속
  * CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다
  * 속성 중에서 상속이 되는 것(Text 관련 요소, opacity, visivility...)과 되지 않는 것(Box model 관련 요소, position 관련요소...)들이 있다.
  ---
  ## CSS 기본 스타일
* 크기 단위
  * px : 모니터 해상도의 한 화소인 '픽셀' 기준, 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
  * % : 백분율 단위, 가변적인 레이아웃에서 자주 사용
  * em : (바로위, 부모 요소에 대한) 상속의 영향을 받음. 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
  * rem : (바로위, 부모 요소에 대한) 상속의 영향을 받지 않음. 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
  * viewport : 웹페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역, 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨 (vw, vh, vmin, vmax / 1vw = A/100)
* 색상단위
  * 색상 키워드 : 대소문자를 구분하지 않음. red, blue, black 과 같은 특정 색을 직접 글자로 나타냄
  * RGB 색상 : 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
* CSS 문서 표현
  * 텍스트 : 서체, 서체스타일, 자간, 단어간격, 행간...
  * 컬러, 배경
  * 목록, 표
---
## Box Model
* CSS 원칙 1 : 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.
* Box model :star:
  * margin : 테두리 바깥의 외부 여백. 배경색 지정 x
  * border : 테두리 영역
  * padding : 테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding까지 적용
  * content : 글이나 이미지 등 요소의 실제 내용
* box-sizing
  * 기본적으로 모든 요소의 box-sizing은 content-box. Padding을 제외한 순수 contents 영역만을 box로 지정
  * 다만 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함. 그 경우 box-sizing을 border-box로 설정
---
## CSS Display
* CSS 원칙 2 : display에 따라 크기와 배치가 달라진다.
* 대표적인 display
  * display : block
    * 줄바꿈이 일어나는 요소
    * 화면 크기 전체의 가로 폭을 차지
    * 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
  * display : inline
    * 줄바꿈이 일어나지 않는 행의 일부 요소
    * content 너비 만큼 가로 폭을 차지
    * width, height, margin-top, margin-bottom을 지정할 수 없다.
    * 상하 여백은 line-height로 지정
  * display : inline-block
    * block과 inline 레벨 요소의 특징을 모두 가짐
    * inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
  * display : none :star:
    * 해당 요소를 화면에 표시하지않고, 공간조차 부여되지 않음. 이와 비슷한 visibility:hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.
* 블록 레벨 요소 vs 인라인 레벨 요소
  * 블록 레벨 요소 : div, ul, ol, li, p, hr, form ...
    * block의 기본 너비는 가질 수 있는 너비의 100%
    * 너비를 가질 수 없다면 자동으로 부여되는 margin
  * 인라인 레벨 요소 : span, a, img, input, label, b, em, i, strog ...
    * inline의 기본 너비는 컨텐츠 영역만큼
---
## CSS Position
* CSS position : 문서 상에서 요소의 위치를 지정
  * static : 모든 태그의 기본값(기준 위치)
    * 일반적인 요소의 배치 순서에 따름(좌측 상단)
    * 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
  * 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동가능
    * relative (상대 위치. 원래 있던 자리에서 옮겨감. 원래 있던 자리는 비워져 있음)
    * absolute (절대 위치. 부모요소 상단을 기준으로 옮겨감)
    * fixed (고정 위치. 부모요소와 관계없이 viewport를 기준으로 이동)
    * sticky (스크롤에 따라 static -> fixed로 변경. 생성된 위치로부터 항상 설정값만큼 떨어져있다 )
