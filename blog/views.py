from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm, ComentsForm, MailingForm, UserRegistrationForm, UserProfileForm
from .models import Post, Category, Teg, Coments, Mailing, UserProfile
from django.utils import timezone


# Create your views here.
def get_categories():
    all = Category.objects.all()
    count = all.count()
    return {'cat1': all[:count / 2 + count % 2], 'cat2': all[count / 2 + count % 2:]}


def index(request):
    posts = Post.objects.all().order_by("-published_date") # сортує по даті додавання
    # postid = Post.objects.get(pk=1)
    # posts = Post.objects.filter(title__icontains="python")
    # posts = Post.objects.filter(published_date__year=2023)
    # posts = Post.objects.filter(category__name__exact="Pyton")
    categories = Category.objects.all()

    context = {
        "posts": posts,
        "category": categories

    }
    context.update(get_categories())
    return render(request, 'blog/index.html', context=context)


# def post(request, id=None):
#     post = get_object_or_404(Post, title=id)
#     coments = Coments.objects.filter(post_id=post.id).order_by('-coment_date') # фільтрує коментарі які є в пості.
#     query = request.POST.get('query')
#     if query:
#         user = request.user
#         comment = Coments(coment_date=timezone.now(), coment=query, user=user, post_id=post)
#         comment.save()
#
#     context = {
#         "post": post,
#         "coments": coments
#     }
#     context.update(get_categories())
#     return render(request, 'blog/post.html', context=context)

def post(request, id=None):
    post = get_object_or_404(Post, title=id)
    coments = Coments.objects.filter(post_id=post.id).order_by('-coment_date') # фільтрує коментарі які є в пості.
    form = ComentsForm()
    user = User.objects.get(username="sedimat")

    if request.method == "POST":
        form = ComentsForm(request.POST)
        if form.is_valid():
            coment = form.save(commit=False)
            coment.published_date = timezone.now()
            coment.post_id = post
            coment.user = user
            coment.save()

            context = {
                "post": post,
                "coments": coments,
                "form": form
            }
            context.update(get_categories())
            return render(request, 'blog/post.html', context=context)

    context = {
        "post": post,
        "coments": coments,
        "form": form
    }
    context.update(get_categories())
    return render(request, 'blog/post.html', context=context)


def news(request):
    context = {
        "test": "Blog test"
    }
    return render(request, 'blog/news.html', context=context)


def woods(request):
    context = {
        "test": "Blog test"
    }
    return render(request, 'blog/woods.html', context=context)

def category(request, name=None):
    c = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=c).order_by("-published_date") # сортує по даті додавання

    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context=context)


def search(request):
    query = request.GET.get('query')

    posts = Post.objects.filter(Q(content__icontains=query) |
                                Q(title__icontains=query) |
                                Q(tegs__name__icontains=query)).order_by("-published_date")  # сортує по даті додавання

    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context=context)

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.user = request.user
            post.save()
            return index(request)

    form = PostForm()
    context = {"form": form}
    context.update(get_categories())
    return render(request, 'blog/create.html', context=context)


def clear_mailing_table():
    pass


def about(request):
    if request.method == "POST":
        form = MailingForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.save()
            form = MailingForm()
            message = "Електрону пошту додано"
            context = {"form": form,
                       "message": message}
            context.update(get_categories())
            return render(request, 'blog/about.html', context=context)

    # Mailing.objects.all().delete()
    # clear_mailing_table()
    # видаляє все з таблиці


    form = MailingForm()
    context = {"form": form}
    context.update(get_categories())
    return render(request, 'blog/about.html', context=context)

def user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        form1 = UserProfileForm(request.POST)

        if form.is_valid():
            form.save()
            form = UserRegistrationForm()
            context = {"form": form}
            context.update(get_categories())
            # return redirect('index')
            a = "Ви успішно зареєструвались"
            return render(request, 'blog/user.html', context={"a": a})

        elif form1.is_valid():
            username = request.user.username
            user = User.objects.get(username=username)
            info = form1.save(commit=False)
            info.user = user
            info.save()
            return redirect('user')

        else:
            # Якщо форма не є валідною, ви можете вивести помилки у консоль для аналізу
            a = form.errors
            return render(request, 'blog/user.html', context={"a": a})

    else:
        if request.user.is_authenticated:
            username = request.user.username
            user = User.objects.get(username=username)
            posts = Post.objects.filter(user=user)
            try:
                info = UserProfile.objects.get(user=user)
                context = {
                    "user": user,
                    "info": info,
                    "status": False,
                    "posts": posts
                }
                context.update(get_categories())
                return render(request, 'blog/user.html', context=context)

            except UserProfile.DoesNotExist:
                error = "Добавте додадкову інформацію"
                form1 = UserProfileForm()
                context = {
                    "user": user,
                    "error": error,
                    "form1": form1,
                    "status": True
                }
                return render(request, 'blog/user.html', context=context)

        form = UserRegistrationForm()
        context = {"form": form}
        context.update(get_categories())
        return render(request, 'blog/user.html', context=context)



def logout_view(request):
    logout(request)
    return redirect('index')

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('user')

def edit_user(request, user_id):
    if request.method == 'POST':
        description = request.POST.get('description')
        email = request.POST.get('email')
        url = request.POST.get('url')
        if description:
            user = get_object_or_404(UserProfile, user__id=user_id)
            user.description = description
            user.save()
            return redirect('user')

        elif email:
            user = get_object_or_404(User, id=user_id)
            user.email = email
            user.save()
            return redirect('user')

        elif url:
            user = get_object_or_404(UserProfile, user__id=user_id)
            user.avatar = url
            user.save()
            return redirect('user')

        else:
            return redirect('user')




