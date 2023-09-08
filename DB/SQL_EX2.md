# SQL Example

### 예제

#### Part3

- ex111
  - sql로 숫자 1부터 10번까지 출력
    `select level as num from dual connect by level <= 10`
  - 1부터 100까지의 합 출력
    `select sum(level) as num from dual connect by level <= 100;`
  - 1부터 100까지 숫자 55를 뺀 수의 합 출력
    `select sum(level) as num from dual where level != 55 connect by level <= 100`
  - 1부터 100까지 짝수의 합 출력
    `select sum(level) as num from dual where mod(level, 2) = 0 connect by level <= 100`
- ex112
  - 구구단
    `with loop_table as ( select level as num from dual connect by level <= 9 ), gugu_table as ( select level + 1 as gugu from dual connect by level <= 8) select to_char(a.num) || 'x' || to_char(b.gugu) || '=' || to_char(b.gugu*a.num) as 구구단 from loop_table a, gugu_table b`
  - 구구단 2, 5, 7단만 출력
    `with loop_table as ( select level as num from dual connect by level <= 9 ), gugu_table as ( select level + 1 as gugu from dual connect by level <= 8) select to_char(a.num) || 'x' || to_char(b.gugu) || '=' || to_char(b.gugu*a.num) as 구구단 from loop_table a, gugu_table b where a.num in (2,5,7)`
  - 구구단에서 짝수단만 출력
    `with loop_table as ( select level as num from dual connect by level <= 9 ), gugu_table as ( select level + 1 as gugu from dual connect by level <= 8) select to_char(a.num) || 'x' || to_char(b.gugu) || '=' || to_char(b.gugu*a.num) as 구구단 from loop_table a, gugu_table b where mod(a.num, 2)=0`
- ex113
  - 직각 삼각형 출력
    `with loop_table as (select level as num from dual connect by level <= 8) select lpad('*', num, '*')as star from loop_table`
  - 삼각형을 뒤집어서 출력
    `with loop_table as (select level as num from dual connect by level <= 8) select lpad('*', 9 - num, '*')as star from loop_table`
  - 위 두개 합쳐진 삼각형 출력
    `with loop_table as (select level as num from dual connect by level <= 8) select lpad('*', num, '*')as star from loop_table union all select lpad('*', 9 - num, '*')as star from loop_table`
- ex114
  - 삼각형 출력
    `with loop_table as (select level as num from dual connect by level <= 8) select lpad(' ', 10 - num, ' ') || lpad('*', num, '*') as star from loop_table`
  - 역삼각형 출력
    `with loop_table as (select level as num from dual connect by level <= 8) select lpad(' ', num, ' ') || lpad('*', 9 - num, '*') as star from loop_table`
- ex115
  - 사용자에게 입력 받기
    `undefine p_num accept p_num prompt '숫자입력 : '`
  - 마름모 출력
    `select lpad(' ', 9 - level, ' ') || lpad('★', level, '★') as star from dual connect by level<=9 union all select lpad(' ', level, ' ') || lpad('★', 9 - level, '★') as star from dual connect by level < 9`
  - 모래시계 출력
    `select lpad(' ', level, ' ') || lpad('★', 9 - level, '★') as star from dual connect by level < 9 union all select lpad(' ', 9 - level, ' ') || lpad('★', level, '★') as star from dual connect by level<=9`
- ex116

  - 사각형 출력

  ```sql
  undefine p_n1
  undefine p_n2
  accept p_n1 prompt '가로 :';
  accept p_n2 prompt '세로 :';

  with loop_table as (select level as num from dual connect by level <= &p_n2) select lpad('★', &p_n1, '★') as star from loop_table
  ```

  - 숫자를 한번만 물어보고 정사각형 출력

  ```sql
  undefine p_n1
  accept p_n1 prompt '숫자 :';
  select lpad('★', &p_n1, '★') as star from dual connect by level <= &p_n1
  ```

