from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User,Question
#要約用の関数をインポート
from .util.summarize import summarize,best_summarize_doc

def index_view(request):
    return render(request, 'index.html')

def login(request):
    params = {'form': None}
    if request.method == 'POST':
        print(request.POST['password'],request.POST['email'])
        user = User.objects.get(email=request.POST['email'],password=request.POST['password'])
        print(user.id)
        if user:
            url = "mypage/"+str(user.id)
            return redirect(to=url)
        else:
            return render(request, 'login.html', params)

    else:
        params['form'] = UserForm()
    return render(request, 'login.html', params)

def signup(request):
    params = {'form': None}
    if request.method == 'POST':
        user = User.objects.create(name=request.POST["name"], email=request.POST["email"],password =request.POST["password"])
        params["user"] = user
        url = "mypage/" + str(user.id)
        return redirect(to=url)
    else:
        params['form'] = UserForm()
    return render(request, 'signup.html',params)


def mypage(request,pk):
    params ={"user" : None, "questions" : None}
    user = User.objects.get(id=pk)
    questions =Question.objects.filter(userid=pk)
    params["user"] = user 
    params["questions"] = questions
    return render(request, 'mypage.html',params)


def answer(request,pk,ans):
    return render(request, 'answer.html')

# questions = {
#     {"question":"ななな","answer","aaaa"},
#     {"question":"ななな","answer","aaaa"}
# }