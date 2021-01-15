from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, ArchiveIndexView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)


post_new = PostCreateView.as_view()


# form test view
# @login_required
# def post_new(request):
#     # 2. 폼에 입력된 데이터와 파일에 대한 분기
#     if request.method == 'POST':
#         # POST 인자는 request.POST와 request.FILES를 제공받아야 함.
#         form = PostForm(request.POST, request.FILES)
#         # 인자로 받은 값에 대해 유효성 검증 수행
#         if form.is_valid():  # 검증이 성공하면 True 리턴
#             # 검증에 성공한 값들을 dict타입으로 제공받음
#             # 검증에 성공한 값을 제공 받으면, Django Form의 역할은 끝
#             # 필요에 따라, 이 값을 DB에 insert.
#             post = form.save(commit=False)  # 3.1. 새 포스팅을 save하기 전 commit=False로 DB에 커밋하기 전까지만 실행
#             post.author = request.user  # 3. 현재 로그인한 유저가 포스팅을 하는 것이 당연하기 때문에 request.user를 할당
#             post.save()  # 3.2. 과정을 끝냈으면 save
#             return redirect(post)
#     else:  # 1. GET 요청일 때의 분기
#         form = PostForm()
#     return render(request, 'instagram/post_form.html', {
#         'form': form
#     })

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()


# ModelForm update
# @login_required
# def post_edit(request, pk):
#     # update 할 때 해당 인스턴스를 가져와야하기 때문에 pk가 필요
#     post = get_object_or_404(Post, pk=pk)
#
#     # 글을 쓴 사용자인지 확인하려면, 현재 로그인된 유저와 글을 작성한 유저를 비교
#     # 팁 : 추후 장식자로 활용한다면 매번 뷰 함수마다 작성할 필요가 없음
#     if post.author != request.user:
#         messages.error(request, '작성자만 수정할 수 있습니다.')
#         return redirect(post)
#
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)  # 여기 instance 인자
#         if form.is_valid():
#             post = form.save()
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)  # 여기 instance 인자 => 수정될 내용이 바로 불러와짐
#     return render(request, 'instagram/post_form.html', {
#         'form': form
#     })


class PostDeleteView(DeleteView):
    model = Post

    # (이해 어려움..) 삭제 완료 후 success_url을 사용하는데
    # 일반적으로 reverse()는 동작하지 않는다. 이유는 파이썬은 소스코드가 임포트될 때 코드가 한줄씩 실행됨
    # success_url은 언제 수행되느냐.. 장고가 초기화 되기전 소스코드가 읽힐 때 수행됨(초기화 하기 전, 읽힐 때 수행되는건 프로젝트가 로딩되기 전)
    # 프로젝트 로딩이 끝나야지만 url reverse가 된다.(목록을 다 알아야지만 동작이 되기 때문에..)

    # 1. reverse는 동작하지 않는다.
    # success_url = reverse('instagram:post_list')
    # 3. reverse_lazy()를 사용하면 실제 이 값이 사용될 때 수행됌
    success_url = reverse_lazy('instagram:post_list')

    # 2. 함수를 재정의하면 실제 reverse가 필요할 때 반환이 된다.
    # def get_success_url(self):
    #     return reverse('instagram:post_list')



post_delete = PostDeleteView.as_view()


# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # 삭제 구현 : 장고의 삭제는 confirm을 확인 후 삭제된다.
#     if request.method == 'POST':
#         post.delete()
#         messages.success(request, '포스팅을 성공적으로 삭제했습니다.')
#         return redirect('instagram:post_list')
#     return render(request, 'instagram/post_confirm_delete.html', {
#         'post': post
#     })


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
