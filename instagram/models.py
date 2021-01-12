from django.db import models

### !!! WARNING !!! ###
# from django.contrib.auth.models import User
# => 이렇게 적용되지만 보장되는 방법은 아님. 장고의 유저 모델이 변경될 수 있기 때문에.. 확실한 방법이라고 할 수 없다.
# => 만약 앱 내에서 User 모델을 새로 만들었다면 프로젝트 settings의 AUTH_USER_MODEL 변수를 통해 지정을 해야하고,
#    이 작업은 프로젝트 초기에 설정을 해야 삽질하지 않는다.
# ==> 제일 안전하고 확실한 장고 유저 모델 지정 방법은 아래 import 문처럼
from django.conf import settings


# ㄴ-> 해줘야함
# ==> 현재 활성화된 유저 모델을 얻을 수 있는 메소드 -> from django.contrib.auth import get_user_model
# ==> user = get_user_model
#######################


class Post(models.Model):
    # 장고의 올바른 User Model 불러오는 방법 : settings.AUTH_USER_MODEL
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()

    # pillow 패키지 사용 추천, imagemagic도 있음
    # 속성 upload_to : media_root 밑에 하위 디렉토리를 설정할 수 있음
    #   - 문자열로 지정 : 파일을 저장할 '중간 디렉토리 경로' 로서 활용
    #   - 함수로 지정 : '중간 디렉토리 경로' 및 '파일명' 까지 결정 가능
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_published = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tag_set = models.ManyToManyField('Tag', blank=True)  # 인터프리터라서 Tag를 참조하기 위해 문자열로 지정

    # Java의 toString과 유사하게 객체에 대한 문자열 표현
    def __str__(self):
        # return f" Custom Post object ({self.id})"
        return self.message

    class Meta:
        ordering = ['-id']

    # 인자 없는 속성(함수), model단에서 구현
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메세지 글자 수'


class Comment(models.Model):
    # 외래키 지정 시 post_id 필드가 생성된다.
    post = models.ForeignKey(Post,  # 1. 'Post' 문자열 가능, 2. '다른앱.모델명' 가능
                             on_delete=models.CASCADE,
                             limit_choices_to={'is_published': True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name