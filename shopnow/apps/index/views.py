from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def view_index(request):
    message = 'Bienvenido a shopnow'
    ctx = {'message':message}
    return render_to_response('index/index.html', ctx, context_instance=RequestContext(request))
