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
from ..models import Activity
from ..forms import ActivityForm


################## views for activity crud operations ################## 

class ActivityList(ListView): # retrieve all activitys
    model = Activity
    template_name = 'managers/activity/activity_list.html'
    context_object_name = 'activity_list'
    paginate_by = 5


class ActivityDetail(DetailView): # retrieve activity detail
    model = Activity
    template_name = 'managers/activity/activity_detail.html'
    context_object_name = 'activity'


class ActivityCreate(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView): # create new activity 
    model = Activity
    template_name = 'managers/activity/activity_form_create.html' 
    form_class = ActivityForm
    success_message = "activity was created successfully"
    permission_required = 'managers.add_activity'

    def form_valid(self, form):
        form.instance.created_by = self.request.user # add activity created_by manually
        return super().form_valid(form)


class ActivityUpdate(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView): # update activity 
    model = Activity
    template_name = 'managers/activity/activity_form_update.html' 
    form_class = ActivityForm
    success_message = "activity was updated successfully"
    permission_required = 'managers.change_activity'

    def form_valid(self, form):
        if form.instance.created_by == self.request.user: # user should be the one who create the activity 
            return super().form_valid(form)
        else:
            return HttpResponse("You couldn't perform this opertaion ")

class ActivityDelete(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView): # delete activity 
    model = Activity
    template_name = 'managers/activity/activity_confirm_delete.html' 
    success_message = "activity was deleted successfully"
    success_url = reverse_lazy('managers:activity_list')
    permission_required = 'managers.delete_activity'

    def form_valid(self, form):
        if form.instance.publisher == self.request.user: # user should be the one who create the activity 
            return super().form_valid(form)
        else:
            return HttpResponse("You couldn't perform this opertaion ")


