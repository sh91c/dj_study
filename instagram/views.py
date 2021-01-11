from django.shortcuts import render
from .models import Post


def post_list(request):
    # request.GET
    # request.POST
    # request.FILES
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    # print(f"request : {str(request)}\n request.GET : {request.GET}\n, q : {q}")
    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })
