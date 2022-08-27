import re
from tkinter.messagebox import QUESTION
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import PollAddForm

# Create your views here.

def home(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request,'index.html',context)

def register(request):
    if request.method == 'POST':
        req_username = request.POST['register_username']
        req_password1 = request.POST['register_password1']
        req_password2 = request.POST['register_password2']
        req_email = request.POST['register_email']

        # conditions
        if len(req_username) >= 7:
            messages.error(request,'length should be greater than 7')
            return redirect('index')
        if not req_username.isalnum():
            messages.error(request,'length should be contain letters and numbers')
            return redirect('index')

        if req_password1 != req_password2:
            messages.error(request,'password not match!')
            return redirect('index')

        # user creation

        myuser = User.objects.create_user(req_username,req_email,req_password1)
        # myuser.username = req_username
        # myuser.email = req_email
        # myuser.password = req_password1
        myuser.save()

        messages.success(request,"user created successfully")
        return redirect('login')
    else:
        return render(request,'register.html')
        return redirect('/')
        return HttpResponse('404 not found')




def login_handle(request):
    print("yasssssssssssssssssssss")
    if request.method == 'POST':
        req_username = request.POST['login_username']
        req_password = request.POST['login_password']

        user = authenticate(request,username = req_username,password = req_password)

        if user is not None:
            print("user is not none")
            login(request,user)
            messages.success(request,"successfully logged in!")
            
            return redirect('index')
        else:
            print("user is none")
            messages.error(request,"not valid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')
        # return HttpResponse('404 not found')
    

def logout_handle(request):
    logout(request)
    messages.success(request,"successfully logged out!")
    return redirect('/')
    

def create_poll(request):
    if request.method == 'POST':
        poll = request.POST['poll_name']
        op1 = request.POST['option1']
        op2 = request.POST['option2']
        op3 = request.POST['option3']
        op4 = request.POST['option3']

        # conditions

        if not poll.isalnum():
            messages.error(request,("length should be contain letters and numbers"))
            return redirect('index')

        # if req_password1 != req_password2:
        #     messages.error(request,"password don't match!")
        #     return redirect('index')

        # user creation

        mypoll = User.objects.create(poll,op1,op2,op3,op4)
        # myuser.username = req_username
        # myuser.email = req_email
        # myuser.password = req_password1
        mypoll.save()

        messages(request,"user created successfully")
    else:
        return render(request,'register.html')
        return redirect('/')
        return HttpResponse('404 not found')


def question_detail(request,pk):
    try:
        question = Question.objects.get(id = pk)
        options = question.answers.all()
        context = {'question': question,'options':options}

        return render(request,'question.html',context)

    except Exception as e:
        print(e)
        return redirect('/')

def result(request,pk):
    question = Question.objects.get(id = pk)
    options = question.answers.all()

    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.count += 5
        selection_option.save()
    return render(request, 'result.html', {'question': question, 'options': options})

    # return render(request,'result.html')

def polls_add(request):
    # if request.user.has_perm('polls.add_poll'):
    form = PollAddForm()
    if request.method == 'POST':
        form = PollAddForm(request.POST)
        if form.is_valid():
            Ques = form.save(commit=False)
            Ques.user = request.user
            Ques.save()
            new_choice1 = Answer(
                    question=Ques, answer_text=form.cleaned_data['choice1']).save()
            new_choice2 = Answer(
                    question=Ques, answer_text=form.cleaned_data['choice2']).save()
            new_choice3 = Answer(
                    question=Ques, answer_text=form.cleaned_data['choice3']).save()
            new_choice4 = Answer(
                    question=Ques, answer_text=form.cleaned_data['choice4']).save()

            messages.success(
                    request, "Poll & Choices added successfully.", extra_tags='alert alert-success alert-dismissible fade show')

            return redirect('/')
        else:
            form = PollAddForm()
            context = {
            'form': form,
            }
            return render(request, 'add_poll.html', context = {'form': form})

    return render(request, 'add_poll.html', context = {'form': form})
    # else:
    #     return HttpResponse("Sorry but you don't have permission to do that!")


def profile(request):
    ques = request.user.questions.all()
    
    return render(request,'profile.html',context = {'ques':ques})

@login_required
def polls_delete(request, pk):
    ques = get_object_or_404(Question, pk=pk)
    if request.user != ques.user:
        return redirect('index')
    ques.delete()
    messages.success(request, "Poll Deleted successfully.",
                     extra_tags='alert alert-success alert-dismissible fade show')
    return redirect("index")
