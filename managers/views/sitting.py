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
from ..models import Sitting
from ..forms import SittingForm


################## views for sitting crud operations ################## 

class SittingList(ListView): # retrieve all sittings
    model = Sitting
    template_name = 'managers/sitting/sitting_list.html'
    context_object_name = 'sitting_list'
    paginate_by = 5


class SittingDetail(DetailView): # retrieve sitting detail
    model = Sitting
    template_name = 'managers/sitting/sitting_detail.html'
    context_object_name = 'sitting'


class SittingCreate(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView): # create new sitting 
    model = Sitting
    template_name = 'managers/sitting/sitting_form_create.html' 
    form_class = SittingForm
    success_message = "sitting was created successfully"
    permission_required = 'managers.add_sitting'

    def form_valid(self, form):
        form.instance.created_by = self.request.user # add sitting created_by manually
        return super().form_valid(form)


class SittingUpdate(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView): # update sitting 
    model = Sitting
    template_name = 'managers/sitting/sitting_form_update.html' 
    form_class = SittingForm
    success_message = "sitting was updated successfully"
    permission_required = 'managers.change_sitting'

    def form_valid(self, form):
        if form.instance.created_by == self.request.user: # user should be the one who create the sitting 
            return super().form_valid(form)
        else:
            return HttpResponse("You couldn't perform this opertaion ")


class SittingDelete(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView): # delete sitting 
    model = Sitting
    template_name = 'managers/sitting/sitting_confirm_delete.html' 
    success_message = "sitting was deleted successfully"
    success_url = reverse_lazy('managers:sitting_list')
    permission_required = 'managers.delete_sitting'

    def form_valid(self, form):
        if form.instance.publisher == self.request.user: # user should be the one who create the sitting 
            return super().form_valid(form)
        else:
            return HttpResponse("You couldn't perform this opertaion ")


