from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import * 
from . models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy,reverse
from . models import User 
from . forms import SignUpForm
from django.http import HttpResponseRedirect

####



class HomeView(TemplateView):
	template_name = 'blog/home.html'


class BlogCreateView(LoginRequiredMixin,CreateView):
	template_name = 'blog/blog_create.html'
	model = Blog 
	fields = ['title', 'content']
	

	def form_valid(self,form):
		form.instance.author = self.request.user 
		return super().form_valid(form)

class AllBlogView(ListView):
	model = Blog 
	template_name = 'blog/all_blogs.html'

class BlogDetailView(DetailView):
	model = Blog 
	template_name = 'blog/blog_details.html'

class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Blog 
	fields = ['title', 'content']
	template_name = 'blog/blog_update.html'
	
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Blog
	template_name = 'blog/blog_delete.html'
	success_url = reverse_lazy('blog:home') 
	def test_func(self):
		post = self.get_object()
		if(self.request.user == post.author):
			return True 
		return False	
	
def sign_up(request):
	if(request.method == 'POST'):
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blog:home'),)
	else:
		form = SignUpForm()
	return render(request, 'blog/sign_up.html', {'form':form})
				


	
