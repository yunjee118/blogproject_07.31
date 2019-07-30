from django.shortcuts import render
#포트폴리오

def portfolio(request):
    return render(request, 'portfolio.html')
