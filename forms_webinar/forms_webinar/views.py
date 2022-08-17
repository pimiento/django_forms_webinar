from django.views import generic
from django.urls import reverse_lazy
from django.utils import translation
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import (CreateView, DeleteView, UpdateView)
from .models import NameModel
from .forms import MessageForm, NameForm, CreateNameForm


def message(request):
    form = MessageForm(request.POST or None)
    return render(
        request,
        "forms_webinar/message.html",
        context={
            'form': form
        }
    )

def name(request):
    form = NameForm(request.POST or None)
    if request.method == "POST":
        form.save()
    return render(
        request,
        "forms_webinar/my_form.html",
        {"form": form}
    )


# если интересно что же лучше использовать обычные вьюхи или generic-views
# https://spookylukey.github.io/django-views-the-right-way/index.html
class NameCreateView(CreateView):
    """Create a Name"""
    model = NameModel
    form_class = CreateNameForm


class NameUpdateView(UpdateView):
    """Update a Name"""
    model = NameModel
    fields = ['name']


class NameDeleteView(DeleteView):
    """Delete a Name"""
    model = NameModel
    success_url = reverse_lazy('list_names')


class NamesListView(generic.ListView):
    model = NameModel
    context_object_name = 'names'
    template_name = "forms_webinar/list.html"


def name_detail(request, pk):
    name = get_object_or_404(NameModel, pk=pk)
    # Translators: here is comment
    name_title = _('Here is name %(name)s. Key is %(key)d.') % {'name': name.name, 'key': name.pk}
    context = {
        'name': name,
        'title': name_title
    }
    return render(request, 'forms_webinar/name.html', context=context)


def my_form(request):
    form = NameForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("name")  # -> HTTP 301/2
    return render(
        request,
        'forms_webinar/my_form.html',
        {
            'form': form
        }
    ) # -> HTTP 200
