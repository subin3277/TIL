# JSP

## MVC 패턴

- Model View Controller
- Seperation of Responsibility 책임의 분리
- Model : 데이터 - Java (value object, DTO, Service object, data access object...)
- View : 화면 - html, JSP
- Controller : 중재, View와 Model간의 연결 - Servlet

## JDBC / My Batiss / JPA

- JDBC : Java Database Connectivity - J2SE 표준스펙
  - JDBD 구현체는 DB Vendor가 작성
- My Batis : JDBC 확장, xml에 sql문 작성
- JPA : Java Persistence API - J2EE 표준스펙
  - Hibernate 하이버네이트 - JPA 구현체
- J2SE vs J2EE
  - J2SE : stand alone program
  - J2EE : server based program
- Servlet vs JSP
  - Servlet
    - Java 코드 내부에 html 코드를 포함 할 수 있다
  - JSP
    - html에 Java 코드를 포함 할 수 있다

## JSP(Java Server Page)

- Template Page
  - HTML내에 코드를 포함하는 방법
  - PHP : Apache -> Apache에서만 동작
  - ASP(Active Server Page) : MS -> IIS에서만 동작
  - JSP(Java Server Page) : Sun Microsystems -> 웹서버 독립적
- JSP
  - JSP 코드를 포함하는 HTML
  - JSP page는 Web Container에 의해 서블릿 인스턴스로 변환 되며, 변환된 서블릿은 해당 JSP page에 대한 요청을 처리
  - ASP나 PHP는 HTTP 요청이 들어올 때 마다 interpret 되는 반면, JSP는 Java bytecode로 컴파일
- JSP 장점
  - OS의 쉘이나 프로세스가 아닌 스레드가 사용되기 때문에 웹 응용프로그램의 성능과 확장성이 있다
  - Java를 기반으로 하기 때문에 Platform independent하다
  - Java 언어로 작성되기 때문에 객체지향언어와 모든 API를 사용할 수 있다
- 단점
  - Presentation logic과 Business logic을 같이 포함하는 경우가 있다
  - 동시성 문제를 고려해야한다
  - 디버깅이 어렵다

### 구조
- userDAO (Data Access Object) -> Model
  - JDBC 사용
  - DB 연동
- userVO (value Object) -> Model
  - 값을 웹상에 뿌려주기 위한 객체
- index.jsp, UserList.jsp -> View
  - Entry 역할
- UserListServlet -> Controller
  - Presentation Layer
  - init, goGet, destroy : life cycle