# Lifecycle Hooks

## Lifecycle Hooks
* Lifecycle Hooks
  * 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침.
    * Vue 인스터스가 생성된 경우, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM을 업데이트하는 경우 등..
  * 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음.
  * 이를 Lifecycle Hooks이라고 함.
* 종류
  * created
    * Vue instance가 생성된 후 호출됨
    * data, computed 등의 설정이 완료된 상태
    * 서버에서 받은 데이터를 vue instance의 data에 할당하는 로직을 구현하기 적합
    * 단 mount 되지 않아 요소에 접근할 수 없음.
  * mounted
    * Vue instance가 요소에 mount된 후 호출됨
    * mount된 요소를 조작할 수 있음
    * created의 경우, mount되기 전이기 때문에 DOM에 접근할 수 없으므로 동작하지 않음.
    * mounted는 주석처리
  * updated
    * 데이터가 변경되어 DOM에 변화를 줄 때 호출됨
* 특징
  * instance마다 각각의 Lifecycle을 가지고 있음
  * Lifecycle Hooks는 컴포넌트별로 정의할 수 있음
  * 부모 컴포넌트의 mounted hook이 실행되었다고 해서 자식이 mount된 것이 아니고, 부모 컴포넌트가 updated hook이 실행되었다고 해서, 자식이 updated 된 것이 아님.
    * 부착 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않은 것
    * instance마다 각각 Lifecycle을 가지고 있기 때문