from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from bs4 import BeautifulSoup
def index(request):
    if request.method == 'POST':
        content=request.POST['text']
        soup=BeautifulSoup(content,"html.parser")
        paras=soup.find('p').get_text()
        data={'entered text':content,
        'returneddata':paras}
        return JsonResponse(data,safe=False)
    else:
        return (render(request,'index.html'))