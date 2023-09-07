# SQL Example

### 기본 Database

- 사원 테이블
  사원번호, 사원이름, 월급, 직업, 관리자번호, 입사일, 커미션 ,부서번호
  ![Alt text](image.png)
- 부서 테이블
  부서번호, 부서이름, 위치
  ![Alt text](image-1.png)

### 예제

#### PART 1

- ex1_select
  - 사원테이블의 사원 번호와 이름 월급 출력
    `select empno, ename, sal from emp;`
  - 사원테이블의 사원 이름과 직업과 부서번호 출력
    `select ename, job, deptno from emp;`
- ex2\_\*
  - 사원 테이블의 모든 열과 데이터 출력
    `select * from emp;`
  - 부서 테이블의 모든 열과 데이터 출력
    `select * from dept;`
- ex3_as
  - 사원테이블의 사원번호, 이름, 월급의 컬럼명 변경하여 출력
    `select empno as "사원번호", ename as "사원이름", sal as "Salary" from emp;`
  - 이름과 직업을 출력하는데 컬럼명이 한글로 이름, 직업으로 출력
    `select ename as "이름", job as "직업" from emp;`
- ex4\_||
  - 사원테이블의 이름과 월급을 붙여서 출력
    `select ename || sal from emp;`
  - 사원테이블의 이름과 직업을 붙여서 문장으로 출력
    `select ename ||'의 직업은 '|| sal || '입니다' from emp;`
- ex5_distinct
  - 직업을 중복행 제거하여 출력
    `select distinct job from emp;`
  - 부서번호를 중복행 제거하여 출력
    `select distinct deptno from emp;`
- ex6_order by
  - 이름과 월급을 출력하는데 월급이 낮은 사원부터(오름차순)
    `select ename, sal from emp order by sal asc;`
  - 이름과 입사일을 출력하는데 최근에 입사한 사원부터(내림차순)
    `select ename, hiredate from emp order by hiredate desc;`
- ex7_where
  - 월급이 3000인 사원들의 사원이름, 월급, 직업 출력
    `select ename, sal, job from emp where sal = 3000;`
  - 사원번호가 7788인 사원의 사원번호, 사원이름, 월급 출력
    `select empno, ename, sal from emp where empno = 7788;`
- ex8_where
  - 이름이 scott인 사원의 이름, 월급, 직업, 입사일, 부서번호 출력
    `select ename, sal, job, hiredate, deptno from emp where ename='SCOTT';`
  - 직업이 salesman인 사원들의 이름, 직업, 입사일 출력
    `select ename, job, hiredate from emp where job='SALESMAN';`
  - 81/11/17일에 입사한 사원의 이름, 입사일 출력
    `select ename, hiredate from emp where hiredate='81/11/17';`
- ex9_where
  - 연봉이 36000 이상인 사원들의 이름과 연봉을 출력. 연봉은 월급의 12배
    `select ename, sal*12 from emp where sal*12 >= 36000`
  - 직업이 analyst인 사람들의 이름과 연봉 출력
    `select ename, sal*12 from emp where job='ANALYST'`
- ex10_where
  - 연봉이 1200이하인 사원들의 이름, 월급, 직업, 부서번호 출력
    `select ename, sal, job, deptno from emp where sal <= 1200`
  - 직업이 salesman이 아닌 사원들의 이름과 직업 출력
    `select ename, job from emp where job != 'SALESMAN'`
- ex11_between
  - 월급이 1000 에서 3000 사이인 사원들의 이름과 월급 출력
    `select ename, sal from emp where sal between 1000 and 3000`
  - 월급이 1000에서 3000 사이가 아닌 사원들의 이름과 월급 출력
    `select ename, sal from emp where sal not between 1000 and 3000`
  - 1981년 11월 01일부터 1982년 05월 30일 사이에 입사한 사원들의 이름과 입사일 출력
    `select ename, hiredate from emp where hiredate between '1981/11/01' and '1982/05/30'`
- ex12_like
  - 이름의 첫글자가 S로 시작하는 사원들의 이름 출력
    `select ename from emp where ename like 'S%'`
  - 이름의 끝글자가 T로 시작하는 사원들의 이름 출력
    `select ename from emp where ename like '%T'`
  - 이름의 두번째 철자가 M인 사원들의 이름 출력
    `select ename from emp where ename like '_M%'`
- ex13_null
  - 커미션이 null인 사원들의 이름과 커미션 출력
    `select ename, comm from emp where comm is null`
  - 커미션이 null이 아닌 사원들의 이름과 커미션 출력
    `select ename, comm from emp where comm is not null`
- ex14_in
  - 직업이 salesman, analyst, manager인 사원들의 이름과 월급과 직업 출력
    `select ename, sal, job from emp where job in ('SALESMAN', 'ANALYST', 'MANAGER')`
  - 직업이 salesman, analyst, manager가 아닌 사원들의 이름과 월급과 직업 출력
    `select ename, sal, job from emp where job not in ('SALESMAN', 'ANALYST', 'MANAGER')`
- ex15_where and
  - 직업이 salesman이고 월급이 1200이상인 사원들의 이름과 월급과 직업을 출력
    `select ename, sal, job from emp where job='SALESMAN' and sal >= 1200`
  - 부서번호가 30번이고 커미션이 100이상인 사원들의 이름과 월급과 커미션을 출력
    `select ename, sal, comm from emp where deptno = 30 and comm >= 100`

#### PART 2

- ex16_lower()
  - 사원의 테이블에서 이름을 출력하는데 모두 소문자로 출력
    `select lower(ename) from emp`
  - 이름이 scott인 사원의 이름과 월급을 출력하는데 이름을 소문자로 검색해도 결과 출력
    `select ename, sal from emp where lower(ename)='scott'`
- ex17_substr()
  - SMITH라는 단어에서 MI만 추출해서 출력
    `select substr('SMITH', 2, 2) from dual`
  - 사원테이블에서 이름을 출력하는데 이름의 첫글자만 출력하고 첫글자를 소문자로 출력
    `select lower(substr(ename, 1, 1)) from emp`
- ex18_length()
  - 이름을 출력하고 이름의 철자의 길이를 출력
    `select ename, length(ename) from emp`
  - 이름의 철자의 길이가 5개 이상인 사원들의 이름과 이름의 철자의 길이를 출력
    `select ename, length(ename) from emp where length(ename) >= 5`
