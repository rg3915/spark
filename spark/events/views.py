import json
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import csrf
from django.template.loader import render_to_string

from spark.decorators import ajax_required
from spark.events.models import Event

EVENTS_NUM_PAGES = 10


@login_required
def events(request):
    all_events = Event.objects.all()  # get_events()
    paginator = Paginator(all_events, EVENTS_NUM_PAGES)
    events = paginator.page(1)
    from_event = -1
    if events:
        from_event = events[0].id
    return render(request, 'events/events.html', {
        'events': events,
        'from_event': from_event,
        'page': 1,
    })


# def event(request, pk):
#     event = get_object_or_404(event, pk=pk)
#     return render(request, 'events/event.html', {'event': event})


@login_required
@ajax_required
def load(request):
    from_event = request.GET.get('from_event')
    page = request.GET.get('page')
    event_source = request.GET.get('event_source')
    all_events = Event.get_events(from_event)
    if event_source != 'all':
        all_events = all_events.filter(user__id=event_source)
    paginator = Paginator(all_events, EVENTS_NUM_PAGES)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        return HttpResponseBadRequest()
    except EmptyPage:
        events = []
    html = ''
    csrf_token = (csrf(request)['csrf_token'])
    for event in events:
        html = '{0}{1}'.format(html,
                               render_to_string('events/partial_event.html',
                                                {
                                                    'event': event,
                                                    'user': request.user,
                                                    'csrf_token': csrf_token
                                                }))

    return HttpResponse(html)


def _html_events(last_event, user, csrf_token, event_source='all'):
    events = Event.get_events_after(last_event)
    if event_source != 'all':
        events = events.filter(user__id=event_source)
    html = ''
    for event in events:
        html = '{0}{1}'.format(html,
                               render_to_string('events/partial_event.html',
                                                {
                                                    'event': event,
                                                    'user': user,
                                                    'csrf_token': csrf_token
                                                }))

    return html


@login_required
@ajax_required
def load_new(request):
    last_event = request.GET.get('last_event')
    user = request.user
    csrf_token = (csrf(request)['csrf_token'])
    html = _html_events(last_event, user, csrf_token)
    return HttpResponse(html)


@login_required
@ajax_required
def check(request):
    last_event = request.GET.get('last_event')
    event_source = request.GET.get('event_source')
    events = Event.get_events_after(last_event)
    if event_source != 'all':
        events = events.filter(user__id=event_source)
    count = events.count()
    return HttpResponse(count)


@login_required
@ajax_required
def post(request):
    last_event = request.POST.get('last_event')
    user = request.user
    csrf_token = (csrf(request)['csrf_token'])
    event = Event()
    event.user = user
    title = request.POST['title']
    title = title.strip()
    date_start_ = request.POST['date_start']
    event.date_start = datetime.strptime(date_start_, '%d/%m/%Y')
    start_ = request.POST['start']
    event.start = datetime.strptime(start_, '%H:%M')
    event.description = request.POST['description']
    event.address = request.POST['address']
    print(request.POST['date_start'], request.POST['start'])
    if len(title) > 0:
        event.title = title[:255]
        event.save()
    html = _html_events(last_event, user, csrf_token)
    return HttpResponse(html)


@login_required
@ajax_required
def like(request):
    event_id = request.POST['event']
    event = event.objects.get(pk=event_id)
    user = request.user
    like = Activity.objects.filter(activity_type=Activity.LIKE, event=event_id,
                                   user=user)
    if like:
        user.profile.unotify_liked(event)
        like.delete()

    else:
        like = Activity(activity_type=Activity.LIKE, event=event_id, user=user)
        like.save()
        user.profile.notify_liked(event)

    return HttpResponse(event.calculate_likes())


# @login_required
# @ajax_required
# def comment(request):
#     if request.method == 'POST':
#         feed_id = request.POST['feed']
#         feed = Feed.objects.get(pk=feed_id)
#         post = request.POST['post']
#         post = post.strip()
#         if len(post) > 0:
#             post = post[:255]
#             user = request.user
#             feed.comment(user=user, post=post)
#             user.profile.notify_commented(feed)
#             user.profile.notify_also_commented(feed)
#         return render(request, 'feeds/partial_feed_comments.html',
#                       {'feed': feed})

#     else:
#         feed_id = request.GET.get('feed')
#         feed = Feed.objects.get(pk=feed_id)
#         return render(request, 'feeds/partial_feed_comments.html',
#                       {'feed': feed})


# @login_required
# @ajax_required
# def update(request):
#     first_feed = request.GET.get('first_feed')
#     last_feed = request.GET.get('last_feed')
#     feed_source = request.GET.get('feed_source')
#     feeds = Feed.get_feeds().filter(id__range=(last_feed, first_feed))
#     if feed_source != 'all':
#         feeds = feeds.filter(user__id=feed_source)
#     dump = {}
#     for feed in feeds:
#         dump[feed.pk] = {'likes': feed.likes, 'comments': feed.comments}
#     data = json.dumps(dump)
#     return HttpResponse(data, content_type='application/json')


# @login_required
# @ajax_required
# def track_comments(request):
#     feed_id = request.GET.get('feed')
#     feed = Feed.objects.get(pk=feed_id)
# return render(request, 'feeds/partial_feed_comments.html', {'feed':
# feed})


# @login_required
# @ajax_required
# def remove(request):
#     try:
#         feed_id = request.POST.get('feed')
#         feed = Feed.objects.get(pk=feed_id)
#         if feed.user == request.user:
#             likes = feed.get_likes()
#             parent = feed.parent
#             for like in likes:
#                 like.delete()
#             feed.delete()
#             if parent:
#                 parent.calculate_comments()
#             return HttpResponse()
#         else:
#             return HttpResponseForbidden()
#     except Exception:
#         return HttpResponseBadRequest()
