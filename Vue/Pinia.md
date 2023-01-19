# A505 김수빈 230110

# Pinia
### 제작자
Vue 코어 팀의 멤버로 Vue Router를 개발한 Eduardo San Martin Morote에 의해 만들어졌다.

### 사용
Vue2, Vue3에서 모두 사용 가능하다

### Pinia vs Vuex
* Pinia는 Vuex보다 간단한 API를 가진다
  - Pinia의 API는 Vuex보다 간단하며, 더 직관적이다
  * 보일러플레이트 코드가 제거되었다.
* Pinia는 모듈식으로 설계
  * Vuex는 내부에 여러 개의 모듈을 가질 수 있는 단일 store가 제공된다
  * Pinia에서는 필요한 컴포넌트에서 바로 가져와서 사용할 수 있는 store를 여러개 생성할 수 있다.
  * 번들러의 코드 스플릿과 타입스크립트 추론이 더 나아지도록 돕는다.
  * store의 메서드만 사용하기 때문에 개발 과정이 단순화 되었다
* Devtool이 제공된다.
  * Vuex는 DevTools를 활용하면 쉽다
  * 위와 비슷한 Pinia devtools가 있으며 Vue 앱에 Pinia를 설치하면 바로 사용할 수 있다
* Pinia에는 타입스크립트 지원이 내장되어있다.
  * 타입 안전성은 잠재적인 런타임 에러 방지와 같은 많은 이점을 제공한다.
  * 타입스크립트를 활용해서 앱을 개발하고 있지 않더라도, Pinia의 재설계된 개발자 경험을 통해 자동완성이나 자동 제안과 같은 큰 이점을 얻을 수 있다.
  
### 기본 구조
``` vue
//stores/list.js
import {defineStore} from 'pinia';

export const useListStore = defineStore("list", {
  state : () => ({list : []}),
  actions : {
    addList(param){
      this.list.push(param);
    }
    //addList:(param) => this.list.push(param);
  },
  getters: {
    getAllList(state){
      return state.list;
    }
    // getAllList: (state) => state.list
  }
})
```
