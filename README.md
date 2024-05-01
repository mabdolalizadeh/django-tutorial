# django tutorial

* [django](#django)
* [data base](#data-base)
* [status responses](#status-responses)

## django

### create a project

for creating a project using this command:

```console
django-admin startproject [mysite]
```

### run server

for running server use this command:

```console
python manage.py runserver
```

### starting app

for starting an app use this command:

```console
python manage.py startapp [name of app]
```

after starting app go to your main directory and in settings.py at section `INSTALLED_APP` put name of new app you made.

### urls

for showing your app in your project you must make an `urls.py` file in your application directory. after that in `urls.py` app make a list:

```python
from django.urls import path
from . import views

urlpatterns= [
  path('[urls adress]', views.index)
]
```

then in the main `urls.py` file do this:

```python
from django.urls import path, include

urlpatterns= [
  path('admin/', admin.site.urls)
  path('[name of your app]/', include('[name of your app].urls'))
]
```

or you can give a name to each url like this:

```python
from django.urls import path
from . import views

urlpatterns= [
  path('[urls adress]', views.index, name='[a unic name]')
]
```

#### dynamic urls

for dynamic urls, first do like this in `views.py` of application:

```python
def dynamic(request, [name of dynamic url]):
    return HttpResponse()
```

then in `urls.py` of application:

```python
urlpatterns= [
  path('<[type]:[name of dynamic url]>', views.dynamic)
]
```

for getting name url by name you can use this pattern:

```python
from django.urls import reverse

redirect = reverse('[name of url]')
```

### views

for showing a view, you must do like this(the name of function is optional):

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("this is django curse")
```

we something that name is `HttpResponseRedirect` that redirect to another page for example:

```python
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect('[page that you want]')
```

another good thing is `HttpResponseNotFound` for undefined pages:

```python
from django.http import HttpResponseNotFound

def index(request):
    return HttpResponseNotFound('[anything you want]')
```

### templates

for using templates first make a directory that name is templates then make another folder in it with name of your application. do this in your app's directory:

```console
mkdir templates
cd templates
mkdir [app's name]
```

then in `view.py` do this:

```python
from django.template.loader import rendoe_to_string

def index(request):
    response_data = render_to_string('[app name]/[html file].html')
    return HttpResponse(response_data)
```

### render

for rendering do this:

```python
def index(request):
    return render(request, '[app name]\[html file].html')
```

#### DTL

for using python's codes or django's dynamic data in html, first make a dictionary that you need to get data from it and then you must give it to render function:

```python
def index(request):
    context: {
        'data': [dynamic list]
    }
    return render(request, '[app name]\[html file].html', context)
```

after that you must put a **DTL** in your html file like this:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>
        {{ data }}
    </h1>
</body>
</html>
```
for having dynamic data except database, you can use a `dictionary` and have access to data value with their keys like this:
```python
{{ [data name].[key name] }}
```

##### built-in filter

for add filter to your data use this syntax:

```python
{{ value|filter }}
```

if you want to know about what filter we have visit [this](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/).
for add an attribute to an url use `add` filter:
```python
{% static '[url'|add:[new url] %}
```
##### tags

for puting python code in your html file you can use tags (this examples is just for loop. you can see other tags [here]([https://](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/)https://)):

```python
{% for n in [list] %}
  # html tags here
{% endfor %}
```

###### **block tag**

always we have some fixed data in a webpage, same tags, same `<body>` or same `<head>` so in here we can make a `base.html` file to put the fixed data in it. `base.html` is in root of our project in directory that we created which name is templates(like other templates).

for using dynamic data you put `block` tag in your `base.html`:

```html
{% block [name of block] %}
    [defualt value]
{% endblock %}

```

in other **html** file you must just fill the blocks. for this first you must put the direction of file in `settings.py`:

```python
templates= [
  {
    'DIR': [
        BASE_DIR / "templates"
    ],
  }
]
```

then in other **html** file in the first line put this:

```html
{% extends "base.html" %}
```

and at the end you must make the `block` tag again with the *names you used in base* and **fill** them.

###### **include**

if your webpage has a part that it must share with other pages you can use `include`. for this, first you must make a directory that name is `includes` in your template directory in application. then you put your codes in a html file and after that in other html files that you need do this:

```djangourlpath
{% include "[app name]/includes/[file].html" %}
```

### static files

for adding static files to your application first make directory of it:

```console
mkdir static
cd static
mkdir [apps name]
```

then for using statics you must put `{% load static %}` in the top of your **html** file and after that:

```html
{% load static %}
<link rel="stylesheet" href="{% static "[app name]/[style name].css" %}">
```

for having a global static file you must put this settings in `settings.py` file:
```python
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
```

## data base
 
### models
for making a table for your database first you must make a **class** in `models.py` file. you must know about django fields so have look on [this](https://docs.djangoproject.com/en/5.0/ref/models/fields/):
```python
from django.db import models

class Name_of_table(models.Model):
    # put here needs of your datas
    # these are just examples
    title = models.CharField(max_length=[something])
```

### migration
for migrating your changes do this in console:
```console
python manage.py makemigrations
```

## status responses

the responses that get from network has several ranges:

1. 200: it means ok
2. 404: the page isn't exist
3. 302: means redirect
