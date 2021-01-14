from django.urls import path, re_path, register_converter

from . import views

app_name = 'instagram'  # URL Reverse에서 namespace 역할을 하게 됨.


# Custom Converter
class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


# 커스텀 컨버터 등록
register_converter(YearConverter, 'year')

urlpatterns = [
    path('', views.post_list, name='post_list'),

    # form test
    path('new/', views.post_new, name='post_new'),

    # URL Captured Value, 아래 두개는 의미가 같음
    path('<int:pk>/', views.post_detail, name='post_detail'),  # 적절하게 형변환
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),  # 정규식, 문자열로 입력받음

    # 정규표현식 예시
    # path('archives/<int:year>/', views.archives_year), 난 20xx년대로 시작하고 숫자 4개만 받고싶다!
    # re_path(r'archives/(?P<year>\d+)/', views.archives_year), # <int:pk> 와 같다
    # re_path(r'archives/(?P<year>\d{4})/', views.archives_year), # 4개를 받음
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year), # 완성
    # path('archives/<year:year>/', views.archives_year), # 커스텀컨버터이름 : 인자로넘겨줄변수명
    path('archive/', views.post_archive, name='post_archive'),
]

