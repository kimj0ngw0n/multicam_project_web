from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest
from django.db.models import Count
from django.core.paginator import Paginator

from .models import Surver, Access, Category, Channel, Message
from .forms import SurverForm, AccessForm, CategoryForm, ChannelForm, MessageForm


User = get_user_model()


# Create
@login_required
@require_http_methods(['GET', 'POST'])
def create_surver(request):
    if request.method == "POST":
        form = SurverForm(request.POST)
        if form.is_valid():
            surver = form.save()
            
            # 서버 주인 설정
            owner = request.user
            access = Access(surver=surver, user=owner, type='owner')
            access.save()

            return redirect('surver:detail', surver.pk, 0)
    else:
        form = SurverForm()

    return render(request, 'surver/form.html', {
        'form': form,
        'type_message': '서버 추가',
    })


@login_required
@require_http_methods(['GET', 'POST'])
def create_category(request, surver_pk):
    surver = get_object_or_404(Surver, pk=surver_pk)

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.surver = surver
            category.save()
            return redirect('surver:detail', surver.pk, 0)
    else:
        form = CategoryForm()

    return render(request, 'surver/form.html', {
        'form': form,
        'type_message': '카테고리 추가',
    })


@login_required
@require_http_methods(['GET', 'POST'])
def create_channel(request, surver_pk):
    if request.method == "POST":
        form = ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.save()
            return redirect('surver:detail', surver_pk, channel.pk)
    else:
        form = ChannelForm()

    return render(request, 'surver/form.html', {
        'form': form,
        'type_message': '채널 추가',
    })


@login_required
@require_POST
def create_message(request, channel_pk):
    channel = get_object_or_404(Channel, pk=channel_pk)
    category = channel.category
    surver = category.surver

    form = MessageForm(request.POST)

    if form.is_valid():
        message = form.save(commit=False)
        message.channel = channel
        message.user = request.user
        message.save()
        return redirect('surver:detail', surver.pk, channel.pk)


# Read
@login_required
@require_safe
def detail(request, surver_pk, channel_pk):
    user = request.user
    survers = user.survers.all()

    this_surver = get_object_or_404(Surver, pk=surver_pk)
    # 사용자가 특정 서버에 들어가있고, 채널이 있는 경우
    if survers and channel_pk:
        this_channel = get_object_or_404(Channel, pk=channel_pk)
    # 사용자가 특정 서버에 들어가있고, 채널이 없는 경우
    else:
        this_channel = False
    # # 사용자가 아무 서버에도 들어가 있지 않을 경우
    # else:
    #     state1 = 0
    #     state2 = 1

    #     this_surver = 0
    #     this_channel = 0

    form = MessageForm()
    
    # 채널이 있을 경우, 메시지 출력 및 입력 가능
    messages = False
    if this_channel:
        messages = this_channel.messages.all()

    # 서버 주인이 아닐 경우, 초대 버튼 안 보이도록
    is_owner = bool(this_surver.surver_access.filter(user=user, type='owner'))

    # 서버 멤버
    member_accesses = this_surver.surver_access.all()
        
    return render(request, 'surver/detail.html', {
        'survers': survers,
        'this_surver': this_surver,
        'this_channel': this_channel,
        'form': form,
        'messages': messages,
        'is_owner': is_owner,
        'member_accesses': member_accesses,
    })


# Update
def update_surver(request, surver_pk):
    pass

    
def update_category(request, category_pk):
    pass


def update_channel(request, channel_pk):
    pass


def update_message(request, message_pk):
    pass


# Delete
@login_required
@require_POST
def delete_surver(request, surver_pk):
    me = request.user
    surver = get_object_or_404(Surver, pk=surver_pk)

    is_owner = surver.surver_access.filter(user=me, type='owner')

    if is_owner:
        surver.delete()
        return redirect('accounts:profile', me.username)
    else:
        return HttpResponseBadRequest('You are not owner in this surver.')


def delete_category(request, category_pk):
    pass


def delete_channel(request, channel_pk):
    pass


@login_required
@require_POST
def delete_message(request, message_pk):
    me = request.user
    message = get_object_or_404(Message, pk=message_pk)
    message_user = message.user
    channel = message.channel
    surver = channel.category.surver

    is_owner = surver.surver_access.filter(user=me, type='owner')

    if message_user == me or is_owner:
        message.delete()
        return redirect('surver:detail', surver.pk, channel.pk)
    else:
        return HttpResponseBadRequest('You are not writer or owner for this message.')
    

# etc    
def reaction(request, message_pk):
    pass


@login_required
@require_http_methods(['GET', 'POST'])
def add_member(request, surver_pk):
    inviter = request.user
    surver = get_object_or_404(Surver, pk=surver_pk)
    is_owner = surver.surver_access.filter(user=inviter, type='owner')

    if is_owner:
        if request.method=='POST':
            form = AccessForm(request.POST)
            if form.is_valid():
                access = form.save(commit=False)
                # 서버의 멤버가 아니라면 초대
                if not Access.objects.filter(surver=surver, user=access.user):
                    access.surver = surver
                    access.type = ''
                    access.save()
                return redirect('surver:detail', surver.pk, 0)
        else:
            form = AccessForm()

        return render(request, 'surver/form.html', {
            'form': form,
        })
    else:
        return HttpResponseBadRequest('You are not owner in this surver.')