- ex19_instr()
  - SMITH이라는 단어에서 알파벳 M이 몇번째 자리에 있는지 출력
    `select instr('SMITH', 'M') from dual`
  - 이름에 철자가 S가 포함된 사원들의 이름을 출력
    `select ename from emp where instr(ename, 'S') > 0`
- ex20_replace(),regexp_replace()
  - 이름과 월급을 출력하는데 숫자 0을 _로 출력
    `select ename, replace(sal, '0', '_') from emp`
  - 이름과 월급을 출력하는데 숫자 0번부터 3번까지는 _로 출력
    `select ename, regexp_replace(sal, '[0-3]', '_') from emp`
- ex21_lpad(),rpad()
  - 이름과 월급을 출력하는데 월급 컬럼의 자릿수를 10자리로 하고 나머지 자리에 _를 채워서 출력
    `select ename, lpad(sal, 10, '_') from emp`
  - 이름과 월급을 출력하는데 월급 컬럼의 자릿수를 10자리로 하고, 월급을 출력하고 남은 나머지 자리 오른쪽에 _를 채워서 출력
    `select ename, rpad(sal, 10, '_') from emp`
- ex22_ltrim(),rtrim(),trim()
  - 다음과 같이 smith 영어단어에서 앞에 s를 잘라내서 출력하고 h를 잘라서 출력하고 양쪽 s를 잘라서 출력
    `select 'smith', ltrim('smith','s'), rtrim('smith','h'), trim('s' from 'smiths') from dual`
  - 다음의 데이터를 사원 테이블에 입력하고 이름이 JACK인 사원의 이름과 월급 출력
    `insert into emp(empno, ename, sal) values(3821, 'JACK ', 3000)`
    `select * from emp where rtrim(ename)='JACK'`
- ex23_round()
  - 876.567 숫자를 출력하는데 소수점 두번째 자리에서 반올림
    `select round(876.567, 1) from dual`
  - 사원 테이블에서 이름과 월급의 12%을 출력하는데 소수점 이하는 출력되지 않도록 반올림
    `select ename, round(sal*0.12) from emp`
- ex24_trunc()
  - 876.567 숫자를 출력하는데 소수점 두번째자리와 그 이후 숫자들은 모두 버리고 출력
    `select trunc(876.567, 1) from dual`
  - 사원 테이블에서 이름과 월급의 12%을 출력하는데 소수점 이하는 출력되지 말고 출력
    `select ename, trunc(sal*0.12) from emp`
- ex25_mod()
  - 숫자 10을 3으로 나눈 나머지 값을 출력
    `select mod(10, 3) from dual`
  - 사원 번호가 홀수인 사원들의 사원번호와 이름 출력
    `select empno, ename from emp where mod(empno, 2) = 1`
- ex26_months_between()
  - 이름을 출력하고 입사한 날짜부터 오늘까지 총 몇달을 근무했는지 출력
    `select ename, round(months_between(sysdate, hiredate)) from emp`
  - 내가 태어난 날부터 오늘까지 총 몇달인지 출력
    `select round(months_between(sysdate, '19990327')) from dual`
- ex27_add_months()
  - 2019년 5월 1일부터 100달 뒤의 날짜는 어떻게 되는지 출력
    `select add_months('20190501', 100) from dual`
  - 오늘부터 100달 뒤의 날짜가 어떻게 되는지 출력
    `select add_months(sysdate, 100) from dual`
- ex28_next_day()
  - 2021년 5월 5일로부터 바로 돌아오는 월요일의 날짜가 어떻게 되는지 출력
    `select next_day('20210505', '월요일') from dual`
  - 오늘부터 앞으로 돌아올 금요일의 날짜가 어떻게 되는지 출력
    `select next_day(sysdate, '금요일') from dual`
- ex29_last_day()
  - 2021년 5월 5일의 해당 달의 마지막 날의 날짜를 출력
    `select last_day('20210505') from dual`
  - 오늘부터 요번 달 말일까지 총 몇일 남았는지 출력
    `select last_day(sysdate)-sysdate from dual`
- ex30_to_char()
  - 이름이 scott인 사원의 입사한 요일과 월급을 출력하는데 월급을 출력할 때에 다음과 같이 천단위를 표시해서 출력
    `select ename, to_char(hiredate, 'day'), to_char(sal, '999,999') from emp where ename='SCOTT'`
  - 수요일에 입사한 사원들의 이름과 입사일과 입사한 요일을 출력
    `select ename, hiredate, to_char(hiredate, 'day') from emp where to_char(hiredate, 'day') = '수요일'`
  - 내가 태어난 생일의 요일 출력
    `select to_char(to_date('1999/03/27', 'RRRR/MM/DD'),'day') from dual`
- ex31_to_date()
  - 81년 11월 17일에 입사한 사원의 이름과 입사일 출력
    `select ename, hiredate from emp where hiredate=to_date('81/11/17','RR/MM/DD')`
  - 1981년에 입사한 사원들의 이름과 입사일을 출력하는데 최근에 입사한 사원부터 출력
    `select ename, hiredate from emp where hiredate between to_date('1981/01/01','RRRR/MM/DD') and to_date('1981/12/31', 'RRRR/MM/DD')+1 order by hiredate desc`
- ex32
  - 암시적 형 변환
  - `select ename, sal from emp where sal = '3000'` 실행 가능
  - `select ename, sal from emp where sal like '30%'` 실행 가능
- ex33_nvl()
  - 이름과 월급과 커미션을 출력하는데 커미션이 null인 사원들은 값을 0으로 출력
    `select ename, sal, nvl(comm, 0) from emp`
  - 이름과 커미션을 출력하는데 커미션이 null인 사원들은 no comm이라는 글씨로 출력
    `select ename, sal, nvl(to_char(comm), 'no comm') from emp`
- ex34_decode()
  - 이름, 부서번호, 보너스를 출력하는데 보너스가 부서번호가 10번이면 300, 부서번호가 20번이면 400, 나머지 부서번호는 0 출력
    `select ename, deptno, decode(deptno, 10, 300, 20, 400, 0) from emp`
  - 이름, 직업, 보너스를 출력하는데 직업이 salesman이면 6000, analyst면 3000, manager이면 2000, 나머지는 0 출력
    `select ename, job, decode(job, 'SALESMAN', 6000, 'ANALYST', 3000, 'MANAGER', 2000, 0) as "보너스" from emp`
