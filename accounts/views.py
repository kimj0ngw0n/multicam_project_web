from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.http import require_http_methods, require_POST, require_safe

from django.http import HttpResponseBadRequest

from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


User = get_user_model()


@require_http_methods(['GET', 'POST'])
def signup(request):
    # 이미 로그인한 사람이 GET 요청 보내는 경우
    if request.user.is_authenticated:
        return redirect('accounts:profile', request.user.username)
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        # 회원가입 성공
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:profile', user.username)
    # 회원가입 창 접근 또는 회원가입 실패
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def signin(request):
    # 이미 로그인한 사람이 GET 요청 보내는 경우
    if request.user.is_authenticated:
        return redirect('accounts:profile', request.user.username)
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:profile', user.username)
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/signin.html', {
        'form': form,
    })


def signout(request):
    logout(request)
    return redirect('accounts:signin')


@require_safe
def profile(request, username):
    if request.user.is_authenticated:
        profile_user = get_object_or_404(User, username=username)
        
        is_my_profile = profile_user.pk == request.user.pk
        
        # 팔로우 버튼
        is_following_star = profile_user.fans.filter(pk=request.user.pk).exists()
        follow_button_text = '팔로우 취소' if is_following_star else '팔로우'
        
        return render(request, 'accounts/profile.html', {
            'profile_user': profile_user,
            'is_my_profile': is_my_profile,
            'follow_button_text': follow_button_text,
        })
    else:
        return redirect('accounts:signin')


def request_friend(request, starname):
    pass


def accept_friend(request, fanname):
    pass


def delete_friend(request, fanname):
    pass
