from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

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
def create_channel(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    surver = category.surver

    if request.method == "POST":
        form = ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.category = category
            channel.save()
            return redirect('surver:detail', surver.pk, channel.pk)
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
        message.user = request.user
        message.category = channel
        message.save()
        return redirect('surver:detail', surver.pk, channel.pk)


# Read
@login_required
def detail(request, surver_pk, channel_pk):
    user = request.user
    survers = user.survers.all()

    # 사용자가 특정 서버에 들어가있고, 채널이 있는 경우
    if survers and surver_pk and channel_pk:
        state1 = 1
        state2 = 1
        
        this_surver = get_object_or_404(Surver, pk=surver_pk)
        this_channel = get_object_or_404(Channel, pk=channel_pk)

        form = MessageForm()
        messages = this_channel.messages.all()
        
        return render(request, 'surver/detail.html', {
            'survers': survers,
            'state1': state1,
            'state2': state2,
            'this_surver': this_surver,
            'this_channel': this_channel,
            'form': form,
            'messages': messages,
        })
    # 사용자가 특정 서버에 들어가있고, 채널이 없는 경우
    elif not channel_pk:
        print('여기1')
        state1 = 1
        state2 = 0
        this_surver = get_object_or_404(Surver, pk=surver_pk)
        return render(request, 'surver/detail.html', {
            'survers': survers,
            'state1': state1,
            'state2': state2,
            'this_surver': this_surver,
        })
    # 사용자가 아무 서버에도 들어가 있지 않을 경우
    else:
        print('여기2')
        state1 = 0
        state2 = 1
        return render(request, 'surver/detail.html', {
            'state1': state1,
            'state2': state2,
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
def delete_surver(request, surver_pk):
    pass

    
def delete_category(request, category_pk):
    pass


def delete_channel(request, channel_pk):
    pass


def delete_message(request, message_pk):
    pass
    
    
def reaction(request, message_pk):
    pass