- ex117
  - 1부터 10까지의 합 출력
  ```sql
  undefine p_n1
  accept p_n1 prompt '숫자 :';
  select sum(level) as 합계 from dual connect by level <= &p_n1
  ```
  - 1부터 100까지의 숫자 중 짝수의 합 출력
    `select sum(level) as 합계 from dual where mod(level, 2)=0 connect by level <= &p_n1`
  - 1부터 100까지의 숫자 중 홀수의 합 출력
    `select sum(level) as 합계 from dual where mod(level, 2)=1 connect by level <= &p_n1`
- ex118
  - 1부터 10까지의 곱 출력
    `select round(exp(sum(ln(level)))) 곱 from dual connect by level <= &p_n`
  - 1부터 100까지의 짝수 숫자들의 곱 출력
    `select round(exp(sum(ln(level)))) 곱 from dual where mod(level,2) = 0 connect by level <= &p_n`
- ex119
  - 1부터 10까지 짝수만 출력
    `select listagg(level, ',') from dual where mod(level, 2)=0 connect by level <= 10`
  - 1부터 10까지 홀수만 출력
    `select listagg(level, ',') from dual where mod(level, 2)=1 connect by level <= 10`
- ex120
  - 소수 출력
    `with loop_table as (select level as num from dual connect by level <= 10) select l1.num as 소수 from loop_table l1, loop_table l2 where mod(l1.num, l2.num) = 0 group by l1.num having count(l1.num) = 2 `
  - 소수의 합 출력
    `select sum(소수) from (with loop_table as (select level as num from dual connect by level <= 10) select l1.num as 소수 from loop_table l1, loop_table l2 where mod(l1.num, l2.num) = 0 group by l1.num having count(l1.num) = 2) `
  - 소수의 곱 출력
    `select round(exp(sum(ln(소수)))) 곱 from (with loop_table as (select level as num from dual connect by level <= 10) select l1.num as 소수 from loop_table l1, loop_table l2 where mod(l1.num, l2.num) = 0 group by l1.num having count(l1.num) = 2 )`
- ex121
  - 16과 24의 최대공약수
    `with num_d as (select 16 as num1, 24 as num2 from dual) select max(level) 최대공약수 from num_d where mod(num1, level) = mod(num2, level) and mod(num1, level) = 0 connect by level <= num2`
  - 16, 24, 48의 최대 공약수
    `with num_d as (select 16 as num1, 24 as num2, 48 as num3 from dual) select max(level) 최대공약수 from num_d where mod(num1, level) = 0 and mod(num2, level)=0 and mod(num3, level) = 0 connect by level <= num3`
- ex122
  - 16과 24의 최소공배수
    `select 16*24 / (with num_d as (select 16 as num1, 24 as num2 from dual) select max(level) 최대공약수 from num_d where mod(num1, level) = mod(num2, level) and mod(num1, level) = 0 connect by level <= num2) 값 from dual;`
  - 16, 24, 56의 최소공배수
    `with num_d as (select 16 as num1, 24 as num2, 48 as num3 from dual) select (num1/max(level))*(num2/max(level))*max(level) 최소공배수 from num_d where mod(num1, level) = 0 and mod(num2, level)=0 and mod(num3, level) = 0 connect by level <= num3`
- ex123
  - 피타고라스 정리로 직각삼각형 확인
    `select case when power(&num1, 2) + power(&num2, 2) = power(&num3, 2) then '맞습니다' else '아닙니다' end as 삼각형 from dual`
  - 빗변 두개와 밑변을 각각 물어보게 하고 정삼각형이 맞는지 확인
    `select case when (&num1 = &num2 and &num2 = &num3) then '맞습니다' else '아닙니다' end as 삼각형 from dual`
- ex124
  - 원주율 구하기
    `select sum(case when (power(num1, 2) + power(num2,2)) <= 1 then 1 else 0 end) / 100000 * 4 as 원주율 from (select dbms_random.value(0,1) as num1, dbms_random.value(0,1) as num2 from dual connect by level < 100000)`
- ex125
  - 자연상수 e 구하기
    `with loop_table as (select level as n from dual connect by level <= 100000) select result from (select n, power ((1+1/n), n)as result from loop_table) where n=100000`
