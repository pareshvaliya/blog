from django.shortcuts import render,redirect,get_object_or_404
import datetime
from myapp.models import Post,Comment
from myapp.forms import CommentForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

# Create your views here.
def index(request):
	#process the request here
	# p is queryset which has all the objects
	p = Post.objects.all()
	context = {'posts':p,'name' : 'Paresh','time':datetime.datetime.now()}
	return render(request,'index.html',context)
	#request,template,dict

# here the primary key is stored in pk variable
'''def detail(request,pk):
	# to get current object of Post
	d = Post.objects.get(pk = pk)
	context = {'post':d}
	# it redirects to the detail.html
	return render(request,'detail.html',context)
'''
# this detail function replace above detail 
# no need of above detail function
@login_required
def detail(request,pk):
    d = Post.objects.get(pk = pk)
    comments = Comment.objects.filter(post = d)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            comment  = form.cleaned_data['comment']
            # print(comment,pk)
            #save comment in Comment model that is in data base
            c = Comment(post = d,comment = comment,user = request.user)
            c.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            context = {'post':d,'form':form,'comments':comments}
            return render(request, 'detail.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()
    context = {'post':d,'form':form,'comments':comments}
    return render(request, 'detail.html', context)

class PostCreate(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','description','image']
	success_url = '/'

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super().form_valid(form)


def like(request):
	if request.is_ajax():
		i = request.GET.get('i')
		p = Post.objects.get(pk = i)
		p.likes += 1
		p.save()
		data = {'i':p.likes}
		return JsonResponse(data)