- ex35_case then
  - 직업이 salesman, analyst인 사원들의 이름, 직업, 월급, 보너스를 출력하는데 월급이 3000이상이면 보너스를 500 출력하고 월급이 2000이상이면 보너스 300을 출력하고 월급이 1000이상이면 보너스를 200 출력하고 나머지는 0 출력
    `select ename, job, sal, case when sal >= 3000 then 500 when sal >= 2000 then 300 when sal >= 1000 then 200 else 0 end as "보너스" from emp`
  - 이름, 월급, 보너스를 출력하는데 월급이 3000이상이면 보너스를 9000 출력하고 월급이 2000이상이면 8000출력하고 나머지는 0 출력
    `select ename, sal, case when sal >= 3000 then 9000 when sal >= 2000 then 8000 else 0 end as "보너스" from emp`
- ex36_max()
  - 사원테이블에서 최대 월급 출력
    `select max(sal) from emp`
  - 직업이 salesman인 사원들중에서의 최대월급 출력
    `select max(sal) from emp where job='SALESMAN'`
  - 직업이 salesman인 사원들 중에서 최대월급을 출력하는데 직업도 함께 출력
    `select job, max(sal) from emp where job='SALESMAN' group by job`
- ex37_min()
  - 직업이 salesman인 사원들 중에서 최소 월급 출력
    `select min(sal) from emp where job='SALESMAN'`
  - 부서번호가 20번인 사람들중에서 최소월급 출력
    `select min(sal) from emp where deptno=20`
  - 부서번호와 부서번호별 최소 월급 출력
    `select deptno, min(sal) from emp group by deptno`
- ex38_avg()
  - 사원 테이블에서 평균 월급 출력
    `select round(avg(sal)) from emp`
  - 직업과 직업별 평균월급을 출력하는데 직업별 평균 월급이 높은 것부터 출력
    `select job, round(avg(sal)) from emp group by job order by 2 desc`
  - 부서번호, 부서번호별 평균 월급을 출력하는데 부서번호별 평균월급을 출력할때에 천단위 표시를 하시오
    `select deptno, to_char(round(avg(sal)), '999,999') from emp group by deptno`
- ex39_sum()
  - 부서번호, 부서번호별 토탈 월급 출력
    `select deptno, sum(sal) from emp group by deptno`
  - 1981년도에 입사한 사원들의 월급의 토탈값 출력
    `select sum(sal) from emp where to_char(hiredate, 'yyyy')='1981'`
  - 직업과 직업별 토탈월급을 출력하는데 직업별 토탈월급이 6000이상인것만 출력
    `select job, sum(sal) from emp group by job having sum(sal) >= 6000`
- ex40_count()
  - 사원 테이블의 전체 인원수가 어떻게 되는지 출력
    `select count(*) from emp`
  - 부서번호, 부서번호 별 인원수 출력
    `select deptno, count(*) from emp group by deptno`
  - 직업과 직업별 인원수를 출력하는데 직업이 salesman은 제외하고 출력하고 직업별 인원수가 3명 이상인 것만 출력
    `select job, count(*) from emp where job != 'SALESMAN' group by job having count(*) >= 3`
- ex41_rank() over ()
  - 직업이 analyst, manager인 사원들의 이름, 직업, 월급, 월급에 대한 순위 출력
    `select ename, job, sal, rank() over (order by sal desc) 순위 from emp where job in ('ANALYST', 'MANAGER')`
  - 부서번호가 20인 사원들의 이름과 부서번호와 월급과 월급에 대한 순위 출력
    `select ename, deptno, sal, rank() over (order by sal desc) 순위 from emp where deptno = 20`
- ex42_dense_rank() over ()
  - 이름과 직업과 월급과 순위를 출력하는데 그 옆에 순위가 동일한 사람이 여러명인 경우 바로 다음 순위가 출력
    `select ename, job, sal, dense_rank() over (order by sal desc) 순위 from emp where job in ('ANALYST', 'MANAGER')`
  - 직업, 이름, 월급, 순위를 출력하는데 순위가 직업별로 각각 월급이 높은 사원 순으로 순위 출력
    `select job, ename, sal, dense_rank() over (partition by job order by sal desc) 순위 from emp`
  - 월급이 2975인 사원은 사원 테이블에서 월급의 순위 출력
    `select dense_rank(2975) within group (order by sal desc) 순위 from emp`
- ex43_ntile()
  - 직업이 analyst, manager, clerk인 사원들의 이름과 직업과 월급과 등급을 출력하는데 등급을 4등급으로 나눠서 출력
    `select ename, job, sal, ntile(4) over (order by sal desc) 등급 from emp where job in ('ANALYST', 'MANAGER', 'CLERK')`
  - 이름, 입사일, 입사한 사원순으로 등급을 나누는데 등급을 5등급으로 나눠서 출력
    `select ename, hiredate, ntile(5) over (order by hiredate asc) 등급 from emp`
- ex44_cume_dist()
  - 이름과 월급과 순위와 자신의 월급의 순위에 대한 비율을 출력
    `select ename, sal, rank() over (order by sal desc), dense_rank() over (order by sal desc), cume_dist() over (order by sal desc) 비율 from emp`
  - 부서번호, 이름과 월급과 월급의 순위에 대한 비율 출력. 순위 비율이 부서번호별로 각각 출력
    `select deptno, ename, sal, cume_dist() over (partition by deptno order by sal desc) 순위 from emp`
- ex45_listagg()
  - 부서번호를 출력하고, 해당 부서번호별로 속한 사원들의 이름을 가로로 출력
    `select deptno, listagg(ename, ',') within group (order by ename asc) as 이름 from emp group by deptno `
  - 직업, 직업별로 속한 사원들의 이름을 가로로 출력하는데 가로로 출력될 때에 월급이 높은 사원부터 출력
    `select job, listagg(ename, ',') within group (order by sal desc) as 이름 from emp group by job `
- ex46_lag() lead()
  - 직업이 analyst, manager인 사원들의 사원번호화 이름과 월급을 출력하는데 다음과 같이 월급의 그 전행과 그 다음행이 출력
    `select empno, ename, sal, lag(sal, 1) over (order by sal asc) 전행, lead(sal, 1) over (order by sal asc) 다음행 from emp where job in ('ANALYST', 'MANAGER')`
  - 이름, 입사일, 바로 전에 입사한 사원과의 간격일을 출력
    `select ename, hiredate, hiredate - lag(hiredate, 1) over (order by hiredate asc) 간격일 from emp`
