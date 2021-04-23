from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.template.loader import render_to_string
from django.core.mail import send_mail
# messages framework
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# class-based generic views
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# import models
from django.contrib.auth.models import User
from ..models import Babysitter
from ..forms import BabysitterForm


################## views for babysitter crud operations ################## 

class BabysitterList(ListView): # retrieve all babysitters
    model = Babysitter
    template_name = 'managers/babysitter/babysitter_list.html'
    context_object_name = 'babysitter_list'
    paginate_by = 5


class BabysitterDetail(DetailView): # retrieve babysitter detail
    model = Babysitter
    template_name = 'managers/babysitter/babysitter_detail.html'
    context_object_name = 'babysitter'


class BabysitterCreate(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView): # create new babysitter 
    model = Babysitter
    template_name = 'managers/babysitter/babysitter_form_create.html' 
    form_class = BabysitterForm
    success_message = "babysitter was created successfully"
    permission_required = 'managers.add_babysitter'

    def form_valid(self, form):
        form.instance.created_by = self.request.user # add babysitter created_by manually
        return super().form_valid(form)


class BabysitterUpdate(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView): # update babysitter 
    model = Babysitter
    template_name = 'managers/babysitter/babysitter_form_update.html' 
    form_class = BabysitterForm
    success_message = "babysitter was updated successfully"
    permission_required = 'managers.change_babysitter'

    def form_valid(self, form):
        if form.instance.created_by == self.request.user: # user should be the one who create the babysitter 
            return super().form_valid(form)
        else:
            return HttpResponse("You couldn't perform this opertaion ")

class BabysitterDelete(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView): # delete babysitter 
    model = Babysitter
    template_name = 'managers/babysitter/babysitter_confirm_delete.html' 
    success_message = "babysitter was deleted successfully"
    success_url = reverse_lazy('managers:babysitter_list')
    permission_required = 'managers.delete_babysitter'

    def form_valid(self, form):
        if form.instance.publisher == self.request.user: # user should be the one who create the babysitter 
            return super().form_valid(form)
        else:
            return HttpResponse("You couldn't perform this opertaion ")


