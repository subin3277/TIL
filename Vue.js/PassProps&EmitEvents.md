# Pass Props & Emit Event

## Data in components
* Data in components
  * 한페이지 내에서 같은 데이터를 공유해야 함. 하지만 페이지들은 component로 구분이 되어있음.
  * 자식 컴포넌트에도 똑같은 data를 정의
  * 필요한 컴포넌트들끼리 데이터 주고 받으면?
    * 데이터의 흐름 파악 힘듦.
    * 개발 속도 저사
    * 유지보수 난이도 증가
  * 부모-자식 관계만 데이터를 주고받기
    * 데이터의 흐름을 파악하기 용이
    * 유지 보수하기 쉬워짐
* pass props : 부모 => 자식
* emit event : 자식 => 부모

## Pass Props