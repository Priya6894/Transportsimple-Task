from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Questions, Answers, Likes
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def post_question(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            question = Questions.objects.create(author=request.user, text=text)
            return redirect('view_question', question_id=question.id)
    return render(request, 'post_question.html')


### View questions posted by others 
@login_required
def view_question(request, question_id):
    question = Questions.objects.get(pk=question_id)
    answers = Answers.objects.filter(question=question)
    return render(request, 'view_question.html', {'question': question, 'answers': answers})


#### Able to post a Question
@login_required
def post_answer(request, question_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            question = Questions.objects.get(pk=question_id)
            Answers.objects.create(question=question, author=request.user, text=text)
    return redirect('view_question', question_id=question_id)

### Able to answer questions posted by others
def answer_question(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    if request.method == 'POST':
        content = request.POST['content']
        answer = Answers.objects.create(user=request.user, question=question, content=content)
        return redirect('home')
    return render(request, 'answer_question.html', {'question': question})


### Should be able to like answers posted by others
@login_required
def like_answer(request, answer_id):
    answer = Answers.objects.get(pk=answer_id)
    Likes.objects.create(answer=answer, user=request.user)
    return redirect('view_question', question_id=answer.question.id)

# The user should be able  a login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('post_question')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


## The user should be able to a logut
def user_logout(request):
    logout(request)
    return redirect('login')


#### created a signup page for the user
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
