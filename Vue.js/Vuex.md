# Vuex

## State Management
* State : 현재에 대한 정보(data)
* State Management
  * 각 component는 독립적이기 때문에 각각의 상태(data)를 가짐
  * 여러개의 componenet가 같은 상태(data)를 유지할 필요가 있음
* Pass Props & Emit Event
  * 같은 데이터를 공유하고 있으므로, 각 컴포넌트가 동일한 상태를 유지하고 있음
  * 데이터의 흐름을 직관적으로 파악 가능
  * 하지만 componenet의 중첩이 깊어지면 데이터 전달이 쉽지 않음
* Centralized Stroe
  * 중앙 저장소(store)에 데이터를 모아서 상태 관리
  * 각 component는 중앙 저장소의 데이터를 사용
  * componenet의 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경 가능
  * 중앙 저장소의 데이터가 변경되면 각각의 componenet는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영.
* Vuex
  * state management pattern + Libray for vue.js (상태 관리 패턴 + 라이브러리)
  * 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
  * 데이터가 예측 가능한 방식으로만 변경 될 수 있도록하는 규칙을 설정하며, Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공 

## Vuex 시작하기
* 프로젝트 생성
  ```
  vue create vuex-app // Vue 프로젝트 생성
  cd vuex-app // 디렉토리 이동
  vue add vuex // Vue Cli를 통해 vuex plugin 적용
  ```
  * src/stroe/index.js 생성
  * vuex의 핵심 컨셉 4가지
    * state
    * getters
    * mutations
    * actions
* vuex의 핵심 컨셉
  * state
    * vue 인스턴스의 data에 해당
    * 중앙에서 관리하는 모든 상태 정보
    * 개별 componene는 state에서 데이터를 가져와서 사용
    * state의 데이터가 변화하면 해당 데이터를 사용하는 componenet도 자동으로 다시 렌더링
    * `$store.state`로 state 데이터에 접근
  * Mutations
    * 실제로 state를 변경하는 유일한 방법
    * vue 인스턴스의 methods에 해당하지만 Mutations에서 호출되는 핸들러(handler) 함수는 반드시 동기적이어야함
    * 첫번째 인자로 state를 받으며, componenet 혹은 Actions에서 `commit()` 메서드로 호출됨
  * Actions
    * mutations와 비슷하지만 비동기 작업을 포함할 수 있다는 차이가 있음
    * state를 직접 변경하지 않고 commit() 메서드로 mutations를 호출해서 state를 변경함.
    * context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근할 수 있음(즉, state를 직접 변경할 수 있찜나 하지 않아야함)
    * componenet에서 `dispatch()` 메서드에 의해 호출됨
  * Getters
    * vue 인스턴스의 computed에 해당
    * state를 활용하여 계산된 값을 얻고자 할 때 사용. state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음.
    * computed와 마찬가지로 getters의 결과는 캐시(cache)되며, 종속된 값이 변경된 경우에만 재계산됨.
    * getters에서 계산된 값은 state에 영향을 미치지 않음.
    * 첫번째 인자로 'state', 두번째 인자로 'getter'를 받음
  * 정리
    * componenet에서 데이터를 조작하기 위한 데이터의 흐름
      * component => (actions) => mutations = > state
    * componenet에서 데이터를 사용하기 위한 데이터의 흐름
      * state => (getters) => component

## Local Storage
* Window.`localStorage`
  * 브라우저에서 제공하는 저장공간 중 하나인 Local Storage에 관련된 속성
  * 만료되지 않고 브라우저를 종료하고 다시 실행해도 데이터가 보존됨
  * 데이터가 문자열 형태로 저장됨
  * 관련 메서드
    * `setItem(key, value)` : key, value 형태로 데이터 저장
    * `getItem(key)` : key에 해당하는 데이터 조회
* vuex-persistedstate
  * vuex state를 자동으로 브라우저의 Local Storage에 저장해주는 라이브러리 중 하나
  * 페이지가 새로고침 되어도 Vuex state를 유지시킴
  * Local Storage에 저장된 data를 자동으로 state로 불러옴.
  * 설치 
    `npm i vuex-persistedstate`
  * 적용
    ``` javascript
    import createPersistedState from 'vuex-persistedstate'

    export default new Vuex.Store({
      plugins: [
        createPersistedState(),
      ]
    })
    ```
