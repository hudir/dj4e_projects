from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myview(request):
    # msg = str(request.COOKIES)
    num = request.session.get('num_vi', 0) + 1
    request.session['num_vi'] = num
    if num > 4: del(request.session['num_vi'])
    resp=HttpResponse("view count="+str(num))
    resp.set_cookie('dj4e_cookie', '60e592a5', max_age=1000)
    return resp