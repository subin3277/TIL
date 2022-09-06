# ModelForm

## ModelForm
* Model을 통해 Form Class를 만들 수 있는 helper class
* ModelForm은 Form과 똑같은 방식으로 View 함수에서 사용

## ModelForm 선언
* forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음
* 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
* 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

## Meta data
* 데이터를 표현하기 위한 데이터
* EX) 사진파일 = 사진 데이터 + 사진 데이터의 데이터(= 사진의 Meta date)(촬영 시각, 렌즈 값, 조리개 값 등..)

## CREATE
* 유효성 검사를 통과하면 데이터 저장 후, 상세 페이지로 리다이렉트
* 통과하지 못하면 작성 페이지로 리다이렉트
``` python
# articles/views.py
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    return redirect('articles:new')
```
* `is_valid()` method
    * 유효성 검사를 실행하고 데이터가 유효한지 여부를 boolean으로 반환
    * 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 is_valid()를 제공

## UPDATE
* ModelForm의 인자 instance는 수정 대상이 되는 객체를 지정
* request.POST : 사용자가 form을 통해 전송한 데이터(새로운 데이터)\
* instance : 수정이 되는 대상

## Form vs ModelForm
* 두가지는 각자 역할이 다른것
* Form
    * 사용자로부터 받는 데이터가 DB와 연관되어 있지 않는 경우에 사용
    * DB에 영향을 미치지 않고 단순 데이터만 사용되는 경우
    * EX) 로그인
* ModelForm
    * 사용자로부터 받는 데이터가 DB와 연관되어 있는 경우
    * 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야할지 이미 알고 있기 때문에 곧바로 `save()` 호출이 가능