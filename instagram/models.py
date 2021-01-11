from django.db import models


class Post(models.Model):
    message = models.TextField()
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