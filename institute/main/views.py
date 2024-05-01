from django.shortcuts import render

data = [
    {
        'name': "kid",
        'image': "kid.jpg",
        'text': "if you want a shining future for your kid."
    },
    {
        'name': "teen",
        'image': "teen.jpg",
        'text': "Learn English is necessary for teens."
    },
    {
        'name': "adult",
        'image': "adult.jpg",
        'text': "Learn English is necessary for adults."
    }
]

def index(request):
    context = {
        'data': data
    }
    return render(request, 'main/index.html', context)

def signin(request):
    return render(request, 'main/signin.html')