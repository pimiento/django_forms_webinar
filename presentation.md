- [HTML](#org43f11c4)
- [Django templates](#orgc4feea3)
- [наследование](#org3c0f6cd)
- [передача переменных](#org8264eed)
- [Дополнительная литература](#org413114e)
- [HTML формы](#org716c477)
- [HTML формы](#orgf1e673c)
- [HTML формы](#org6717bac)
- [Django формы](#org16aea23)
- [Django формы](#org40587c0)
- [Django формы](#orgcef109d)
  - [<span class="underline">[Form Fields](https://docs.djangoproject.com/en/3.2/ref/forms/fields/#built-in-field-classes)</span>](#orgc54d0cf)
- [Bound / Unbond forms](#org708b9bb)
- [Unbound](#org3b0da2d)
- [Bound](#org49028c2)
- [Валидация форм](#org1760a0d)
- [Валидаторы](#orgd188b0d)
- [Валидаторы](#orge973c75)
- [Валидаторы](#orgb139fdc)
- [Forms Workflow](#org5a57091)
- [Рендеринг форм вручную](#orgc6fad71)
- [Безопасность](#org60659fe)
- [CSRF](#orgd74a23c)
- [CSRF](#org8d8099c)
- [CSRF](#orgbbeffdb)
- [ModelForm](#orgabdc09b)
- [ModelForm](#orgd9f3b85)
- [ModelForm](#orgeb77d6d)
  - [save(commit=False)](#orgd886cff)
- [ModelForm](#org6ebb86b)
- [ModelForm](#orgfd483c4)
- [ModelForm](#org3bc3d2c)
- [ModelForm](#orgda73e0c)
- [ModelForm](#org09ce08b)
- [Widgets](#orgc25e9a9)
- [Widgets](#orgb534cd3)
- [Widgets](#org46e0ddf)
- [Widgets](#org6653484)
- [Вопросы-ответы](#orgd223e76)



<a id="org43f11c4"></a>

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


<a id="orgc4feea3"></a>

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


<a id="org3c0f6cd"></a>

# наследование

-   **extends:** взять за основу *расширяемый шаблон* и *переопределить* в нём нужные блоки. Остальное содержимое шаблона останется прежним.
-   **include:** вставить на место \({% include ... %}\) содержимое подключаемого шаблона.


<a id="org8264eed"></a>

# передача переменных

-   В шаблоне доступны объекты из middleware, например [user](https://docs.djangoproject.com/en/4.0/topics/auth/default/#authentication-data-in-templates)
-   Нужные вам переменные вы передаёте из вьюхи во [время рендеринга](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#render)


<a id="org413114e"></a>

# Дополнительная литература

-   <https://docs.djangoproject.com/en/2.2/ref/templates/builtins/>
-   <https://docs.djangoproject.com/en/2.2/topics/templates/>
-   <https://habr.com/ru/post/23132/?ysclid=l2hw076rbl>


<a id="org716c477"></a>

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


<a id="orgf1e673c"></a>

# HTML формы

Формы могут быть более красивыми

![img](html_form1.jpg)


<a id="org6717bac"></a>

# HTML формы

И очень разнообразными. Но писать такие разнообразные формы вручную это очень утомительно. На помощь нам приходят [**Django Forms**](https://docs.djangoproject.com/en/3.2/topics/forms/).

![img](html_form.png)


<a id="org16aea23"></a>

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


<a id="org40587c0"></a>

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


<a id="orgcef109d"></a>

# Django формы


<a id="orgc54d0cf"></a>

## <span class="underline">[Form Fields](https://docs.djangoproject.com/en/3.2/ref/forms/fields/#built-in-field-classes)</span>

Поля формы в Django описываются классами Field, каждый из которых имеет своё представление в виде Widget-а.
![img](builtin_fields.png)


<a id="org708b9bb"></a>

# Bound / Unbond forms

Формы в *Django* **[могут быть в двух состояних](https://docs.djangoproject.com/en/3.2/ref/forms/api/#bound-and-unbound-forms)**

-   **unbound:** — форма пустая
-   **bound:** — форма заполнена данными


<a id="org3b0da2d"></a>

# Unbound

Форма не связана ни с какими данными

```python
form = MessageForm()
form.is_bound   # -> False
```


<a id="org49028c2"></a>

# Bound

Форма *частично* или *полностью* заполнена

```python
# обычно мы передаём request.POST
form = MessageForm({
    'message': 'foobar'
})
form.is_bound   # -> True
```


<a id="org1760a0d"></a>

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


<a id="orgd188b0d"></a>

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


<a id="orge973c75"></a>

# Валидаторы

```python
from django import forms

class EvenNumbersForm(forms.Form):
    number = forms.IntegerField(
        validators=[validate_even]
    )
```

*validators* добавит валидаторы к уже существующему базовому валидатору *IntegerField*


<a id="orgb139fdc"></a>

# Валидаторы

[**Готовых валидаторов очень много!**](https://docs.djangoproject.com/en/3.2/ref/validators/)

![img](validators.png)


<a id="org5a57091"></a>

# Forms Workflow

![img](form_handling_-_standard.png)


<a id="orgc6fad71"></a>

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


<a id="org60659fe"></a>

# Безопасность

[**Настоятельно рекомендую ознакомиться с этой документацией**](https://docs.djangoproject.com/en/3.2/topics/security/)
\newline
<https://docs.djangoproject.com/en/3.2/topics/security/>


<a id="orgd74a23c"></a>

# CSRF

На сайте может быть обычная кнопка, предлагающая вам посмотреть фотографии.

![img](csrf.png)


<a id="org8d8099c"></a>

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


<a id="orgbbeffdb"></a>

# CSRF

Но если на стороне банка используются csrf-токены в формах, то ничего страшного не случится. Запрос злоумышленника не может содержать нужное значение (случайное в рамках сессии) csrf-токена.

```html
<form method="post"
      action="{% url signup %}">
  {% csrf_token %}
</form>
```

![img](csrf_html.png)


<a id="orgabdc09b"></a>

# ModelForm

[**Прекрасная документация**](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/)


<a id="orgd9f3b85"></a>

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


<a id="orgeb77d6d"></a>

# ModelForm


<a id="orgd886cff"></a>

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


<a id="org6ebb86b"></a>

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


<a id="orgfd483c4"></a>

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


<a id="org3bc3d2c"></a>

# ModelForm

Или использовать *commit=False* чтобы доопределить модель перед записью в БД.

```python
form = YaForm(request.POST)
model = form.save(commit=False)
model.Z = 'foobar'
model.save()
```


<a id="orgda73e0c"></a>

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


<a id="org09ce08b"></a>

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


<a id="orgc25e9a9"></a>

# Widgets

Виджеты это то как формы будут представлены на web-страницы, то есть виджеты отвечают за генерацию HTML-кода для полей форм.
**[Документация](https://docs.djangoproject.com/en/3.2/ref/forms/widgets/)**

![img](widgets.png)


<a id="orgb534cd3"></a>

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


<a id="org46e0ddf"></a>

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


<a id="org6653484"></a>

# Widgets

```html
<input type="text" name="name"
       class="special" required>

<input type="url" name="url"
       required>

<input type="text" name="comment"
       size="40" required>
```


<a id="orgd223e76"></a>

# Вопросы-ответы

![img](questions.jpg)
