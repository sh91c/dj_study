"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# ------------------------------------------
# from django.conf import global_settings
# from config import settings
# --- 위 두개를 합친 것이 아래와 같음 ---
from django.conf import settings
# ------------------------------------------
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView


# view를 상속받아 따로 만든 TemplateView
class RootView(TemplateView):
    template_name = 'root.html'


urlpatterns = [
    # django-admin-honeypot 앱을 통해, 가짜 admin 페이지를 노출 시킬수 있다.
    path('', RedirectView.as_view(
        # url='/instagram/', # url를 사용시
        pattern_name='instagram:post_list',  # App.urls.patterns의 namespace를 활용 시 (선호)
    ), name='root'),
    # path('', RedirectView.as_view(url='/instagram/'), name='root'),
    # path('', RootView.as_view(), name='root'),
    # path('', TemplateView.as_view(template_name='root.html'), name='root'), # 또는 위처럼 view를 상속받아서 따로 만들어 사용 가능
    path('admin/', admin.site.urls),  # URL reverse : 임의의 주소를 변경해도 내부에서 찾아가는 기능
    path('accounts/', include('accounts.urls')),
    path('instagram/', include('instagram.urls')),
]

if settings.DEBUG:
    # settings.MEDIA_URL -> URL 접근
    # settings.MEDIA_ROOT -> 저장 경로
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 접근시 조회 가능
    # django-debug-toolbar
    import debug_toolbar

    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),
    ]
