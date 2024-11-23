from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class Vote(TemplateView):
    # 投票ページを表示
    def get(self, request):
        
        # コードを追加 セッションに投票データがある場合はすでに投票していると判断して、already_voted にリダイレクトする
        # リダイレクトのコードは 
        # return redirect('already_voted')
        # という形でかく


        return render(request, 'vote_page.html')
    
    # 投票ボタンが押された時の処理
    def post(self, request):
        vote = request.POST.get('vote') # 投票した選択肢を取得　例: 'A'
        
        # コードを追加 変数 vote に格納されている投票データをセッションに保存する
    


        return redirect('result')

class Result(TemplateView):
    # セッションから投票した選択肢を取得して結果ページに表示
    def get(self, request):
        
        # コードを追加 セッションから投票データを取得して、変数 vote に格納する
        vote = ""   # "" の部分をセッションから取得した投票データに変更する



        context = {'vote': vote}
        return render(request, 'result_page.html', context)
    

# 演習２の時に使用
class AlreadyVoted(TemplateView):
    
    # すでに投票している場合のページを表示
    def get(self, request):
        return render(request, 'already_voted.html')
    
    def post(self, request):
        if 'reset' in request.POST:

            # コードを追加 セッションをリセットする
            
            
            print("aaaa")
        return redirect('vote')