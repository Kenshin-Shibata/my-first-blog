from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

#post_list関数を作る
def post_list(request): #requestを引数とする
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts}) #テンプレートを組み立てるrender関数を呼び出して得た値をreturnする

