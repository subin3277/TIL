# Vue CLI
## CLI
* Vue 개발을 위한 표준 도구
* 프로젝트의 구성을 도와주는 역할
* 확장 플러그인, GUI, Babel등 다양한 tool 제공

* 명령어
  * 설치 : `npm install -g @vue/cli`
  * 프로젝트 생성 : `vue create {이름}`
  * 프로젝트 실행 : `npm run serve`

## 프로젝트 구조
* node_modules
  * node.js 환경의 여러 의존성 모듈
  * python의 venv와 비슷한 역할을 함.
  * Babel : Javascript compiler
    * 자바스크립트의 ES6+ 코드를 구버전으로 번역/변환 해주는 도구
    * 자바스크립트의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양
    * 최신 문법을 사용해도 브라우저의 버전 별로 동작하지 않는 상황이 발생.
    * 버전에 따른 같은 의미의 다른 코드를 작성하는 등의 대응이 필요해졌고, 이러한 문제를 해결하기 위한 도구
  * Webpack : static module bundler
    * 모듈 간의 의존성 문제를 해결하기 위한 도구
    * 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함
* package.json
  * 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함
* package-lock.json
  * node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
  * 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
  * 사용할 패키지의 버전을 고정
  * 개발 과정 간의 의존성 패키지 충돌 방지
* public/index.html
  * vue 앱의 뼈대가 되는 html 파일
  * vue 앱과 연결될 요소가 있음
* src/
  * src/assets : 정적 파일을 저장하는 디렉토리
  * src/components : 하위 컴포넌트들이 위치
  * src/App.vue : 최상위 컴포넌트. public/index.html과 연결됨
  * src/main.js : webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point. public/index.html과 src/App.vue를 연결시키는 작업이 이루어지는 곳. vue 전역에서 활용할 모듈을 등록할 수 있는 파일