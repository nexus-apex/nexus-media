import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Content, MediaChannel, PublishSchedule


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['content_count'] = Content.objects.count()
    ctx['content_article'] = Content.objects.filter(content_type='article').count()
    ctx['content_video'] = Content.objects.filter(content_type='video').count()
    ctx['content_podcast'] = Content.objects.filter(content_type='podcast').count()
    ctx['mediachannel_count'] = MediaChannel.objects.count()
    ctx['mediachannel_website'] = MediaChannel.objects.filter(platform='website').count()
    ctx['mediachannel_youtube'] = MediaChannel.objects.filter(platform='youtube').count()
    ctx['mediachannel_podcast'] = MediaChannel.objects.filter(platform='podcast').count()
    ctx['publishschedule_count'] = PublishSchedule.objects.count()
    ctx['publishschedule_scheduled'] = PublishSchedule.objects.filter(status='scheduled').count()
    ctx['publishschedule_published'] = PublishSchedule.objects.filter(status='published').count()
    ctx['publishschedule_cancelled'] = PublishSchedule.objects.filter(status='cancelled').count()
    ctx['recent'] = Content.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def content_list(request):
    qs = Content.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(content_type=status_filter)
    return render(request, 'content_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def content_create(request):
    if request.method == 'POST':
        obj = Content()
        obj.title = request.POST.get('title', '')
        obj.content_type = request.POST.get('content_type', '')
        obj.author = request.POST.get('author', '')
        obj.status = request.POST.get('status', '')
        obj.views = request.POST.get('views') or 0
        obj.published_date = request.POST.get('published_date') or None
        obj.category = request.POST.get('category', '')
        obj.save()
        return redirect('/contents/')
    return render(request, 'content_form.html', {'editing': False})


@login_required
def content_edit(request, pk):
    obj = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.content_type = request.POST.get('content_type', '')
        obj.author = request.POST.get('author', '')
        obj.status = request.POST.get('status', '')
        obj.views = request.POST.get('views') or 0
        obj.published_date = request.POST.get('published_date') or None
        obj.category = request.POST.get('category', '')
        obj.save()
        return redirect('/contents/')
    return render(request, 'content_form.html', {'record': obj, 'editing': True})


@login_required
def content_delete(request, pk):
    obj = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/contents/')


@login_required
def mediachannel_list(request):
    qs = MediaChannel.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(platform=status_filter)
    return render(request, 'mediachannel_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def mediachannel_create(request):
    if request.method == 'POST':
        obj = MediaChannel()
        obj.name = request.POST.get('name', '')
        obj.platform = request.POST.get('platform', '')
        obj.subscribers = request.POST.get('subscribers') or 0
        obj.status = request.POST.get('status', '')
        obj.content_count = request.POST.get('content_count') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/mediachannels/')
    return render(request, 'mediachannel_form.html', {'editing': False})


@login_required
def mediachannel_edit(request, pk):
    obj = get_object_or_404(MediaChannel, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.platform = request.POST.get('platform', '')
        obj.subscribers = request.POST.get('subscribers') or 0
        obj.status = request.POST.get('status', '')
        obj.content_count = request.POST.get('content_count') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/mediachannels/')
    return render(request, 'mediachannel_form.html', {'record': obj, 'editing': True})


@login_required
def mediachannel_delete(request, pk):
    obj = get_object_or_404(MediaChannel, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/mediachannels/')


@login_required
def publishschedule_list(request):
    qs = PublishSchedule.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(content_title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'publishschedule_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def publishschedule_create(request):
    if request.method == 'POST':
        obj = PublishSchedule()
        obj.content_title = request.POST.get('content_title', '')
        obj.channel_name = request.POST.get('channel_name', '')
        obj.scheduled_date = request.POST.get('scheduled_date') or None
        obj.status = request.POST.get('status', '')
        obj.published_url = request.POST.get('published_url', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/publishschedules/')
    return render(request, 'publishschedule_form.html', {'editing': False})


@login_required
def publishschedule_edit(request, pk):
    obj = get_object_or_404(PublishSchedule, pk=pk)
    if request.method == 'POST':
        obj.content_title = request.POST.get('content_title', '')
        obj.channel_name = request.POST.get('channel_name', '')
        obj.scheduled_date = request.POST.get('scheduled_date') or None
        obj.status = request.POST.get('status', '')
        obj.published_url = request.POST.get('published_url', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/publishschedules/')
    return render(request, 'publishschedule_form.html', {'record': obj, 'editing': True})


@login_required
def publishschedule_delete(request, pk):
    obj = get_object_or_404(PublishSchedule, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/publishschedules/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['content_count'] = Content.objects.count()
    data['mediachannel_count'] = MediaChannel.objects.count()
    data['publishschedule_count'] = PublishSchedule.objects.count()
    return JsonResponse(data)
