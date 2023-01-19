# Routing

### Routing

- Routing

  - 네트워크에서 경로를 선택하는 프로세스
  - 웹 서비스에서의 라우팅
    - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것

- Routing in SSR

  - Server가 모든 라우팅을 통제
  - URL로 요청이 들어오면 응답으로 완성된 HTML 제공
  - Routing(URL)에 대한 결정권을 서버가 가짐

- Routing in SPA/CSR
  - 서버는 하나의 HTML(index.html)만을 제공
  - 이후에 모든 동작은 하나의 HTML 문서 위에 JS 코드 활용
    - DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
  - 즉, 하나의 URL만 가질 수 있음.

## Vue Router

- Vue Router
  - Vue의 공식 라우터
  - SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
  - 라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
    - SPA를 MPA처럼 URL을 이동하면서 사용가능
    - SPA의 단점 중 하나인 'URL이 변경되지 않는다.'를 해결
  - `vue add router`를 입력하여 설치 및 반영
- History mode
  - 브라우저의 History API를 활용한 방식
    - 새로고침 없이 URL 이동 기록을 남길 수 있음
  - Histroy mode를 사용하지 않으면 Default 값인 hash mode로 설정됨('#'을 통해 URL을 구분하는 방식)
- `router-link`
  - a 태그와 비슷한 기능 : URL을 이동시킴
    - routes에 등록된 컴포넌트와 매핑됨
    - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a 태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
  - 목표 경로는 'to' 속성으로 지정됨
  - 기능에 맞게 HTML에서 a 태그로 rendering 되지만, 필요에 따라 다른 태그로 바꿀 수 있음.
- `router-view`
  - 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
  - 실제 component가 DOM에 부착되어 보이는 자리를 의미
  - router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
- src/router/index.js
  - 라우터에 관련된 정보 및 설정이 작성되는 곳
  - routes에 URL와 컴포넌트를 매핑
- src/Views
  - router-view에 들어갈 component 작성
  - 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나뉘어짐
  - 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
  - views/
    - routes에 매핑되는 컴포넌트, 즉 <router-view>의 위치에 렌더링되는 컴포넌트를 모아두는 폴더
    - 다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것을 권장
  - components/
    - routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더

## Navigation Guard

- 네비게이션 가드
  - Vue router를 통해 특정 URL에 접근할 때 다른 url로 redirect를 하거나 해당 URL로의 접근을 막는 방법
  - 종류
    - 전역가드
    - 라우터 가드
    - 컴포넌트 가드
- 전역 가드
  - 다른 url 주소로 이동할 때 항상 실행
  - router/index.js에 `router.beforeEach()`를 사용하여 설정
  - 콜백 함수의 값으로 다음과 같이 3개의 인자를 받음
    - to : 이동할 URL 정보가 담긴 Route 객체
    - from : 현재 URL 정보가 담긴 Route 객체
    - next : 지정한 URL로 이동하기 위해 호출하는 함수
      - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
      - 기본적으로 to에 해당하는 URL로 이동
  - URL이 변경되어 화면이 전환되기 전 router.beforeEach()가 호출됨
    - 화면이 전환되지 않고 대기 상태가 됨
  - 변경된 URL로 라우팅하기 위해서는 next()를 호출해줘야함
    - next()가 호출되기 전까지 화면이 전환되지 않음
- 라우터 가드
  - 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
  - `beforeEnter()`
    - route에 진입했을 때 실행됨
    - 라우터를 등록한 위치에 추가
    - 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
    - 콜백 함수는 to, from, next를 인자로 받음
- 컴포넌트 가드
  - 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
  - `beforeRouteUpdate()`
    - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행