- ex47_decode()
  - 부서번호와 부서번호별 토탈 월급을 가로로 출력
    `select sum(decode(deptno, 10, sal, null)) as "10", sum(decode(deptno, 20, sal, null)) as "20", sum(decode(deptno, 30, sal, null)) as "30" from emp`
  - 직업, 직업별 토탈월급을 가로로 출력
    `select sum(decode(job, 'ANALYST', sal)) as "ANALYST",
sum(decode(job, 'CLERK', sal)) as "CLERK",
sum(decode(job, 'SALESMAN', sal)) as "SALESMAN",
sum(decode(job, 'MANAGER', sal)) as "MANAGER",
sum(decode(job, 'PRESIDENT', sal)) as "PRESIDENT"                
from emp`
- ex48
  - 부서번호, 부서번호별 토탈 월급을 가로로 출력
    `select * from (select deptno, sal from emp) pivot ( sum(sal) for deptno in (10, 20, 30))`
  - 직업, 직업별 토탈월급을 가로로 출력
    `select * from (select job, sal from emp) pivot ( sum(sal) for job in ('ANALYST', 'CLERK', 'SALESMAN', 'MANAGER', 'PRESIDENT'))`
- ex49_unpivot()
  - 컬럼이 데이터로 들어가게
    `select * from order2 unpivot ( 건수 for 아이템 in (BICYCLE, CAMERA, NOTEBOOK))`
  - 범죄원인 테이블을 생성하고 방화사건의 가장 큰 원인이 무엇인지 출력
    `select * from crime_cause unpivot (건수 for 원인 in (생계형, 유흥, 도박, 허영심, 복수, 해고, 징벌, 가정불화, 호기심, 유혹, 사고, 불만, 부주의, 기타)) where crime_type='방화' order by 건수 desc`
- ex50_rows between unbounded preceding and current row
  - 직업이 analyst, manager인 사원들의 사원번호, 사원이름, 월급, 월급에 대한 누적치를 출력
    `select empno, ename, sal, sum(sal) over (order by empno rows between unbounded preceding and current row) 누적치 from emp where job in ('ANALYST', 'MANAGER')`
  - 부서번호가 20번인 사원들의 사원이름, 월급, 월급에 대한 누적치 출력
    `select ename, sal, sum(sal) over (order by empno rows between unbounded preceding and current row) 누적치 from emp where deptno=20`
- ex51_ratio_to_report()
  - 부서번호가 20번인 사원들의 사원번호, 이름, 월급, 월급에 대한 비율 출력
    `select empno, ename, sal, round(ratio_to_report(sal) over (), 2) 비율 from emp where deptno=20`
  - 사원 테이블 전체에서 사원번호, 이름, 월급, 월급에 대한 비율 출력
    `select empno, ename, sal, round(ratio_to_report(sal) over (), 2) 비율 from emp`
- ex52_rollup()
  - 직업, 직업별 토탈월급을 출력하는데 맨 아래에 전체 토탈월급이 출력
    `select job, sum(sal) from emp group by rollup(job)`
  - 부서번호, 부서번호별 토탈 월급을 출력하는데 맨 아래에 전체 토탈월급이 출력
    `select deptno, sum(sal) from emp group by rollup(deptno)`
- ex53_cube()
  - 직업, 직업별 토탈월급을 출력하는데 맨 위에 토탈월급이 출력
    `select job, sum(sal) from emp group by cube(job)`
  - 입사한 년도, 년도별 토탈 월급을 출력하는데 맨위에 사원 테이블의 전체 토탈월급 출력
    `select to_char(hiredate, 'RRRR'), sum(sal) from emp group by cube(to_char(hiredate, 'RRRR'))`
- ex54_grouping sets()
  - 직업별 토탈 월급과 부서번호별 토탈월급과 전체 토탈월급을 같이 출력
    `select deptno, job, sum(sal) from emp group by grouping sets ( deptno, job, () )`
  - 입사한 년도별 토탈월급과 직업별 토탈월급을 같이 출력
    `select to_char(hiredate, 'RRRR'), job, sum(sal) from emp group by grouping sets ((to_char(hiredate, 'RRRR')), (job))`
- ex55_row_number()
  - 부서번호가 20인 사원들의 사원번호, 사원이름, 월급, 순위를 출력하는 결과 끝에 번호를 넘버링해서 출력
    `select empno, ename, sal, rank() over (order by sal desc) as rank, dense_rank() over (order by sal desc) as dense_rank, row_number() over (order by sal desc) as row_num from emp`
  - 월급이 1000에서 3000 사이인 사원들의 이름과 월급을 출력하는데 출력하는 결과 맨 끝에 번호를 넘버링
    `select ename, sal, row_number() over (order by empno asc) as 번호 from emp where sal between 1000 and 3000`
- ex56_rownum
  - 사원 테이블에서 맨 위의 5개 행만 출력
    `select rownum, empno, ename, job, sal from emp where rownum <= 5`
  - 직업이 salesman인 사원들의 이름과 월급과 직업을 출력하는데 맨위의 행 2개만 출력
    `select ename, sal, job from emp where job='SALESMAN' and rownum <= 2`
- ex57_fetch first {n} rows only
  - 월급이 높은 사원순으로 사원번호, 이름, 직업, 월급을 출력하는데 맨위의 행 4개만 출력
    `select empno, ename, sal, job from emp order by sal desc fetch first 4 rows only`
  - 최근에 입사한 사원순으로 이름, 입사일과 월급을 출력하는데 맨위의 행 5개만 출력
    `select ename, hiredate, sal from emp order by hiredate desc fetch first 5 rows only`
- ex58_join
  - 사원테이블과 부서테이블을 조인해서 이름과 부서위치를 출력
    `select e.ename, d.loc from emp e , dept d where e.deptno = d.deptno`
  - 직업이 salesman인 사원들의 이름과 직업과 부서위치를 출력
    `select e.ename, e.job, d.loc from emp e, dept d where e.deptno = d.deptno and e.job='SALESMAN'`
  - dallas에서 근무하는 사원들의 이름과 월급과 부서위치를 출력
    `select e.ename, e.sal, d.loc from emp e, dept d where e.deptno = d.deptno and d.loc='DALLAS'`
