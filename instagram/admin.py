from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag


# 첫 번째 방법
# admin.site.register(Post)

# 두 번째 방법
# class PostAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Post, PostAdmin)


# 세 번째 방법 *
@admin.register(Post)  # Wrapping
class PostAdmin(admin.ModelAdmin):
    # list_display & _link : 해당 모델의 속성들을 어드민 페이지에서 출력할 수있음, 링크 또한 복수개 가능
    list_display = ['id', 'message', 'created_at', 'updated_at', 'message_length', 'is_published', 'photo_tag']
    # message_length 멤버 함수 또한 속성으로 사용가능
    list_display_links = ['message']
    # 어드민 페이지에 message 필드에 대한 검색창 활성화
    search_fields = ['message']
    # 우측에 필터 옵션 활성화
    list_filter = ['created_at', 'is_published']

    def photo_tag(self, post):
        if post.photo:
            # post.photo.url  # 해당 URL을 얻을 수 있다.
            # mark_safe : 태그를 활성화 시킬 수 있음 (안전하니까)
            return mark_safe(f'<img src="{post.photo.url}" style="width: 70px"/>')
        return None

    # message_length를 model에서 구현하느냐, 어드민단에서 구현하느냐..
    # 둘다 가능하다. 자주 쓰는 로직은 model, 어드민 단에서만 쓸 것이라면 아래처럼 구현
    def message_length(self, post):  # post는 instance를 말하는 듯..
        return f"{len(post.message)} 글자"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
