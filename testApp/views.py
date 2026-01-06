from django.shortcuts import render, redirect # redirect を追加
from .models import Post
from django import forms # 簡易的なフォームを作るために追加

# 実験用に簡易的なフォームクラスを定義（forms.pyがない場合でも動きます）
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content'] # Postモデルに 'content' という項目があると仮定

def timeline(request):
    posts = Post.objects.select_related('author').all().order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'timeline.html', context)

def post_list(request):
    posts = Post.objects.select_related('author').order_by('-created_at') 
    return render(request, 'post_list.html', {'posts': posts})

# ここを修正しました！
def post_new(request):
    if request.method == "POST":
        # 送信されたデータを受け取る（実験2ではここでエラーが出るはず）
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # ログインユーザーを作者にする
            post.save()
            return redirect('timeline')
    else:
        # 画面を開いたとき：空のフォームを作成する
        form = PostForm()
    
    # 作成した form をテンプレートに渡す
    return render(request, 'post_new.html', {'form': form})
