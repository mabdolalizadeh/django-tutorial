# django tutorial

* [notes](#notes)
* [statuses](#status)

## notes

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

## statuses

for responses that get from network has several ranges:

1. 200: it means ok
2. 404: the page isn't exist
3. 302: means redirect
