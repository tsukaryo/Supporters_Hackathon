from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User,Question,Company,ES
#要約用の関数をインポート
from .util.summarize import summarize,best_summarize_doc
#wordcloud用の関数をインポート
from .util.wordcloud import get_word_str,word_cloud

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

def logout(request):
    return redirect('index')


def mypage(request,pk):
    params ={"user" : None, "questions" : None,"companies":None} 
    user = User.objects.get(id=pk)
    print(user)
    questions = Question.objects.filter(userid=pk)
    companies = Company.objects.filter(userid=pk)
    params["user"] = user 
    params["questions"] = questions
    params["companies"] = companies

    return render(request, 'mypage.html',params)



def answer(request,pk,ans):
    params = {}
    params["pk"] = pk
    params["ans"] = ans
    question = Question.objects.filter(userid=pk,id=ans)
    print(question[0].answer)
    answer = question[0].answer
    question = question[0].question
    params["question"] = question
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

def post_answer(request,pk):
    params = {}
    params['pk'] = pk
    if request.method == 'POST':
        question = Question.objects.create(userid=pk, question=request.POST["question"],answer =request.POST["answer"])
        user = User.objects.get(id=pk)
        questions =Question.objects.filter(userid=pk)
        companies =Company.objects.filter(userid=pk)
        params["user"] = user 
        params["questions"] = questions
        params["companies"] = companies
        
        return render(request, 'mypage.html',params)
    return render(request,'post_answer.html',params)

def CompanyEsPage(request,pk,comp):
    params ={"user_id" : None,"questions" : None,"company" : None} 
    company = Company.objects.filter(id=comp)
    questions_answers = ES.objects.filter(userid=pk,company_id=comp)
    params["questions"] = questions_answers
    params["company"] = company[0]

    # company = [{"id":1}]
    #question_id = Question.objects.get(userid=pk)
    #company_id = Company.objects.get(userid=pk)
    params['user_id'] = pk
    #params['question'] = question_id
    #params['company'] = company_id

    return render(request,'CompanyEsPage.html',params)


def delete_answer(request,pk,ans):
    answer = Question.objects.get(userid=pk, id=ans)
    answer.delete()
    params ={"user" : None, "questions" : None} 
    user = User.objects.get(id=pk)
    questions = Question.objects.filter(userid=pk)
    companies = Company.objects.filter(userid=pk)
    params["user"] = user 
    params["questions"] = questions
    params["companies"] = companies
    return render(request, 'mypage.html',params)
    
def CompanyESPost(request,pk,comp):
    params = {}
    params['pk'] = pk
    params["user_id"] = pk
    if request.method == 'POST':
        question = ES.objects.create(userid=pk, question=request.POST["question"],answer =request.POST["answer"],company_id=comp)
        user = User.objects.get(id=pk)
        questions = ES.objects.filter(userid=pk)
        company = Company.objects.get(id=comp)
        params["company"] = company
        params["user"] = user 
        params["questions"] = questions
        return render(request, 'CompanyEsPage.html',params)
    return render(request,"ESpost.html",params)

def delete_ES(request,pk,es,comp):
    es = ES.objects.get(id=es)
    es.delete()
    params ={"user" : None, "questions" : None} 
    user = User.objects.get(id=pk)
    company = Company.objects.get(id=comp)
    questions = ES.objects.filter(userid=pk)
    companies = Company.objects.filter(userid=pk)
    params["user"] = user 
    params["company"] = company
    params["questions"] = questions
    params["companies"] = companies
    return render(request, 'CompanyESPage.html',params)
    return render()


def post_company(request, pk):
    params = {}
    params['pk'] = pk
    if request.method == 'POST':
        company = Company.objects.create(userid = pk, company_name = request.POST["company"])
        user = User.objects.get(id=pk)
        companies = Company.objects.filter(userid=pk)
        questions =Question.objects.filter(userid=pk)
        params["user"] = user 
        params["companies"] = companies
        params["questions"] = questions
        return render(request, 'mypage.html',params)
    return render(request, "Add_Company.html", params)



def questions(request,pk):
    params ={"user" : None, "questions" : None} 
    user = User.objects.get(id=pk)
    questions = Question.objects.filter(userid=pk)
    params["user"] = user 
    params["questions"] = questions
    return render(request,"questions.html",params)

def companies(request,pk):
    params ={"user" : None, "companies" : None} 
    user = User.objects.get(id=pk)
    companies = Company.objects.filter(userid=pk)
    params["user"] = user 
    params["companies"] = companies
    return render(request,"companies.html",params)

def wordcloud_test(request,pk,ans):
    params = {}
    params["pk"] = pk
    params["ans"] = ans
    question = Question.objects.filter(userid=pk,id=ans)
    print(question[0].answer)
    answer = question[0].answer
    question = question[0].question
    params["question"] = question
    params["answer"] = answer
    params["answer_length"] = len(answer)
    params["word_cloud"] = word_cloud(answer,"テスト")
    

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
    return render(request,"wordcloud_test.html",params)
