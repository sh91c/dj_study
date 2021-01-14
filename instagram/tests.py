from .models import Post

# qs = Post.objects.all().order_by('-id')
# for post in qs:
#     print("id: {id}, message: {message}, created_at: {created_at}".format(**post.__dict__))

# queryset은 chaining을 지원
# field__icontains : 대소 구분X 포함된 문자열 검색
# field__startswith : 찾고자하는 문자열로 시작되는 문자열
# query = '메세지' # 검색어
# qs = Post.objects.all()\
#     .filter(message__icontains=query)\
#     .order_by('-id')
# print(qs)

# qs = Post.objects.all()
# print(qs.first())
# print(qs.last())

# OR을 사용할 때 Q 객체 사용
# from django.db.models import Q
# query = '메세지'
# qs = Post.objects.all()
# # qs = qs.filter(id__gte=2, message__icontains=query) # WHERE ~ AND 절
# # qs = qs.filter(Q(id__gte=2) & Q(message__icontains=query)) Q 객체를 사용한 WHERE ~ AND 절
# qs = qs.filter(Q(id__gte=2) | Q(message__icontains=query)) # WHERE ~ OR 절
# print(qs)

###############################################################
# URL Reverse
from django.urls import reverse
from django.shortcuts import resolve_url
print(reverse('instagram:post_list'))
print(reverse('instagram:post_detail', args=[123992342349]))
print(resolve_url('instagram:post_detail', pk=1231231212451254))
