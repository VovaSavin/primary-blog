from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Blog,
    Bloger,
    Comments,
)
from .forms import (
    EditProfile,
    EditBlogerProfile,
    CommentsForm, 
    ImageLoadForm,
    )
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    FormMixin,
)
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


# Create your views here.


def main_page(request):
    '''Главная страница'''
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'blogdiy/first.html', context)


class BlogsList(ListView):
    '''Список всех блогов'''
    model = Blog
    template_name = 'blogdiy/blog-list.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        context['title'] = 'Список блогов'
        return context


class BlogsDetail(DetailView, FormMixin):
    '''Отображение конкретного блога'''
    model = Blog
    template_name = 'blogdiy/blog-detail.html'
    context_object_name = 'oneblog'
    form_class = CommentsForm

    def get_success_url(self, **kwargs):
        '''Перадресация на текущуую страницу после публикации коммента'''
        return reverse_lazy('blogs-detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        '''Проверка валидности формы'''
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        '''Подстановка автора коммента и блога, к которому он принадлежит'''
        self.object = form.save(commit=False)
        self.object.to_blog = self.get_object()
        self.object.author_comments = self.request.user
        self.object.save()
        return super().form_valid(form)
 

    def get_context_data(self, **kwargs):
        context = super(BlogsDetail, self).get_context_data(**kwargs)
        context['title'] = Blog.objects.get(pk=self.kwargs['pk'])
        return context


@login_required
def delete_comment(request, pk, type, *args):
    comment = Comments.objects.get(pk=pk)
    blog = Blog.objects.get(title=comment.to_blog).id
    if type == 'delete':
        if Comments.objects.filter(author_comments=request.user) or Blog.objects.filter(author_blog=request.user):
            comment.delete()
            return redirect(reverse_lazy('blogs-detail', args=[str(blog)]))
        else:
            return redirect(reverse_lazy('blogs-detail', args=[str(blog)]))
    context = {
        'comment': comment,
    }
    return render(request, 'blogdiy/comment-delete.html', context)


class BlogerList(ListView):
    '''Список всех блоггеров'''
    model = Bloger
    template_name = 'blogdiy/blogger-list.html'
    context_object_name = 'bloggers'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(BlogerList, self).get_context_data(**kwargs)
        context['title'] = 'Список блоггеров'
        return context


class BlogerDetail(DetailView):
    '''Отображение конкретного блоггера'''
    model = Bloger
    template_name = 'blogdiy/blogger-detail.html'
    context_object_name = 'oneblogger'

    def get_context_data(self, **kwargs):
        context = super(BlogerDetail, self).get_context_data(**kwargs)
        context['title'] = Bloger.objects.get(pk=self.kwargs['pk'])
        return context


class CreateBlog(LoginRequiredMixin, CreateView):
    '''Создание блога на стороне клиента'''
    model = Blog
    fields = ['title', 'text_blog', 'date']
    initial = {
        'date': timezone.now,
    }
    template_name = 'blogdiy/create-blog.html'

    def form_valid(self, form):
        form.instance.author_blog = self.request.user
        return super().form_valid(form)


class DeleteBlog(UserPassesTestMixin, DeleteView):
    '''Удаление блога на стороне клиента'''
    model = Blog
    success_url = reverse_lazy('blogs-all')
    template_name = 'blogdiy/delete-blog.html'
    context_object_name = 'b'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author_blog:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(DeleteBlog, self).get_context_data(**kwargs)
        context['title'] = Blog.objects.get(pk=self.kwargs['pk'])
        return context


@login_required
def my_pofile(request):
    '''Профиль пользователя/блоггера'''
    context = {
        'title': 'Кабинет пользователя',
    }
    return render(request, 'blogdiy/profile.html', context)


@login_required
def edit_profile_info(request):
    '''Редактирование информации о блоггере'''
    if request.method == 'POST':
        forms = EditProfile(request.POST, instance=request.user)
        try:
            forms2 = EditBlogerProfile(
                request.POST, instance=request.user.bloger)
            forms_foto = ImageLoadForm(request.POST, request.FILES, instance=request.user.bloger)
        except:
            forms2 = EditBlogerProfile(request.POST)
            forms_foto = ImageLoadForm(request.POST, request.FILES)
        if forms.is_valid() and forms2.is_valid() and forms_foto.is_valid():
            forms2.instance.user = request.user
            forms.save()
            forms2.save()
            forms_foto.save()
            username = forms.cleaned_data.get('username')
            name = forms.cleaned_data.get('name')
            surname = forms.cleaned_data.get('surname')
            age = forms.cleaned_data.get('age')
            about = forms.cleaned_data.get('about')
            return redirect(reverse_lazy('profile'))
    else:
        forms = EditProfile(instance=request.user)
        try:
            forms2 = EditBlogerProfile(instance=request.user.bloger)
            forms_foto = ImageLoadForm(instance=request.user.bloger)
        except:
            forms2 = EditBlogerProfile()
            forms_foto = ImageLoadForm()
    context = {
        'title': f'Редактирование {request.user}',
        'form': forms,
        'form2': forms2,
        'forms_foto': forms_foto,
    }
    return render(request, 'blogdiy/create-blogger.html', context)


class UpdateProfile(UpdateView):
    pass

