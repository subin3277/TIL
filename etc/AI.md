# 인공지능

### 인공지능(기계학습)
* 인공지능이란
  * 기계 지능을 다루는 컴퓨터 공학 분야
    - 인간 같은 인지능력을 구현
    - 추론, 문제 해결, 계획, 이해, 학습, 그리고 패턴을 인식
- 프로그래밍 vs 기계학습
  - 프로그래밍 : 데이터 + 프로그램 => 컴퓨터 => 출력
  - 기계학습 : 데이터 + 출력 => 컴퓨터 => 프로그램
- 기계학습
  - 지도학습(Supervised learning) : 입력과 정답을 반복적으로 알려줌
  - 비지도학습(Unsupervised learning) : 데이터 사이의 관계성을 도출

### 역사
- 인공지능의 시작
  - 퍼셉트론(Rosenblatt, 1958)
    - 1950년대 부터 연구시작
    - 최초로 구현된 인공 신경망
  - Perceptron의 한계
    - XOR 문제는 퍼셉트론만으로는 풀 수 없는 문제
    - 다층 퍼셉트론의 등장
- 딥러닝의 등장
  - AlexNet : ImageNet 챌린지 2012에서 큰 격차로 1등
  - 등장배경 : 데이터, 알고리즘, 연산 능력
- 기계학습 패러다임의 변화
  - 머신 러닝 : 입력 => 특징 추출 => 분류 => 출력
  - 딥 러닝 : 입력 => 특징 추출 & 분류 => 출력

### 지각능력
- 지각능력 이란?
  - 입출력 데이터
  - 인간은 자연스럽게 지각을 통해 상호작용하며 학습
  - 인간처럼 multi-modal의 상호 관계성으로부터 유용한 정보 수집
  - 기계가 세상을 인식하는 방법을 개발하는 것은 아직 활발한 연구 분야
- 최신 연구 동향
  - Media creation : Text-to-image 생성 연구
  - Media creation : Text-to-video 생성 연구
  - Media creation : Text-to-human 생성 연구
  - Media creation : Text-to-audio 생성 연구
  - Media creation : 소리기반 talking head 생성
  - 음성 생성 연구
  - AR & VR application - Codec Avatar
  - 인간을 뛰어넘는 인지능력 : 육안으로는 잘 보이지 않는 것을 관찰 가능하게 해줌

### 기계학습
- 기계학습의 구성요소
  - 경험사례
  - 모델
  - 평가 기준
  - 경험 사례(data) -> 모델(인공 신경망) <-> 평가기준
- 가장 좋은 모델은 어떻게 찾을 수 있을까?
  - Annotation을 통한 학습으로 이루어 짐
  - min(최적화)||Label - f(data)||
- 적용 예시
  - 문제 정의 : 주어진 주식 변동 그래프를 통하여 시간의 흐름과 주가와의 관계를 알고싶음
  - 시간 => Model => 주가
  - 과거의 결과들 = Data
- 기계학습이란
  - 계산 / 추론 (computation / inference)
    - 함수를 주고, Output이 나오도록 계산
  - 최적화(Optimization)
    - 한 세트(input, output)을 주고 관계를 가장 잘 설명하는 f를 찾는 것
- 문제 해결 방법
  - 충분히 많은 양의 데이터 사용
  - 모델의 복잡도 줄이기
  - 가중치의 regularization 적용하기
  - 드롭아웃(drop out)
- Deep Neural Network
  - 모델이 충분히 크다면 input과 output의 관계를 모두 학습할 수 있음