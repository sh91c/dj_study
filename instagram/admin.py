from django.contrib import admin
from .models import Post


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
    list_display = ['id', 'message', 'created_at', 'updated_at', 'message_length', 'is_published']
    # message_length 멤버 함수 또한 속성으로 사용가능
    list_display_links = ['message']
    # 어드민 페이지에 message 필드에 대한 검색창 활성화
    search_fields = ['message']
    # 우측에 필터 옵션 활성화
    list_filter = ['created_at', 'is_published']

    # message_length를 model에서 구현하느냐, 어드민단에서 구현하느냐..
    # 둘다 가능하다. 자주 쓰는 로직은 model, 어드민 단에서만 쓸 것이라면 아래처럼 구현
    def message_length(self, post):
        return f"{len(post.message)} 글자"
