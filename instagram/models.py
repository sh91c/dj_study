from django.db import models


class Post(models.Model):
    message = models.TextField()

    # pillow 패키지 사용 추천, imagemagic도 있음
    # 속성 upload_to : media_root 밑에 하위 디렉토리를 설정할 수 있음
    #   - 문자열로 지정 : 파일을 저장할 '중간 디렉토리 경로' 로서 활용
    #   - 함수로 지정 : '중간 디렉토리 경로' 및 '파일명' 까지 결정 가능
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_published = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString과 유사하게 객체에 대한 문자열 표현
    def __str__(self):
        # return f" Custom Post object ({self.id})"
        return self.message

    # 인자 없는 속성(함수), model단에서 구현
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메세지 글자 수'