- ex59_join
  - 사원테이블과 급여 테이블과 조인하여 이름과 월급과 월급에 대한 등급을 출력
    `select e.ename, e.sal, s.grade from emp e, salgrade s where e.sal between s.losal and s.hisal`
  - 급여등급이 4등급인 사원들의 이름과 월급을 출력하는데 월급이 높은 사원부터 출력
    `select e.ename, e.sal, s.grade from emp e, salgrade s where s.grade=4 and e.sal between s.losal and s.hisal order by e.sal desc`
- ex60\_ (+)
  - 이름과 부서위치를 출력하는데 boston도 출력
    `select e.ename, d.loc from emp e, dept d where e.deptno (+) = d.deptno`
  - 사원테이블 전체에 이름과 부서위치를 출력하는데 jack도 출력
    `select e.ename, d.loc from emp e, dept d where e.deptno = d.deptno (+)`
- ex61_join
  - 직업이 salesman인 사원들의 사원이름과 직업을 출력하고 관리자 이름과 관리자의 직업 출력
    `select 사원.ename as 사원, 사원.job as 직업, 관리자.ename as 관리자, 관리자.job as 직업 from emp 사원, emp 관리자 where 사원.mgr = 관리자.empno`
  - 위 결과를 출력하는데 관리자인 사원들보다 더 많은 월급을 받는 사원들의 데이터만 출력
    `select 사원.ename as 사원, 사원.job as 직업, 관리자.ename as 관리자, 관리자.job as 직업 from emp 사원, emp 관리자 where 사원.mgr = 관리자.empno and 사원.sal > 관리자.sal`
- ex62_join on
  - on 절을 사용한 조인문법으로 결과 출력
    `select e.ename, e.sal, e.job, d.loc from emp e join dept d on ( e.deptno = d.deptno ) where e.job='SALESMAN'`
  - 월급이 1000에서 3000인 사이인 사원들의 이름과 월급과 부서위치를 on절을 사용한 조인문법으로 출력
    `select e.ename, e.sal, d.loc from emp e join dept d on (e.deptno = d.deptno) where e.sal between 1000 and 3000`
- ex63_join using
  - using 절을 사용한 조인문법으로 결과 출력
    `select e.ename, e.job, e.sal, d.loc from emp e join dept d using (deptno)`
  - using 절을 사용한 조인문법으로 부서위치가 dallas인 사원들의 이름과 월급과 부서위치 출력
    `select e.ename, e.sal, d.loc from emp e join dept d using (deptno) where d.loc = 'DALLAS'`
- ex64_natural join
  - natural join으로 결과 출력
    `select e.ename, e.job, e.sal, d.loc from emp e natural join dept d`
  - 직업이 salesmand이고 부서번호가 30번인 사원들의 이름과 직업과 월급과 부서위치 출력
    `select e.ename, e.job, e.sal, d.loc from emp e natural join dept d where e.job='SALESMAN' and deptno=30`
- ex65_rigth/left outer join
  - 1999 ansi 조인문법의 outer join으로 결과 출력
    `select e.ename, e.job, e.sal, d.loc from emp e right outer join dept d on (e.deptno = d.deptno)`
  - 1999 ansi 조인문법을 사용하여 이름과 직업, 월급과 부서위치를 출력하는데 사원 테이블에 jack도 출력
    `select e.ename, e.job, e.sal, d.loc from emp e left outer join dept d on (e.deptno = d.deptno)`
- ex66_full outer join
  - 다음과 같이 jack도 출력되고 부서위치의 boston도 출력
    `select e.ename, e.job, e.sal, d.loc from emp e full outer join dept d on (e.deptno = d.deptno)`
  - 직업이 ANALYST 이거나 부서위치가 BOSTON인 사원들의 이름과 직업과 월급과 부서위치를 출력하는데 full outer 조인을 사용
    `select e.ename, e.job, e.sal, d.loc from emp e full outer join dept d on (e.deptno = d.deptno) where e.job='ANALYST' or d.loc='BOSTON'`
- ex67_union all
  - 부서번호와 부서번호별 토탈 월급을 출력하는데 맨아래 전체 토탈 월급도 출력
    `select deptno, sum(sal) from emp group by deptno union all select null, sum(sal) from emp`
  - 직업과 직업별 토탈월급을 출력하는데 맨 아래에 전체 토탈월급도 출력
    `select job, sum(sal) from emp group by job union all select to_char(null) as job, sum(sal) from emp order by job asc`
- ex68_union
  - 부서번호와 부서번호별 토탈 월급을 출력하고 맨 아래에 전체 토탈월급도 출력하는데 부서번호가 오름차순으로 정렬
    `select deptno, sum(sal) from emp group by deptno union select to_number(null) as deptno, sum(sal) from emp`
  - 직업, 직업별 토탈월급을 출력하는데 직업이 abcd 순으로 정렬되어서 출력하고 맨 아래에 전체 토탈월급을 출력
    `select job, sum(sal) from emp group by job union select to_char(null) as job, sum(sal) from emp`
  - 입사한 년도, 입사한 년도별 토탈월급을 출력하는데 맨 아래에 전체 토탈월급이 출력
    `select to_char(hiredate, 'RRRR'), sum(sal) from emp group by to_char(hiredate, 'RRRR') union select to_char(null) as job, sum(sal) from emp`
- ex69_intersect
  - 집합 연산자로 데이터의 교집합 출력
    `select ename, sal, job, deptno from emp where deptno in (10, 20) intersect select ename, sal, job, deptno from emp where deptno in (20, 30)`
  - 사원 테이블과 부서 테이블과의 공통된 부서번호 출력
    `select deptno from emp intersect select deptno from dept`
- ex70_minus
  - 집합 연산자로 데이터의 차이 출력
    `select ename, sal, job, deptno from emp where deptno in (10, 20) minus select ename, sal, job, deptno from emp where deptno in (20, 30)`
  - 부서테이블에는 존재하는데 사원 테이블에는 존재하지 않는 부서번호 출력
    `select deptno from emp minus select deptno from dept`
- ex71\_단일 쿼리문
  - jones보다 더 많은 월급을 받는 사원들의 이름과 월급 출력
    `select ename, sal from emp where sal > (select sal from emp where ename='JONES')`
  - allen보다 더 늦게 입사한 사원들의 이름과 월급 출력
    `select ename, sal from emp where hiredate > (select hiredate from emp where ename='ALLEN')`
