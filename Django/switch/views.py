from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from switch.models import Switch
from extra.main import xpru
#from django.contrib.auth.decorators import login_required
#@login_required(login_url="/login/")
def index(request):
    jpgids = [True,True]
    for i in range(1,3):
        l = get_object_or_404(Switch,pk = i)
        id= l.status
        if id:
            jpgids[i-1] = True
        else:
            jpgids[i-1] = False
    return render(request,'switch/index.html',{'jpgids':jpgids})

def detail(request,pk):

    gp = ['\xfe','\xfd','\x01','\x02']
    l = get_object_or_404(Switch,pk = pk)
    st= l.status
    pk = int(pk)
    if st:
        st = True
        xpru(gp[pk-1])
        l.status = 0
        l.save()
    else:
        st = False
        xpru(gp[pk+1])
        l.status = 1
        l.save()

    jpgids = [True,True]
    for i in range(1,3):
        l = get_object_or_404(Switch,pk = i)
        id= l.status
        if id:
            jpgids[i-1] = True
        else:
            jpgids[i-1] = False
    return render(request,'switch/index.html',{'jpgids':jpgids})
