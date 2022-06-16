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
        user = User.objects.filter(email=request.POST['email'],password=request.POST['password'])
        
        if user:
            user_id = user[0].id
            url = "mypage/"+str(user_id)
            return redirect(to=url)
        else:
            params["error"] = "入力内容に誤りがあります。"
            params['form'] = UserForm()
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
    params = {}
    question = Question.objects.filter(userid=pk,id=ans)
    print(question[0].answer)
    answer = question[0].answer
    params["answer"] = answer
    params["answer_length"] = len(answer)
    if request.method == 'POST':
        print("要約前：")
        print(request.POST["length"])
        max_letter = int(request.POST["length"])
        summarized_doc = best_summarize_doc(answer, max_letter)
        print("要約後：")
        print(summarized_doc)
        params["summarized_answer"] = summarized_doc
        params["summarized_answer_length"] = len(summarized_doc)
        print("文字数:", len(summarized_doc), "文字")
        return render(request, 'answer.html',params)
    return render(request, 'answer.html', params)

# questions = {
#     {"question":"ななな","answer","aaaa"},
#     {"question":"ななな","answer","aaaa"}
# }