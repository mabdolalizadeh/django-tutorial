from django.shortcuts import render

datas = [
    {
        'name': "logo",
        'image': "images/logo.png",
    },
    {
        'name': "kid",
        'image': "images/kid.jpg"
    },
    {
        'name': "teen",
        'image': "images/teen.jpg"
    },
    {
        'name': "adult",
        'image': "images/adult.jpg"
    }
]

def index(request):
    return render(request, 'main/index.html')

def signin(request):
    return render(request, 'main/signin.html')