from django.shortcuts import render
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm, FindForm, CheckForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import Q, Count,Sum,Avg,Min,Max


class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend


def index(request):
    data = Friend.objects.all().order_by('age').reverse()
    params = {
        'title': 'Hello',
        'message':'',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

# create model(modelsForm)
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
    return render(request, 'hello/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id':num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from hello_friend'
        if (msg != ''):
            sql += ' where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()

    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)

def check(request):
    params = {
        'title': 'Hello',
        'message': 'check validation',
        'form': FriendForm(),
    }
    if (request.method == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'hello/check.html', params)


'''
# create model(1)
def create(request):
    params = {
        'title':'Hello',
        'form': HelloForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        gender = 'gender' in request.POST
        age = int(request.POST['age'])
        birth = request.POST['birthday']
        friend = Friend(name=name,mail=mail,gender=gender,age=age,birthday=birth)
        friend.save()
        return redirect(to='/hello')
    return render(request, 'hello/create.html', params)
'''