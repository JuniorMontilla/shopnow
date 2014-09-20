from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required

#profile imports
from shopnow.apps.profile.forms import loginform, registerform, profileform
from  shopnow.apps.profile.models import profile

def view_login(request):
    message = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usertoauthenticate = authenticate(username=username, password=password)
            if usertoauthenticate is not None and usertoauthenticate.is_active:
                login(request,usertoauthenticate)
                return HttpResponseRedirect('/profile/')
        else:
            message = 'Vuelve a intentarlo'
            ctx = {'message': message, 'form':form }
            return render_to_response('profile/login.html', ctx, context_instance=RequestContext(request))

    form = loginform()
    ctx = {'message': message, 'form':form }
    return render_to_response('profile/login.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def view_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def view_register(request):
    message = ''
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            username  =  User.username = form.cleaned_data['username']
            first_name = User.first_name = form.cleaned_data['first_name']
            last_name = User.lastname_name = form.cleaned_data['last_name']
            email = User.email = form.cleaned_data['email']
            password = User.password = form.cleaned_data['password']
            createuser = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            createuser.save()
            return HttpResponseRedirect('/login/')
	else:  
            message = 'Vuelve a intentarlo'
            ctx =  {'message':message, 'form':form}
            return render_to_response('profile/register.html', ctx, context_instance=RequestContext(request))

    form = registerform()
    ctx =  {'message':message, 'form':form}
    return render_to_response('profile/register.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def view_profile(request):
    message = ''
    if request.method == 'POST':
        form = profileform(request.POST, request.FILES)
        if form.is_valid():
            avatar =  form.cleaned_data['avatar']
            phone = form.cleaned_data['phone']
            cellphone = form.cleaned_data['cellphone']
            address =  form.cleaned_data['address']
            sex = form.cleaned_data['sex']
            dateofbirth = form.cleaned_data['dateofbirth']
            occupation = form.cleaned_data['occupation']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            province =  form.cleaned_data['province']
            municipality = form.cleaned_data['municipality']
            for usr in User.objects.all():
                profileobject = profile(user=usr)
            if avatar:
                profileobject.avatar = avatar
            profileobject.avatar = avatar
            profileobject.phone = phone
            profileobject.cellphone = cellphone
            profileobject.address = address
            profileobject.sex = sex
            profileobject.dateofbirth = dateofbirth
            profileobject.occupation = occupation
            profileobject.country = country
            profileobject.city = city
            profileobject.province = province
            profileobject.municipality  = municipality
            profileobject.save()
            message = 'Tu perfil ha sido creado'
            ctx ={'message':message}
            return render_to_response('profile/profile.html', ctx, context_instance=RequestContext(request))
        else:
            message = 'Vuelve a intentarlo'
            ctx ={'message':message, 'form':form}
            return render_to_response('profile/profile.html', ctx, context_instance=RequestContext(request))



    try:
        getprofiledata = profile.objects.get(id=request.user.get_profile().id)
        form = profileform(initial={

                                            'avatar':getprofiledata.avatar,
                                            'phone':getprofiledata.phone,
                                            'cellphone':getprofiledata.cellphone,
                                            'address':getprofiledata.address,
                                            'sex':getprofiledata.sex,
                                            'dateofbirth':getprofiledata.dateofbirth,
                                            'occupation':getprofiledata.occupation,
                                            'country':getprofiledata.country,
                                            'city':getprofiledata.city,
                                            'province':getprofiledata.province,
                                            'municipality':getprofiledata.municipality,

                                    })
    except profile.DoesNotExist:
        form = profileform()
        ctx ={'form':form}
        return render_to_response('profile/profile.html', ctx, context_instance=RequestContext(request))