- ex72\_다중 쿼리문
  - 직업이 salesman인 사원들과 같은 월급을 받는 사원들의 이름과 월급 출력
    `select ename, sal from emp where sal in (select sal from emp where job='SALESMAN')`
  - 부서번호가 20번인 사원들과 같은 직업을 갖는 사원들의 이름과 직업 출력
    `select ename, sal from emp where job in (select job from emp where deptno=20)`
- ex73_not in
  - 관리자인 사원들의 이름을 출력
    `select ename from emp where empno in (select mgr from emp)`
  - 관리자가 아닌 사원들의 이름을 출력
    `select ename from emp where empno not in (select nvl(mgr, -1) from emp)`
- ex74_exists
  - 부서 테이블에 있는 부서번호 중에서 사원 테이블에 존재하는 부서번호에 대한 모든 컬럼 출력
    `select * from dept where exists ( select * from emp where emp.deptno = dept.deptno)`
- ex75_having
  - 직업과 직업별 토탈월급을 출력하는데 직업이 salesman인 사원들의 토탈월급보다 더 큰 것만 출력
    `select job, sum(sal) from emp group by job having sum(sal) > (select sum(sal) from emp where job ='SALESMAN')`
  - 부서번호, 부서번호 별 인원수를 출력하는데 10번 부서번호의 인원수보다 더 큰 것만 출력
    `select deptno, count(*) from emp group by deptno having count(*) > (select count(*) from emp where deptno = 10)`
- ex76_from의 서브 쿼리
  - 사원 테이블에서 월급을 가장 많이 받는 사원의 이름과 월급과 월급의 순위 출력
    `select * from ( select ename, sal, rank() over (order by sal desc) rnk from emp ) where rnk = 1`
  - 직업이 salesman인 사원들중에서 가장 먼저 입사한 사원의 이름과 입사일 출력
    `select * from ( select ename, hiredate, rank() over (order by hiredate asc) rnk from emp where job = 'SALESMAN' ) where rnk = 1`
- ex77\_ select의 서브 쿼리
  - 직업이 salesman인 사원들의 이름과 월급을 출력하면서 그 옆에 직업이 salesman인 사원들의 최대월급과 최소월급 출력
    `select ename, sal, (select max(sal) from emp where job='SALESMAN') max, (select min(sal) from emp where job='SALESMAN') min from emp where job='SALESMAN'`
  - 부서번호가 20번인 사원들의 이름과 월급을 출력하고 그 옆에 20번 부서번호인 사원들의 평균월급 출력
    `select ename, sal, (select avg(sal) from emp where deptno=20) avg from emp where deptno=20`
- ex78_insert
  - 사원 테이블에 데이터 추가
    `insert into emp(empno, ename, sal, job, hiredate) values (2812, 'JACK', 3500, 'ANALYST', to_date('2019/06/05', 'RRRR/MM/DD'));`
  - 부서 테이블에 데이터 추가
    `insert into dept(deptno, dname , loc) values (50, 'RESEARCH','SEOUL');`
- ex79_update
  - scott의 월급을 3200으로 수정
    `update emp set sal=3200 where ename='SCOTT';`
  - 직업이 salesman인 사원들의 커미션을 7000으로 수정
    `update emp set comm=7000 where job='SALESMAN';`
- ex80_delete truncate drop
  - scott의 데이터 삭제
    `delete from emp where ename='SCOTT';`
  - 월급이 3000이상인 사원들을 삭제
    `delete from emp where sal >= 3000`
  - delete : 데이터 삭제, 저장공간 유지, 저장구조 유지
  - truncate : 데이터 삭제, 저장공간 삭제, 저장구조 유지
  - drop : 데이터 삭제, 저장공간 삭제, 저장구조 삭제
- ex81_commit rollback
  - 데이터 입력 작업을 영구히 저장하거나 취소
  - 영구히 저장 : `commit`
  - 취소 : `rollback`
- ex82_merge
  - 사원테이블에서 부서위치 컬럼을 생성하고 부서테이블만 있는 부서번호를 사원테이블에 입력
    `merge into emp e using dept d on ( e.deptno = d.deptno ) when matched then update set e.loc=d.loc;`
  - 사원테이블에 부서명 컬럼을 추가하고 해당 사원의 부서명으로 값을 갱신
    `merge into emp e using dept d on (e.deptno = d.deptno) when matched then update set e.dname=d.dname;`
- ex83_lock
  - scott으로 접속한 창 2개를 열어놓은 상태에서 하나의 창에서 allen의 월급을 2000으로 수정하고 커밋을 안한 상태에서 다른 창에서 allen의 부서번호를 10번으로 수정하면 수정이 되겠는가?
  - 안된다.
- ex84_select for update
  - 부서번호가 10, 20번인 사원의 이름과 직업과 부서번호를 조회하는 동안 그 누구도 부서번호 10번, 20번인 사원들의 데이터를 갱신하지 못하도록 하세요
    `select ename, job, deptno from emp where deptno in (10, 20) for update`
- ex85\_서브쿼리
  - 사원 테이블과 같은 구조의 새로운 테이블을 생성하고 사원 테이블에서 부서번호가 10번인 사원들의 사원번호, 이름, 월급, 부서번호를 생성한 테이블에 입력
    `insert into emp2(empno, ename, sal, deptno) select empno, ename, sal, deptno from emp where deptno=10`
  - 부서 테이블과 같은 구조의 테이블을 dept2라는 이름으로 생성하고 부서번호가 20번 30번의 모든 컬럼의 데이터를 dept2에 입력
    `insert into dept2 select * from dept where deptno in (20,30)`
- ex86
  - 직업이 salesman인 사원들의 월급을 allen의 월급으로 수정
    `update emp set sal = ( select sal from emp where ename='ALLEN' ) where job = 'SALESMAN';`
  - 부서번호가 30번인 사원들의 직업을 martin의 직업으로 변경
    `update emp set job = ( select job from emp where ename='MARTIN' ) where deptno=30;`
- ex87
  - scott보다 더 많은 월급을 받는 사원들을 삭제
    `delete from emp where sal > (select sal from emp where ename='SCOTT');`
  - allen보다 늦게 입사한 사원들의 모든 행을 삭제
    `delete from emp where hiredate > (select hiredate from emp where ename='allen');`
