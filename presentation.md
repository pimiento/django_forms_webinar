- [HTML](#orgf415eae)
- [Django templates](#orgaeb56cb)
- [наследование](#orgacdb27b)
- [передача переменных](#org3b2372a)
- [Дополнительная литература](#org0a08c2b)
- [HTML формы](#orgddead79)
- [HTML формы](#orgd993e9a)
- [HTML формы](#orgef5e15d)
- [Django формы](#org427e979)
- [Django формы](#org33ff481)
- [Django формы](#org7d30b3d)
  - [<span class="underline">[Form Fields](https://docs.djangoproject.com/en/3.2/ref/forms/fields/#built-in-field-classes)</span>](#org25cc5a4)
- [Bound / Unbond forms](#org400b78d)
- [Unbound](#org7d55449)
- [Bound](#orgb21ce35)
- [Валидация форм](#orga81b012)
- [Валидаторы](#orgf56f52f)
- [Валидаторы](#orgad0f1b2)
- [Валидаторы](#orgf569918)
- [Forms Workflow](#org5e149c9)
- [Рендеринг форм вручную](#orgf531c54)
- [Безопасность](#org18c125f)
- [CSRF](#org6f271c2)
- [CSRF](#orgfcb5582)
- [CSRF](#orgd05e572)
- [ModelForm](#org1736d18)
- [ModelForm](#orgac07945)
- [ModelForm](#orgb90f418)
  - [save(commit=False)](#org244efb3)
- [ModelForm](#org2bd1449)
- [ModelForm](#orgade968f)
- [ModelForm](#org3928e11)
- [ModelForm](#org7d3063b)
- [ModelForm](#orge823e93)
- [Widgets](#orgde7ad8b)
- [Widgets](#org388c054)
- [Widgets](#org71b67f9)
- [Widgets](#org86831b8)
- [Вопросы-ответы](#orgf4f438c)



<a id="orgf415eae"></a>

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


<a id="orgaeb56cb"></a>

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


<a id="orgacdb27b"></a>

# наследование

-   **extends:** взять за основу *расширяемый шаблон* и *переопределить* в нём нужные блоки. Остальное содержимое шаблона останется прежним.
-   **include:** вставить на место **{% include &#x2026; %}** содержимое подключаемого шаблона.


<a id="org3b2372a"></a>

# передача переменных

-   В шаблоне доступны объекты из middleware, например [user](https://docs.djangoproject.com/en/4.0/topics/auth/default/#authentication-data-in-templates)
-   Нужные вам переменные вы передаёте из вьюхи во [время рендеринга](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#render)


<a id="org0a08c2b"></a>

# Дополнительная литература

-   <https://docs.djangoproject.com/en/2.2/ref/templates/builtins/>
-   <https://docs.djangoproject.com/en/2.2/topics/templates/>
-   <https://habr.com/ru/post/23132/?ysclid=l2hw076rbl>


<a id="orgddead79"></a>

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


<a id="orgd993e9a"></a>

# HTML формы

Формы могут быть более красивыми

![img](html_form1.jpg)


<a id="orgef5e15d"></a>

# HTML формы

И очень разнообразными. Но писать такие разнообразные формы вручную это очень утомительно. На помощь нам приходят [**Django Forms**](https://docs.djangoproject.com/en/3.2/topics/forms/).

![img](html_form.png)


<a id="org427e979"></a>

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


<a id="org33ff481"></a>

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


<a id="org7d30b3d"></a>

# Django формы


<a id="org25cc5a4"></a>

## <span class="underline">[Form Fields](https://docs.djangoproject.com/en/3.2/ref/forms/fields/#built-in-field-classes)</span>

Поля формы в Django описываются классами Field, каждый из которых имеет своё представление в виде Widget-а.
![img](builtin_fields.png)


<a id="org400b78d"></a>

# Bound / Unbond forms

Формы в *Django* **[могут быть в двух состояних](https://docs.djangoproject.com/en/3.2/ref/forms/api/#bound-and-unbound-forms)**

-   **unbound:** — форма пустая
-   **bound:** — форма заполнена данными


<a id="org7d55449"></a>

# Unbound

Форма не связана ни с какими данными

```python
form = MessageForm()
form.is_bound   # -> False
```


<a id="orgb21ce35"></a>

# Bound

Форма *частично* или *полностью* заполнена

```python
# обычно мы передаём request.POST
form = MessageForm({
    'message': 'foobar'
})
form.is_bound   # -> True
```


<a id="orga81b012"></a>

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


<a id="orgf56f52f"></a>

# Валидаторы

Пример написания своего валидатора

```python
from django.core.exceptions import (
    ValidationError
)

def validate_even(value):
    if value % 2 != 0:
        raise Validationerror(
            '%(value) нечётно',
            params={'value': value}
        )
```


<a id="orgad0f1b2"></a>

# Валидаторы

```python
from django import forms

class EvenNumbersForm(forms.Form):
    number = forms.IntegerField(
        validators=[validate_even]
    )
```

*validators* добавит валидаторы к уже существующему базовому валидатору *IntegerField*


<a id="orgf569918"></a>

# Валидаторы

[**Готовых валидаторов очень много!**](https://docs.djangoproject.com/en/3.2/ref/validators/)

![img](validators.png)


<a id="org5e149c9"></a>

# Forms Workflow

![img](form_handling_-_standard.png)


<a id="orgf531c54"></a>

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


<a id="org18c125f"></a>

# Безопасность

[**Настоятельно рекомендую ознакомиться с этой документацией**](https://docs.djangoproject.com/en/3.2/topics/security/)
\newline
<https://docs.djangoproject.com/en/3.2/topics/security/>


<a id="org6f271c2"></a>

# CSRF

На сайте может быть обычная кнопка, предлагающая вам посмотреть фотографии.

![img](csrf.png)


<a id="orgfcb5582"></a>

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


<a id="orgd05e572"></a>

# CSRF

Но если на стороне банка используются csrf-токены в формах, то ничего страшного не случится. Запрос злоумышленника не может содержать нужное значение (случайное в рамках сессии) csrf-токена.

```html
<form method="post"
      action="{% url signup %}">
  {% csrf_token %}
</form>
```

![img](csrf_html.png)


<a id="org1736d18"></a>

# ModelForm

[**Прекрасная документация**](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/)


<a id="orgac07945"></a>

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


<a id="orgb90f418"></a>

# ModelForm


<a id="org244efb3"></a>

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


<a id="org2bd1449"></a>

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


<a id="orgade968f"></a>

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


<a id="org3928e11"></a>

# ModelForm

Или использовать *commit=False* чтобы доопределить модель перед записью в БД.

```python
form = YaForm(request.POST)
model = form.save(commit=False)
model.Z = 'foobar'
model.save()
```


<a id="org7d3063b"></a>

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


<a id="orge823e93"></a>

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


<a id="orgde7ad8b"></a>

# Widgets

Виджеты это то как формы будут представлены на web-страницы, то есть виджеты отвечают за генерацию HTML-кода для полей форм.
**[Документация](https://docs.djangoproject.com/en/3.2/ref/forms/widgets/)**

![img](widgets.png)


<a id="org388c054"></a>

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


<a id="org71b67f9"></a>

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


<a id="org86831b8"></a>

# Widgets

```html
<input type="text" name="name"
       class="special" required>

<input type="url" name="url"
       required>

<input type="text" name="comment"
       size="40" required>
```


<a id="orgf4f438c"></a>

# Вопросы-ответы

![img](questions.jpg)
