from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from shopnow.apps.product.forms import productform

@login_required(login_url='/login')
def view_product(request):
    message  = "Agregar Producto"
    form = productform()
    ctx = {"message":message, "form":form}
    return render_to_response('product/addproduct.html',ctx,context_instance=RequestContext(request))
