from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myview(request):
    # msg = str(request.COOKIES)
    num = request.session.get('num_vi', 0) + 1
    request.session['num_vi'] = num
    if num > 4: del(request.session['num_vi'])

    return HttpResponse("view count="+str(num))