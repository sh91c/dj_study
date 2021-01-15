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


# django 외 파이썬 테스트

# class Person:
#     def greeting(self):
#         print('안녕하세요')
#
#
# class University:
#     def manage_credit(self):
#         print('학점 관리')
#
#
# class Undergraduate(Person, University):
#     def study(self):
#         print('공부하기')
#
# james = Undergraduate()
# james.greeting()
# james.manage_credit()
# james.study()

# 다이아몬드 상속 == 지옥
class A:
    def greeting(self):
        print('Hi Im A')


class B:
    def greeting(self):
        print('Hi Im B')




class C:
    def greeting(self):
        print('Hi Im C')
        self.d_method()

class D(B,C):
    def d_method(self):
        print('d_method 호출')

    def c_method(self):
        c = C()
        c.greeting()

x = D()
x.greeting()
# 파이썬은 메소드 탐색 순서 Method Resolution Order, MRO)를 따른다.
print(D.__mro__)