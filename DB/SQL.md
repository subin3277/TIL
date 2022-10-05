# SQL

## SQL(Structured Query Language)
* RDBMS의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
* RDBMS에서 데이터베이스 스키마를 생성 및 수정할 수 있으며, 테이블에서의 자료 검색 및 관리도 가능
* 데이터베이스 객체에 대한 처리를 관리하거나 접근 권한을 설정하여 허가된 사용자만 RDBMS를 관리할 수 있도록 할 수 있음
* 많은 데이터베이스 관련 프로그램들이 SQL을 표준으로 채택하고 있음

## Commands
* DDL (Data Definition Language) : 데이터 정의 언어. 관계형 데이터베이스 구조를 정의(생성, 수정, 삭제)하기 위한 명령어(CREATE, DROP, ALTER)
* DML (Data Manipulation Language) : 데이터 조작 언어. 데이터를 조작(추가, 조회, 변경, 삭제)하기 위한 명령어(INSERT, SELECT, UPDATE, DELETE)
* DCL (Data Control Language) : 데이터 제어 언어. 데이터의 보안, 수행제어, 사용자 권한 부여등을 정의하기 위한 명령어

## SQL 구조
* 모든 SQL문은 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작하고, 세미콜론(;)으로 끝남
* 키워드는 대소문자를 구분하지 않음(하지만 대문자로 작성 권장)

## DDL
* CREATE
``` sql
CREATE TABLE table_name (
    column_1 data_type constraints,
    column_2 data_type constraints,
    column_3 data_type constraints
);
```

## 데이터 타입
* NULL : NULL value, 정보가 없거나 알 수 없음을 의미
* INTEGER : 정수, 크기에 따라 0, 1, 2, 3, 4, 6, 8 바이트와 같은 가변 크기를 가짐
* REAL : 실수, 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
* TEXT : 문자 데이터
* BLOB : 입력된 그대로 저장도니 데이터 덩어리. 바이너리 등 멀티미디어 파일. 이미지 데이터 등...
* Boolena type은 없음

## Constraints 종류
* NOT NULL : 컬럼이 NULL 값을 허용하지 않도록 지정, 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용함
* UNIQUE : 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
* PRIMARY KEY : 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼. 각 테이블에는 하나의 기본 키만 있음. 암시적으로 NOT NULL 제약 조건이 포함되어있음
* AUTOINCREMENT : 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지. INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함.

## ALTER TABLE
* rename a table
`ALTER TABLE table_name RENAME TO new_table_name;`
* rename a column
`ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;`
* add a new column to a table
`ALTER TABLE table_name ADD COLUMN column_definition;`
* delete a column
`ALTER TABLE table_name DROP COLUMN cloumn_name;`

## DROP TABLE
* remove a table
`DROP TABLE table_name;`