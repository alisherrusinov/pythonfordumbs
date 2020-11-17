from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import LessonModel, CurrentLesson


# Create your views here.
def index(request):
    """Функция которая редиректит на текущий урок пользователя"""
    if request.user.is_authenticated:
        username = request.user.username
        try:
            curr_lesson = CurrentLesson.objects.get(username=username)
        except CurrentLesson.DoesNotExist:
            CurrentLesson.objects.create(username=username, attached_to=LessonModel.objects.all()[0])
            curr_lesson = CurrentLesson.objects.get(username=username)

        return HttpResponseRedirect(
            reverse('course:lesson_detail', kwargs={'lesson_slug': curr_lesson.attached_to.slug})
        )
    else:
        return HttpResponse('login first')


def lesson_detail(request, lesson_slug):
    """Страница урока"""
    if request.user.is_authenticated:
        username = request.user.username
        lesson = get_object_or_404(LessonModel, slug=lesson_slug)
        user_less = CurrentLesson.objects.get(username=username)
        if user_less.attached_to.id > lesson.id:
            pass
        else:
            user_less.attached_to = lesson
            user_less.save(update_fields=['attached_to'])

        link_models = lesson.attachedlinkmodel_set.all()
        links = []
        for link in link_models:
            links.append(link.link)

        return render(
            request,
            'course/lesson_detail.html',
            {'title': lesson.title,
             'links': links,
             'video': lesson.embed_url,
             'script': lesson.script,
             'lesson': lesson,
             }
        )
    else:
        lesson = get_object_or_404(LessonModel, slug=lesson_slug)
        return HttpResponse('hello')
