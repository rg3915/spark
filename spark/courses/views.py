from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.urlresolvers import reverse_lazy as r
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from spark.authentication.models import Profile
from spark.courses.models import Classe, ClasseDetail
from spark.lectures.models import Lecture
from spark.videos.models import Video

CLASSES_NUM_PAGES = 10


@login_required
def classes(request):
    all_classes = Classe.objects.all()
    paginator = Paginator(all_classes, CLASSES_NUM_PAGES)
    classes = paginator.page(1)
    from_classe = -1
    if classes:
        from_classe = classes[0].id
    ctx = {
        'classes': classes,
        'from_classe': from_classe,
        'page': 1,
    }
    return render(request, 'courses/classes.html', ctx)


@login_required
def classe_detail(request, slug):
    classe = get_object_or_404(Classe, slug=slug)
    ctx = {'classe': classe}
    return render(request, 'courses/classe_detail.html', ctx)


@login_required
def subscribe(request, slug):
    classe = get_object_or_404(Classe, slug=slug)
    user = get_object_or_404(Profile, user=request.user)
    try:
        classedetail = ClasseDetail.objects.get(classe=classe, user=user)
        is_exist = True
    except Exception as e:
        classedetail = ClasseDetail(classe=classe, user=user)
        is_exist = False
    if not is_exist:
        classedetail.save()

    return HttpResponseRedirect(r('classes'))


@login_required
def lecture(request, slug):
    lectures = Lecture.objects.filter(course__slug=slug)
    videos = Video.objects.filter(course__slug=slug)
    ctx = {
        'lectures': lectures,
        'videos': videos,
    }
    return render(request, 'courses/lectures.html', ctx)


@login_required
def lecture_detail(request, slug, pk):
    lecture = Lecture.objects.get(course__slug=slug, pk=pk)
    ctx = {'lecture': lecture}
    return render(request, 'courses/lecture_detail.html', ctx)
