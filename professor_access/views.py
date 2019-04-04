from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


from professor_access.models import Project
from professor_access.models import Post

class professorForm(ModelForm):
    class Meta:
        model = Project
#        fields = ['ID', 'name', 'notes', 'stage']
        fields = ['name', 'details', 'advisor', 'email', 'stage']

def professor_list(request, template_name='professor_access/pa_list.html'):
    project = Project.objects.all()
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)



def professor_create(request, template_name='professor_access/project_form.html'):
    form = professorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('professor_access:pa_list')
    return render(request, template_name, {'form':form})


def professor_update(request, pk, template_name='professor_access/project_form.html'):
    project= get_object_or_404(Project, pk=pk)
    form = professorForm(request.POST or None, instance= project)
    if form.is_valid():
        form.save()
        return redirect('professor_access:pa_list')
    return render(request, template_name, {'form':form})

def professor_update1(request, pk, template_name='professor_access/project_form_copy.html'):
#def professor_update1(request, pk, template_name='professor_access/detail.html'):
    project= get_object_or_404(Project, pk=pk)
    content = professorForm(request.POST or None, instance= project)
    if content.is_valid():
       content.save()
       return redirect('professor_access:pa_list')
    return render(request, template_name, {'form':content})



    #get = professorForm (get.POST or None, instance=project)
    #if get.is_valid ():
    #   get.save()
    #   return redirect('professor_access:pa_list')
    #return render (get, template_name, {'get': get})
def professor_delete(request, pk, template_name='professor_access/project_confirm_delete.html'):
    project= get_object_or_404(Project, pk=pk)
    if request.method=='POST':
        project.delete()
        return redirect('professor_access:pa_list')
    return render(request, template_name, {'object':project})


#def post_list(request, template_name='professor_access/project_form_copy.html'):
#    posts = Post. published.all()
#    return render(request,
#                  'professor_access/project_form_copy.html',
#                  {'post': 'posts'})

def post_detail(request, year, month, day, post):
#def professor_update1(request, year, month, day, post):
    posts = Post.published.all ()
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'professor_access/project_form_copy.html',
                  {'post': post})