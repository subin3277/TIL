# A505 김수빈 230109

# Vue2와 Vue 3의 차이점

### Fragments
* fragments :  다중 루트 노드 컴포넌트를 의미.
* Vue2
``` vue
<template>
  <div>
    <h1>hello world!</h1>
  </div>
</template>
```
template 태그 안에 div 태그 작성후 그 안에 원하는 태그를 사용 가능했다.
* Vue3
``` vue
<template>
  <h1>hello world!</h1>
</template>
```
vue3에서는 div 태그없이 template 태그 안에서 바로 사용이 가능하다!!!!

### Emit
* Vue2에서는 그냥 emit을 사용하면 되었다.
* Vue3에서는 emit을 정의하는 부분이 존재한다.
* props처럼 객체 형식으로 선언하여, 더 구체적으로 검사 할 수 있다.

### CSS 변수
* Vue2
  * style에 대해 변수로 사용하고 싶으면 html 코드에 style 태그를 추가하여 사용했어야한다.
  * html, css, javascript를 분리하여 관리하는 vue의 컨셉에 맞지안흔 방법이었다.
* Vue 3
  * template에서 정의한 변수를 css에 그대로 사용할 수 있다.

### v-model
* Vue3
  * props -> modelValue
  * emit -> update:modelValue
  * 하나의 컴포넌트가 여러개의 v-model을 가질 수 있다.

### v-for, v-if
* Vue2
  * v-for, v-if에 key를 사용해야했다.
* Vue3
  * key를 자동으로 생성해준다.

### Computed
* Vue2
  * computed 블록 안에 계산 될 값들을 넣어야한다.
* Vue2
  * setup()안에서 변수 선언시 `computed(()=> {return _});`

### Composition API
* Vue2 : Options API
* Vue3 : Composition API