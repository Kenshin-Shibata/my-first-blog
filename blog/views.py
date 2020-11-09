from django.shortcuts import render

# Create your views here.

#post_list関数を作る
def post_list(request): #requestを引数とする
    return render(request, 'blog/post_list.html', {}) #テンプレートを組み立てるrender関数を呼び出して得た値をreturnする

