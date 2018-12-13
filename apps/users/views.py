# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import User

# Create your views here.

def index(request):
	users = User.objects.all()
	context = {'users' : []}
	for user in users:
		context['users'].append({
			'id' : user.id,
			'full_name' : user.first_name + " " + user.last_name,
			'email' : user.email,
			'created_at' : user.created_at.strftime('%B %e, %Y')
		})
	return render(request, 'users/index.html', context)

# def show(request, id):
# 	id = int(id)
# 	user = User.objects.get(id = id)
# 	if request.method == 'GET':
# 		context = {
# 			'id' : id,
# 			'full_name' : user.first_name + ' ' + user.last_name,
			# 'email' : user.email,
# 			'created_at' : user.created_at.strftime('%B %e, %Y')
# 		}
# 		return render(request, 'users/user.html', context)
# 	elif request.method == 'POST':
# 		errors = User.objects.basic_validator(request.POST)
# 		if len(errors):
# 			for tag, error in errors.iteritems():
# 				messages.error(request, error, extra_tags = tag)
# 		    return redirect('/users/' + str(id) + '/edit/')
		
# 		user.first_name = request.POST['first_name']
# 		user.last_name = request.POST['last_name']
# 		user.email = request.POST['email']
# 		user.save()
# 		return redirect('/users/' + str(id))
def show(request, id):
    id = int(id)
    user = User.objects.get(id=id)
    if request.method == 'GET':
        context = {
            "id": id,
            "full_name": user.first_name + " " + user.last_name,
            "email": user.email,
            "created_at": user.created_at.strftime('%B %e, %Y')
        }
        return render(request, 'users/user.html', context)
    elif request.method == 'POST':
        # FORM VALIDATION
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/' + str(id) + '/edit/')
        
        # UPDATE DATABASE
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users/' + str(id))
def edit(request, id):
    id = int(id)
    user = User.objects.get(id=id)
    context = {
        "id": id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }
    return render(request, 'users/edit.html', context)
	

def new(request):
    return render(request, 'users/new.html')


def create(request):
    if request.method == 'POST':

        # FORM VALIDATION
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('users:new'))

        # ADD TO DATABASE
        new_user_id = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email']).id
        
        return redirect('/users/' + str(new_user_id))
    else:
        return redirect(reverse('users:index'))


def destroy(request, id):
    id = int(id)
    User.objects.get(id=id).delete()
    return redirect(reverse('users:index'))


