- [HTML](#org14f6224)
- [Django templates](#org63e2c3d)
- [наследование](#org6b5fbc1)
- [передача переменных](#orgd5dd604)
- [Дополнительная литература](#org12a79ad)
- [HTML формы](#org77ac8b1)
- [HTML формы](#org6c71764)
- [HTML формы](#org900b7d3)
- [Django формы](#orgbb7f754)
- [Django формы](#org4cd64af)
- [Django формы](#org9dba36d)
  - [<span class="underline">[Form Fields](https://docs.djangoproject.com/en/3.2/ref/forms/fields/#built-in-field-classes)</span>](#orgac68da6)
- [Bound / Unbond forms](#org0e55fca)
- [Unbound](#org1add42b)
- [Bound](#org057de00)
- [Валидация форм](#orgc2e5ec6)
- [Валидаторы](#org9871f1d)
- [Валидаторы](#org3eb238c)
- [Валидаторы](#org104482b)
- [Forms Workflow](#orge81f6b6)
- [Рендеринг форм вручную](#org07e02fc)
- [Безопасность](#org24c12dd)
- [CSRF](#org2630e63)
- [CSRF](#org30870a8)
- [CSRF](#org6013a39)
- [ModelForm](#orgddbf278)
- [ModelForm](#orgd96d77c)
- [ModelForm](#org518a4e7)
  - [save(commit=False)](#orgf065cef)
- [ModelForm](#orga2665f4)
- [ModelForm](#org7774f3f)
- [ModelForm](#org5c6ee02)
- [ModelForm](#orgc317505)
- [ModelForm](#org01c8a59)
- [Widgets](#orgcdf5f16)
- [Widgets](#org365744e)
- [Widgets](#orgac53e1e)
- [Widgets](#org62c3f30)
- [Немного практики](#org47d97eb)
- [Вопросы-ответы](#org24c1521)



<a id="org14f6224"></a>

# HTML

```html
<html>
  <head>
    <title>Мир! Труд! Май!</title>
  </head>
  <body>
    <center
      onclick="alert('привет!')"
      style="color:red;font-size:40px"
    >
      <!-- тут нужно вставить своё имя -->
      <i>Привет, &lt;ИМЯ&gt;!</i>
    </center>
  </body>
</html>
```


<a id="org63e2c3d"></a>

# Django templates

```html
<html>
  <head>
    <title>Мир! Труд! Май!</title>
  </head>
  <body>
    <center
      onclick="alert('привет!')"
      style="color:red;font-size:40px"
      >
      <i>Привет, {{ name }}!</i>
    </center>
  </body>
</html>
```


<a id="org6b5fbc1"></a>

# наследование

-   **extends:** взять за основу *расширяемый шаблон* и *переопределить* в нём нужные блоки. Остальное содержимое шаблона останется прежним.
-   **include:** вставить на место **{% include &#x2026; %}** содержимое подключаемого шаблона.


<a id="orgd5dd604"></a>

# передача переменных

-   В шаблоне доступны объекты из middleware, например [user](https://docs.djangoproject.com/en/4.0/topics/auth/default/#authentication-data-in-templates)
-   Нужные вам переменные вы передаёте из вьюхи во [время рендеринга](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#render)


<a id="org12a79ad"></a>

# Дополнительная литература

-   <https://docs.djangoproject.com/en/2.2/ref/templates/builtins/>
-   <https://docs.djangoproject.com/en/2.2/topics/templates/>
-   <https://habr.com/ru/post/23132/?ysclid=l2hw076rbl>


<a id="org77ac8b1"></a>

# HTML формы

[**HTML-формы**](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form) это просто текст. И вообщем-то мы можем писать его вручную или, например, с использованием f-string в Python.  

```html
<form action="." method="post">
 <label for="message">Послание</label>
 <input type='text' name="message"
        value="сообщение"
        maxlength="100" />
 <input type="submit"
       value="Отправить" />
</form>
```

![img](simple_html_form.png)  


<a id="org6c71764"></a>

# HTML формы

Формы могут быть более красивыми  

![img](html_form1.jpg)  


<a id="org900b7d3"></a>

# HTML формы

И очень разнообразными. Но писать такие разнообразные формы вручную это очень утомительно. На помощь нам приходят [**Django Forms**](https://docs.djangoproject.com/en/3.2/topics/forms/).  

![img](html_form.png)  


<a id="orgbb7f754"></a>

# Django формы

```python
from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(
        label='Послание',
        max_length=100
    )

form = MessageForm(
    initial={'message': 'сообщение'}
)
```

*initial* заполнит форму какими-то данными. При рендеринге это будет значение атрибута *value* в HTML. Обычно мы передаём туда *request.POST*  


<a id="org4cd64af"></a>

# Django формы

```html
<tr>
  <th>
    <label for="id_message">
      Послание:
    </label>
  </th>
  <td>
    <input type="text"
           name="message"
           value="сообщение"
           maxlength="100"
           required
           id="id_message" />
  </td>
</tr>
```


<a id="org9dba36d"></a>

# Django формы


<a id="orgac68da6"></a>

## <span class="underline">[Form Fields](https://docs.djangoproject.com/en/3.2/ref/forms/fields/#built-in-field-classes)</span>

Поля формы в Django описываются классами Field, каждый из которых имеет своё представление в виде Widget-а.  
![img](builtin_fields.png)  


<a id="org0e55fca"></a>

# Bound / Unbond forms

Формы в *Django* **[могут быть в двух состояних](https://docs.djangoproject.com/en/3.2/ref/forms/api/#bound-and-unbound-forms)**  

-   **unbound:** — форма пустая
-   **bound:** — форма заполнена данными


<a id="org1add42b"></a>

# Unbound

Форма не связана ни с какими данными  

```python
form = MessageForm()
form.is_bound   # -> False
```


<a id="org057de00"></a>

# Bound

Форма *частично* или *полностью* заполнена  

```python
# обычно мы передаём request.POST
form = MessageForm({
    'message': 'foobar'
})
form.is_bound   # -> True
```


<a id="orgc2e5ec6"></a>

# Валидация форм

[**Документация**](https://docs.djangoproject.com/en/3.2/ref/forms/validation/)  

```python
form.is_valid()  # -> True / False
# в случае когда is_valid -> True,
# тогда у формы появляется атрибут
# cleaned_data, который содержит
# словарь со значениями полей
form.cleaned_data['field_name']
# если is_valid -> False
# то заполняется переменная
form.errors
```


<a id="org9871f1d"></a>

# Валидаторы

Пример написания своего валидатора  

```python
from django.core.exceptions import (
    ValidationError
)

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value) нечётно',
            params={'value': value}
        )
```


<a id="org3eb238c"></a>

# Валидаторы

```python
from django import forms

class EvenNumbersForm(forms.Form):
    number = forms.IntegerField(
        validators=[validate_even]
    )
```

*validators* добавит валидаторы к уже существующему базовому валидатору *IntegerField*  


<a id="org104482b"></a>

# Валидаторы

[**Готовых валидаторов очень много!**](https://docs.djangoproject.com/en/3.2/ref/validators/)  

![img](validators.png)  


<a id="orge81f6b6"></a>

# Forms Workflow

![img](form_handling_-_standard.png)  


<a id="org07e02fc"></a>

# Рендеринг форм вручную

-   <span class="underline"><span class="underline">[Статья](https://www.geeksforgeeks.org/render-django-form-fields-manually/)</span></span>
-   <span class="underline"><span class="underline">[оф. документация](https://docs.djangoproject.com/en/4.0/topics/forms/#rendering-fields-manually)</span></span>

```html
{{ form.non_field_errors }}
<div class="fieldWrapper">
    {{ form.subject.errors }}
    <label
     for="{{form.subject.id_for_label}}" />
    >
      Email subject:
    </label>
    {{ form.subject }}
</div>
```


<a id="org24c12dd"></a>

# Безопасность

[**Настоятельно рекомендую ознакомиться с этой документацией**](https://docs.djangoproject.com/en/3.2/topics/security/)  
\newline  
<https://docs.djangoproject.com/en/3.2/topics/security/>  


<a id="org2630e63"></a>

# CSRF

На сайте может быть обычная кнопка, предлагающая вам посмотреть фотографии.  

![img](csrf.png)  


<a id="org30870a8"></a>

# CSRF

А на самом деле там будет отправляться форма перевода денег с вашего аккаунта на аккаунт злоумышленника.  

```html
<form
  action="bank.com/transfer.do"
  method="POST">
  <input type="hidden"
         name="acct" value="воришка"/>
  <input type="hidden"
         name="amount" value="$1kk"/>
  <input type="submit"
         value="View my pictures!"/>
</form>
```


<a id="org6013a39"></a>

# CSRF

Но если на стороне банка используются csrf-токены в формах, то ничего страшного не случится. Запрос злоумышленника не может содержать нужное значение (случайное в рамках сессии) csrf-токена.  

```html
<form method="post"
      action="{% url signup %}">
  {% csrf_token %}
</form>
```

![img](csrf_html.png)  


<a id="orgddbf278"></a>

# ModelForm

[**Прекрасная документация**](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/)  


<a id="orgd96d77c"></a>

# ModelForm

У ModelForm появляется метод **.save()**  

```python
class NameForm(models.ModelForm):
    class Meta:
        model = Name

form = NameForm(request.POST)
# сохранить запись в базу данных
form.save()
```


<a id="org518a4e7"></a>

# ModelForm


<a id="orgf065cef"></a>

## save(commit=False)

```python
class NameForm(models.ModelForm):
    class Meta:
        model = Name

form = NameForm(request.POST)
# создаёт объект модели Name
# но не записываем его в базу
model = form.save(commit=False)
```


<a id="orga2665f4"></a>

# ModelForm

```python
class YaForm(models.ModelForm):
    class Meta:
        # содержит поля X, Y, Z
        model = YaModel
        fields = ['X', 'Y']

form = YaForm(request.POST)
# не передаст в модель Z,
# а значит в базу запишется
# пустое значение поля Z
from.save()
```


<a id="org7774f3f"></a>

# ModelForm

Один из вариантов решения — определить модель заранее  

```python
model = YaModel(Z='foobar')
form = YaForm(
    request.POST,
    instance=model
)
# форма будет содержать все
# поля заполненными
form.save()
```


<a id="org5c6ee02"></a>

# ModelForm

Или использовать *commit=False* чтобы доопределить модель перед записью в БД.  

```python
form = YaForm(request.POST)
model = form.save(commit=False)
model.Z = 'foobar'
model.save()
```


<a id="orgc317505"></a>

# ModelForm

Допустим, мы определили модель  

```python
class Article(models.Model):
  headline = models.CharField(
    max_length=200,
    null=True,
    blank=True,
  )
  content = models.TextField()
```


<a id="org01c8a59"></a>

# ModelForm

Если поле не перечислено в *fields* или добавлено в *excludes* в Meta-классе, то это поле будет исключено из данных передаваемых в модель.  

```python
class ArticleForm(ModelForm):
  slug = CharField(
    validators=[validate_slug]
  )

  class Meta:
    model = Article
    # slug не попадёт в save()
    fields = ['headline', 'content']
```


<a id="orgcdf5f16"></a>

# Widgets

Виджеты это то как формы будут представлены на web-страницы, то есть виджеты отвечают за генерацию HTML-кода для полей форм.  
**[Документация](https://docs.djangoproject.com/en/3.2/ref/forms/widgets/)**  

![img](widgets.png)  


<a id="org365744e"></a>

# Widgets

Можно добавлять стили и другие атрибуты виджетам  

```python
class CommentForm(forms.Form):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={'class': 'special'}
    )
  )
  url = forms.URLField()
  comment = forms.CharField(
    widget=forms.TextInput(
      attrs={'size': '40'}
    )
  )
```


<a id="orgac53e1e"></a>

# Widgets

```python
class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = (
      'name', 'url', 'comment'
    )
    widgets = {
      'name': forms.TextInput(
        attrs={'class': 'special', 'rows': 20}
      ),
      'comment': forms.TextInput(
        attrs={'size': '40'}
      )
    }
```


<a id="org62c3f30"></a>

# Widgets

```html
<input type="text" name="name"
       class="special" required>

<input type="url" name="url"
       required>

<input type="text" name="comment"
       size="40" required>
```


<a id="org47d97eb"></a>

# Немного практики

-   <span class="underline"><span class="underline">[Примеры](https://docs.djangoproject.com/en/2.2/ref/forms/widgets/)</span></span>
-   <span class="underline"><span class="underline">[Ещё примеры](https://www.javatpoint.com/django-form-widget)</span></span>
-   <span class="underline"><span class="underline">[django-colorfield](https://pypi.org/project/django-colorfield/)</span></span>


<a id="org24c1521"></a>

# Вопросы-ответы

![img](questions.jpg)
