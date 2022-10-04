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
* REAL : 
* TEXT
* BLOB