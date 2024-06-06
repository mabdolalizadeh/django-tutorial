# django tutorial

* [django](#django)
  - [create a project](#create-a-project)
  - [run server](#run-server)
  - [start app](#starting-app)
  - [urls](#urls)
  - [views](#views)
  - [templates](#templates)
  - [render](#render)
  - [static files](#static-files)
  - [function view partial](#function-view-partial)
  - [forms](#forms)
* [database](#database)
  - [models](#models)
  - [migration](#migration)
  - [getting](#getting)
  - [loading](#loading)
  - [slug](#slug)
  - [admin](#admin)
  - [relations](#relations)
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
for product and division you can use `widthratio` tag:
```python
{% widthratio a 1 b %} # this use for multiply
{% widthratio a b 1 %} # this use for division
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
{% include "[app name]/includes/[file].html" with VAR_NAME_IN_INCLUDE=VAR_NAME_IN_HTML %}
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
### function view partial
we need our `_layout.html` be more cleaner so we can load some elements that are need to have request to database and also load in many pages, put in another **html** file and then use render partial app:
```console
pip install django-render-partial
```
and then put in `settings.py` in installed app. after that make a function in `view.py`:
```python
def PARTIAL_TEST(request):
	return render(request, ‘HTML_NAME_OF_THE_ELEMENTS.html’)
```
and next you must add it to your template:
```html
{% load render_partial %}
.
.
.
{% render ‘ADDRESS_OF_VIEW’ %}
```
### forms
> **get** in form method means send in url and **post** means send in head.
for using django forms first make a new file with name `forms.py` then do this in it:
```python
from django import forms

class NAME_OF_CLASS(forms.Form):
	# here is like models but use forms. instead of models.
```
if you want your form inherit a model use `forms.ModelForm` instead of `forms.Form`:
```python
from django import forms
from .models import NAME_OF_MODEL

class NAME_OF_FORM(forms.ModelForm):
	class Meta:
		model = NAME_OF_MODEL
		fields = ['FIELDS'] # add name of fields that you want to show. if you need all fields use __all__
		exclude = ['FIELDS'] # add name of fields that you want not to show.
		widgets = {
			'FIELD': forms.TextInput(attr={})
			} # dictionary of each field and its attributes
		labels = {
			'FIELD': 'NAME THAT YOU WANT TO SHOW'
			} # names that shows to client
```

## database
 
### models
for making a table for your database first you must make a **class** in `models.py` file. you must know about django fields so have look on [this](https://docs.djangoproject.com/en/5.0/ref/models/fields/):
```python
from django.db import models

class Name_of_table(models.Model):
    # put here needs of your datas
    # these are just examples
    title = models.CharField(max_length=[something])
```
if you wan’t something can’t edit from admin you can add `editable=False` in constructor of that module. for example:
```python
slug = models.SlugField(editable=False)
```

### migration
for migrating your changes do this in console:
```console
python manage.py makemigrations
```

for adding models to database do this:
```console
python manage.py migrate
```
### getting
for getting set from database you can do this(it must be one item):
```python
DATABASE_NAME.objects.get([cloumn what you want])
```
for getting more than one item use `filter()` funtction:
```python
DATABASE_NAME.objects.filter([item])
```
for useing more than sth or lower than something add in end of item `__lt`(lower than),`__lte`(lower or equal),`__gt`(greater than),`__gte`(greater than or  equal). you can see more in [here](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#field_lookup)

### loading
for loading with primary key use this function in `views.py` (this function if it doesn't have any response rais 404 instead):
```python
from django.shortcuts import get_object_or_404

def index(request, primary_key):
  response = get_object_or_404(CLASS_NAME, pk=primary_key)
```

in `models.py` you can add a function that give you url base of parameter you need:
```python
from django.urls import reverse

def get_absolute_url(self):
  return return reverse('URL_NAME', args=[self.PARAMETER])
```
### slug
slug is something that put dash(-) instead of spaces in your title for example *temp title* -> *temp-title*. for use it you must import it then use it as a field in data base. after that override method of save:
```python
from django.utils.text import slugify

class DATA_BASE:
  slug = SlugField(defult="", null=False)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)
```
### soft delete
sometimes we mustn't delete completely, because with this we lost 2 or more product not one. for this reason we have something that called soft delete. we put a boolean field:
```python
is_deleted = models.BooleanField()
```

### admin
for editing admin page you can make a new class in `admin.py`, and in end you must pass it to `admin.site.register` function:
```python
class NAMEAdmin(admin.ModelAdmin):
	readonly_fields = ['NAME_OF_FIELD'] # list of fields that you want make it read only
	prepopulated_fields = { 'NAME_OF_FIELD' : ['NAME_OF_FIELDS'] } # dictionary that says the field complete 	base on which filed
	list_display = ['NAME_OF_FIELDS', '__str__'] # put fields that you want to show the value of that in the main 	list
	list_filter = ['NAME_OF_FIELDS'] # filter base on one or some fields
	list_edtitable = ['NAME_OF_LIST'] # with this option you can edit any field you want  just from the list ,without opening it

admin.site.register(models.DATABASE_NAME, NAMEAdmin)
```
#### Meta class
mata class use for more option for models in admin we make it in class model:
```python
class MODEL_NAME(models.Model):
	class Meta:
		verbose_name = '' # this is name instead of class name
		verbose_name_plural = '' # this name use for plural names instead 
```
### relations
for tables we have three relations **one to one**, **one to many**, **many to many**.  have a look on [this](https://jamboard.google.com/d/1ZlVUVBwfMy_vE-jSylpoiymbqBPauDAQlzoO0HYUDTI/edit?usp=sharing).
for pointing to another table we can use `models.ForeignKey` module:
```python
FIELD = model.ForeignKey(NAME_OF_TABLE, on_delete=models.CASCADE) # cascade means if table has been deleted, delete this product
```
or for one to one relations use this. one to one use for user informations:
```python
FIELD = model.OneToOneField(TABLE_NAME, on_delete=models.CASCADE)
```
and filnally for many to many use this. many to many use for tags:
```python
FIELD = model.ManyToMany(TABLE_NAME)
```


## status responses

the responses that get from network has several ranges:

1. 200: it means ok
2. 404: the page isn't exist
3. 302: means redirect
