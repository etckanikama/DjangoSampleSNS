from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import BoardModel
from django.contrib.auth.decorators import login_required

# Create your views here.

def signupfunc(request):
    # print(request.method)#GET
    # User.objectsでテーブルからデータを持ってこれる(all(),get()など)
    # user2 = User.objects.get(username='root')
    # print(user2.email)
    if request.method == 'POST':
        # signup.html内の'username'
        username2 = request.POST['username']
        password2 = request.POST['password']
        # print(request.POST)
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'signup.html', {'some':100})
    return render(request, 'signup.html', {'some':100})

# デコレーター
@login_required
def loginfunc(request):
    if request.method == 'POST':
        # signup.html内の'username'
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

def listfunc(request):
    # boardModelのすべてのオブジェクトを取り出すことがデキル
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})
