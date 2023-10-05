# I/O

### I/O

- Input : 저장
- Output : 읽기
- I/O를 최대한 줄여야 속도가 빨라진다.

### I/O 발생

- 많이 발생하면
  - 메모리 늘리기 (캐싱)
  - 필요한 데이터가 최대한 많이 메모리 존재(캐싱)

### I/O 줄이기

- 분산처리

### I/O 응용

- 청군 vs 홍군
  - 홍군 기지를 공격하기 위해 두곳에 나뉘어져 있는 청군. 함께 들어가야하기 때문에 편지를 보내야한다
  - 왼쪽 청군
    - 오른쪽 청군이 응답 x
    - 오른쪽 청군의 응답을 홍군이 변경 후 다시 전송
  - 오른쪽 청군
    - 편지를 못받음
    - 홍군이 변경 후 전송
    - 홍군이 낚아챔
- 이로 인해 신뢰성 있는 통신 필요!