from django.shortcuts import render,redirect
from task_tracker.models import Comment
from task_tracker.forms.comment_form import CommentModelForm


def show_all_comments(request):
    comments = Comment.objects.all() # тут делаем задачи в админ из базы
    context = {
        'comments': comments,
    }

    return render(request, 'comments.html', context=context)


def create_comment_form(request):
    context = {}
    if request.method == 'POST':

        form = CommentModelForm(request.POST, request.FILES)

        form.save()

        if form.is_valid():
            context['form'] = form

            return redirect('all_comments')
    else:
        form = CommentModelForm()
        context['form'] = form

    return render(request, 'comment_form.html', context=context)