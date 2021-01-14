from django.test import TestCase
from django.shortcuts import get_object_or_404, render

# Post = 'import PostModel'
# Article = 'import ArticleModel'
#
#
# # 함수를 통해, 동일한 View 함수를 생성하기
# def generate_view_fn(model):
#     def view_fn(request, id):
#         instance = get_object_or_404(model, id=id)
#         instance_name = model._meta.model_name
#         template_name = f"P{model._meta.app_label}/{instance_name}_detail.html"
#         return render(request, template_name, {
#             instance_name: instance
#         })
#
#     return view_fn
#
#
# post_detail = generate_view_fn(Post)
# article_detail = generate_view_fn(Article)