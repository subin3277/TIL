# CSS Layout

## Float
* 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping 하도록 함. 요소가 Normal flow를 벗어나도록 함
* 속성 
    * none : 기본값
    * left : 요소를 왼쪽으로 띄움
    * right : 요소를 오른쪽으로 띄움

## Flexbox
* 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
* 축 : 메인 축(main axis), 교차 축(cross axis)
* 구성 요소
    * 부모 요소(Flex Container) : flexbox 레이아웃을 형성하는 가장 기본적인 모델. Flex Item들이 놓여있는 영역. display 속성을 flex 혹은 inline-flex로 지정
    * 자식 요소(Flex item) : 컨테이너에 속해 있는 컨텐츠
* 속성
    * 배치 설정
        * flex-direction : Main axis 기준 방향 설정, 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (row, row-reverse, column, column-reverse)
        * flex-wrap : 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정. 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함. (wrap - 넘치면 그 다음 줄로 배치, nowrap - 기본 값. 한줄에 배치)
        * flex-flow : flex-direction과 flex-wrap의 shorthand. 두 설정 값을 차례로 작성
    * 공간 나누기 
        * justify-content : main axis를 기준으로 공간 배분 (flex-start, flex-end, center, space-between, space-around, space-evenly)
        * align-content : cross axis를 기준으로 공간 배분, 아이템이 한 줄로 배치되는 경우 확인 할 수 없음. (flex-start, flex-end, center, space-between, space-around, space-evenly)
    * 정렬
        * align-items : 모든 아이템을 cross axis 기준으로 정렬(stretch, flex-start, flex-end, center, baseline), align-self(개별 아이템)