- ex88
  - 부서테이블에 부서번호별 토탈월급 데이터가 입력
    `merge into dept d using ( select deptno, sum(sal) as sumsal from emp group by deptno ) v on ( d.deptno = v.deptno ) when matched then update set d.sumsal = v.sumsal;`
  - 부서테이블에 cnt라는 컬럼을 추가하고 해당 부서번호의 인원수로 값을 갱신
    `merge into dept d using ( select deptno, count(*) as cnt from emp group by deptno ) v on ( d.deptno = v.deptno ) when matched then update set d.cnt = v.cnt`
- ex89_level
  - 사원 테이블의 서열(level) 출력
    `select rpad(' ',level*3) || ename, level, sal, job from emp start with ename='KING' connect by prior empno=mgr;`
  - 서열 2위인 사원들의 이름과 서열과 직업 출력
    `select ename, level, sal, job from emp where level = 2 start with ename='KING' connect by prior empno=mgr`
- ex90
  - 서열 순서를 유지한 상태에서 blake와 blake 팀원들이 출력되지 않도록
    `select rpad(' ', level*3)||ename, level, sal, job from emp start with ename='KING' connect by prior empno=mgr and ename!='BLAKE'`
  - 사원 테이블에서 서열순서대로 이름과 서열과 월급과 직업을 출력하는데 scott과 scott의 팀원과 ford와 ford의 팀원들이 출력되지 않도록
    `select rpad(' ', level*3)||ename, level, sal, job from emp start with ename='KING' connect by prior empno=mgr and ename not in ('SCOTT', 'FORD')`
- ex91_siblings
  - 서열 순서를 유지한 상태에서 월급이 높은 순서대로 출력
    `select rpad(' ', level*3)||ename as employee, level, sal, job from emp start with ename='KING' connect by prior empno=mgr order siblings by sal desc`
  - blake와 blake의 팀원들만 출력하는데 서열을 유지한 상태에서 월급이 낮은 순서대로 출력
    `select rpad(' ', level*3)||ename as employee, level, sal, job from emp start with ename='BLAKE' connect by prior empno=mgr order siblings by sal asc`
- ex92_sys_connect_by_path
  - 자기의 서열순서가 어떻게 되는지 출력
    `select ename, sys_connect_by_path(ename,'/') as path from emp start with ename='KING' connect by prior empno = mgr`
  - 월급도 함께 나오게 출력
    `select ename, sys_connect_by_path(ename,'/')||'('||sal||')' as path from emp start with ename='KING' connect by prior empno = mgr`
- ex93_create
  - 오라클에 데이터를 저장할 테이블 생성
    `create table emp93 (empno number(10), ename varchar2(10), sal number(10, 2), hiredate date)`
  - 테이블 생성
    `create table emp50 (empno number(10), ename varchar2(10), sal number(10, 2), job varchar(10), deptno date)`
- ex94_on commit delete/preserve rows
  - 테이블을 만들고 데이터를 저장하는데 commit을 하면 데이터가 사라지도록
    `create global temporary table emp37 ( empno number(10), ename varchar2(10), sal number(10)) on commit delete rows;`
  - 세션을 종료하면 데이터가 사라지는 임시테이블을 다음과 같이 생성
    `create global temporary table emp94 ( empno number(10), ename varchar2(10), sal number(10) on commit preserve rows) `
- ex95_view
  - 사원 테이블에서 직업이 slaesman인 사원들의 사원번호, 사원이름, 직업, 관리자 번호, 부서번호만 바라볼 수 있는 view 생성
    `create view emp_view as select empno, ename, job, sal, deptno from emp where job = 'SALESMAN';`
  - 사원테이블에서 부서번호가 20번인 사원들의 사원번호와 사원이름, 직업, 월급을 볼 수 있는 view 생성
    `create view emp_view as select empno, ename, job, sal from emp where deptno=20;`
- ex96
  - 사원테이블에서 부서번호와 부서번호별 평균 월급만 바라볼 수 있는 view
    `create view emp_view2 as select deptno, round(avg(sal)) as avgsal from emp group by deptno; `
  - 직업, 직업별 토탈월급을 출력하는 view 생성
    `create view emp_view as select job, sum(job) as sumsal from emp group by job`
- ex97_index
  - 월급이 3000인 사원의 이름과 월급을 인덱스를 통해서 빠르게 검색
    `explain plan for select ename, sal from emp where sal = 3000;`
  - 사원 테이블에 직업에 인덱스 생성
    `create index emp_job on emp(job)`
- ex98_sequence
  - 사원번호에 번호를 입력할때 데이터가 중복되지 않고 순서대로 입력되게
    `create sequence seq2 start with 1 maxvalue 100 increment by 1 nocycle`
  - dept 테이블에 부서번호를 50번부터 입력하고 10씩 증가되는 시퀀스
    `create sequence dept_seq1 start with 50 increment by 10`
- ex99_flashback query
  - 사원 테이블을 지우기전인 5분전인 사원 테이블의 상태를 검색
    `select * from emp as of timestamp(systimestamp - interval '5' minute)`
  - 사원 테이블의 월급을 모두 0으로 변경하고 commit 한 후에 사원테이블을 1분전 상태로 되돌리시오
    `merge into emp e using (select empno, sal from emp as of timestamp(systimestamp - interval '1' minute)) s on (e.empno = s.empno) when matched then update set e.sal = s.sal;`
- ex100_flashback table
  - 사원 테이블을 지우기전 5분 전의 상태로 되돌리세요
    `flashback table emp to timestamp(systimestamp - interval '5' minute)`
  - 사원 테이블의 월급을 전부 0으로 변경하고 commit 한 다음에 사원 테이블의 월급을 전부 0으로 변경하기 전 상황으로 복구
    `flashback table emp to timestamp(systimestamp - interval '5' minute)`
- ex101_flashback drop
  - drop한 테이블 살리기
    `flashback table emp to before drop;`
  - dept 테이블을 drop하고 다시 복구하세요
    `flashback table dept to before drop;`
- ex102_flashback version query
  - 그동안 emp 테이블이 어떻게 변해왔는지 확인하고 싶다면
    `select ename, sal, deptno, versions_starttime, versions_endtime, versions_operation from emp versions between to_timestamp('21/08/11 13:21:10', 'RRRR-MM-DD HH24:MI:SS') and maxvalue where ename='KING' order by versions_starttime nulls first`
  - 부서 테이블의 부서위치를 전부 seoul로 변경하고 dept 테이블이 그동안 어떻게 변경되어왔는지 확인
    `select deptno, dname, loc, versions_starttime, versions_endtime, versions_operation from dept versions between to_timestamp('21/08/11 13:21:10', 'RRRR-MM-DD HH24:MI:SS') and maxvalue order by versions_starttime nulls first`
