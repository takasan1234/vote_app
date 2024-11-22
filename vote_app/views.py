from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class Vote(TemplateView):
    # 投票ページを表示
    def get(self, request):
        if request.session.get("vote") != None:
            return redirect('already_voted')
        return render(request, 'vote_page.html')
    # 投票ページで投票した選択肢をセッションに保存
    def post(self, request):
        vote = request.POST.get('vote') # 投票した選択肢を取得　例: 'A'
        request.session['vote'] = vote  # セッションに投票した選択肢を保存
        return redirect('result')

class Result(TemplateView):
    # セッションから投票した選択肢を取得して結果ページに表示
    def get(self, request):
        vote = request.session.get('vote')
        context = {'vote': vote}
        return render(request, 'result_page.html', context)
    


# 演習２の時に使用

class AlreadyVoted(TemplateView):
    # すでに投票している場合のページを表示
    def get(self, request):
        print("already_voted get")
        return render(request, 'already_voted.html')
    def post(self, request):
        if 'reset' in request.POST:
            request.session.pop('vote', None)
        return redirect('vote')