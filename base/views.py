from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {
        'index': True,
        'title': u'TelcoOAM 관리',
        })

#def list_users(request):
#    users = 'test'
#    return HttpResponse(json.dumps(users))