- ex103_flashback transaction query
  - 실수로 데이터를 지워서 다시 복구할 수 있는 스크립트를 구할 수 있다면?
- ex104_primary key
  - 사원번호에 중복된 데이터와 null 값을 입력 안되게 하려면
    `create table dept2 ( deptno number(10) constraint dept2_deptno_pk primary key, dname varchar(10), loc varchar2(10))` or `alter table dept add constraint dept_deptno_pk primary key(deptno)`
  - 사원 테이블의 empno에 primary key 생성
    `alter table emp add constraint emp_empno_pk primary key(empno)`
- ex105_unique
  - 사원번호에 중복된 데이터가 입력안되게 하려면
    `create table dept3 (deptno number(10), dname varchar(14) constraint dept3_dname_un unique, loc varchar2(10));` or `alter table dept4 add constraint dept4_dname_un unique(dname)`
  - 사원번호, 사원이름 ,월급, 직업을 담는 테이블을 아래와 같이 생성하는데 사원번호 컬럼에 중복된 데이터가 입력되지 않도록 제약을 걸어서 생성
    `create table emp1000 (empno number(10) constraint emp100_empno_un unique, ename varchar2(10), sal number(10), job varchar2(10))`
  - 사원 테이블에 사원번호에 중복된 데이터가 있는지 검색
    `select empno, count(*) from emp group by empno having count(*) >= 2`
  - 사원 테이블에 사원번호에 중복된 데이터가 입력되지 못하도록 제약
    `alter table emp add constraint emp_empno_un unique(empno)`
- ex106_not null
  - 사원 이름에 null이 입력 안되게 하려면
    `create table dept5 (deptno number(10), dname varchar(14), loc varchar2(10) constraint dept5_loc_nn not null)` or `alter table dept5 modify loc constraint dept5_loc_nn not null`
  - 사원 테이블에 사원이름에 null 값이 몇건 존재하는지 검색
    `select count(*) from emp where ename is null`
  - 사원 테이블에 사원이름에 not null 제약을 거세요
    `alter table emp modify ename constraint emp_ename_nn not null`
  - 부서 테이블에 부서번호에 not null 제약을 거세요
    `alter table dept modify deptno constraint dept_deptno_nn not null`
- ex107_check
  - 월급 컬럼에 9000보다 큰 월급은 입력되지 못하게 하려면
    `create table emp6 (empno number(10), ename varchar2(20), sal number(10) constraint emp6_sal_ck check (sal between 0 and 9000))` or `alter table emp add constraint emp_sal_ck check(sal between 0 and 9000)`
  - 제약 삭제
    `alter table emp6 drop constraint emp6_sal_ck`
  - 사원 테이블의 부서번호에 부서번호가 10, 20, 30번만 입력 제약
    `alter table emp add constraint emp_deptno_ck check(deptno in (10, 20, 30))`
  - 부서 테이블의 부서위치에 new york, dallas, chicago, boston만 입력 수정
    `alter table dept add constraint dept_loc_ck check(loc in ('NEW YORK', 'DALLAS', 'CHICAGO', 'BOSTON'))`
  - 사원 테이블에 이메일 컬럼을 다음과 같이 추가하고 이메일에 @가 있어야지만 데이터가 입력 수정
    `alter table emp add constraint emp_email_ck check(email like '%@%')`
- ex108_foreign key
  - 부서 테이블에 있는 부서번호만 사원 테이블에 입력
    - `create table dept7 (deptno number(10) constraint dept7_deptno_pk primary key, dname varchar(14), loc varchar2(10))`
    - `create table emp7 (empno number(10), ename varchar2(20), sal number(10), deptno number(10) constraint emp7_deptno_fk references dept7(deptno))`
    - `alter table dept7 add constraint dept7_deptno_pk cascade;`
  - 사원 테이블에 empno 에 primary key 설정
    `alter table emp add constraint emp_empno_pk primary key(empno)`
  - 사원 테이블에 관리자번호에 forein key 제약을 걸고 사원 테이블에 있는 컬럼을 참조하게 하여 관리자 번호가 사원 테이블에 있는 사원번호에 해당하는 사원들만 관리자 번호로 입력 또는 수정
    `alter table emp add constraint emp_empno_fk foreign key(mgr) references emp(empno)`
- ex109_with as
  - 시간이 오래걸리는 무거운 쿼리문이 하나의 쿼리문에서 반복 사용된다면
    `with job_sumsal as (select job, sum(sal) as 토탈 from emp group by job) select job, 토탈 from job_sumsal where 토탈 > (select avg(토탈) from job_sumsal)`
  - 부서번호별 토탈월급을 출력하는데 부서번호별 토탈월급들의 평균값보다 더 큰것만 출력
    `with job_sumsal as (select job, sum(sal) as 토탈 from emp group by job) select job, 토탈 from job_sumsal where 토탈 > (select avg(토탈) from job_sumsal)`
  - 부서위치, 부서위치별 토탈월급을 출력하는데 부서위치별 토탈월급의 평균값보다 더 큰 것만 출력
    `with loc_sumsal as (select d.loc, sum(e.sal) as 토탈 from emp e join dept d on (e.deptno = d.deptno) group by d.loc) select loc, 토탈 from loc_sumsal where 토탈 > (select avg(토탈) from loc_sumsal)`
- ex110_subquery factoring
  - `select deptno, sum(sal) from (select job, sum(sal) 토탈 from emp group by job) as job_sumsal, (select deptno, sum(sal) 토탈 from emp group by deptno having sum(sal) > (select avg(토탈) + 3000 from job_sumsal))` => 불가능
  - 입사한 년도와 입사한 년도별 토탈 월급을 출력하는데 부서번호별 토탈월급들의 평균값보다 더 큰것만 출력
    `with deptno_sumsal as (select deptno, sum(sal) 토탈 from emp group by deptno), hire_sumsal as (select to_char(hiredate, 'RRRR') hire_year, sum(sal) 토탈 from emp group by to_char(hiredate, 'RRRR') having sum(sal) > (select avg(토탈) from deptno_sumsal)) select hire_year, 토탈 from hire_sumsal`
