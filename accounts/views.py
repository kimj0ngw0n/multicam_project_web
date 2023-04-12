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


@login_required
@require_safe
def friends(request):
    profile_user = request.user
    friends = profile_user.friends.all()
    
    return render(request, 'accounts/friends.html', {
        'profile_user': profile_user,
        'friends': friends,
    })


@require_safe
def profile(request, username):
    if request.user.is_authenticated:
        profile_user = get_object_or_404(User, username=username)
        
        is_my_profile = profile_user.pk == request.user.pk

        # 친구 추가 버튼
        is_friend = profile_user.friends.filter(pk=request.user.pk).exists()

        # 친구 요청 목록
        request_friends = request.user.friend_request_from.all()

        return render(request, 'accounts/profile.html', {
            'profile_user': profile_user,
            'is_my_profile': is_my_profile,
            'is_friend': is_friend,
            'request_friends': request_friends,
        })
    else:
        return redirect('accounts:signin')


@require_POST
def request_friend(request, starname):
    star = get_object_or_404(User, username=starname)
    fan = request.user
    
    if star == fan:
        return HttpResponseBadRequest('Can not friendly yourself')
    else:
        if fan.is_authenticated:
            # 이미 친구라면, 친구 삭제
            if fan.friends.filter(pk=star.pk).exists():
                fan.friends.remove(star)
            # 이미 친구 요청을 보냈으면, 재요청
            else:
                if fan.friend_request_to.filter(pk=star.pk).exists():
                    fan.friend_request_to.remove(star)
                fan.friend_request_to.add(star)

            return redirect('accounts:profile', star)
        else:
            return redirect('accounts:signin')


@login_required
@require_POST
def feedback_request(request, fanname):
    star = request.user
    fan = get_object_or_404(User, username=fanname)
    
    star.friend_request_from.remove(fan)
    
    # 친구 요청 수락
    if request.POST.get('accept'):
        star.friends.add(fan)
    
    return redirect('accounts:profile', star.username)


@login_required
@require_POST
def delete_friend(request, fanname):
    star = request.user
    fan = get_object_or_404(User, username=fanname)
    
    star.friends.remove(fan)

    return redirect('accounts:profile', star.username)
