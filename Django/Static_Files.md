# Managing static files

## Static files(정적 파일)
* 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
* 파일 자체가 고정되어있고, 서비스 중에도 추가되거나 변경되지않고 고정

## Media File
* 미디어 파일
* 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
* 유저가 업로드 한 모든 정적 파일

## Django에서 정적파일 구성하고 사용하기
1. `INSTALLED_APPS`에 `django.contrib.staticfiles`가 포함되어있는지 확인하기
2. settings.py에 `STATIC_URL`을 정의
3. 앱의 static 폴더에 정적 파일을 위치
4. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기
    * `{% load %}` : load tag, 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드
    * `{% static '' %}` : static tag, STATIC_ROOT에 저장된 정적 파일에 연결

# IMAGEFIELD
## ImageField
* 이미지 업로드에 사용하는 모델 필드
* FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용가능
* 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
* ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경할 수 있음

## FileField
* `FileField(upload_to='', storage=None, max_length=100, **options)`
* 파일 업로드에 사용하는 모델 필드
* `upload_to`, `storage` 2개의 인자를 가지고 있음

## ImageField, FileField 사용하기 위한 단계
1. settings.py에 `MEDIA_ROOT`, `MEDIA_URL` 설정
2. `upload_to` 속성을 정의하여 업로드 된 파일에 사용한 MEDIA_ROOT의 하위 경로를 지정(선택)