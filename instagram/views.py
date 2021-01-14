from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, ArchiveIndexView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

from .forms import PostForm


# form test view
def post_new(request):
    # 2. 폼에 입력된 데이터와 파일에 대한 분기
    if request.method == 'POST':
        # POST 인자는 request.POST와 request.FILES를 제공받아야 함.
        form = PostForm(request.POST, request.FILES)
        # 인자로 받은 값에 대해 유효성 검증 수행
        if form.is_valid():  # 검증이 성공하면 True 리턴
            # 검증에 성공한 값들을 dict타입으로 제공받음
            # 검증에 성공한 값을 제공 받으면, Django Form의 역할은 끝
            # 필요에 따라, 이 값을 DB에 insert.
            post = form.save()
            return redirect(post)
        else: # 검증에 실패하면, form.errors와 form.각필드.errors에 오류 정보 저장
            form.errors
    else:  # 1. GET 요청일 때의 분기
        form = PostForm()
    return render(request, 'instagram/post_form.html', {
        'form': form
    })


# CBV에 장식자 사용..
# @method_decorator(login_required, name='dispatch') 잘 안씀..
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()


# post_list = ListView.as_view(model=Post, paginate_by=10)

# @login_required
# def post_list(request):
#     # request.GET
#     # request.POST
#     # request.FILES
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     # print(f"request : {str(request)}\n request.GET : {request.GET}\n, q : {q}")
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })


class PostDetailView(DetailView):
    model = Post

    # queryset = Post.objects.filter(is_published=True)

    def get_queryset(self):
        qs = super().get_queryset()  # override할 때 부모의 함수를 일단 호출
        if not self.request.user.is_authenticated:  # 로그인이 되어있지 않다면
            qs = qs.filter(is_published=True)  # 공개된 포스트만 볼 수 있도록
        return qs


post_detail = PostDetailView.as_view()

# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_published=True))

# 함수형 -> 클래스형으로 구현
# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # shortcut을 활용해서 위 처럼 작성할 수 있다.
#     # try:
#     #     post = Post.objects.get(pk=pk)  # 필드:인자값, # DoesNotExist 예외
#     # except:
#     #     raise Http404
#     return render(request, 'instagram/post_detail.html', {
#         'post': post
#     })


post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)
# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives")
