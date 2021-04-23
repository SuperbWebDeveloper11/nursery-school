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
from ..models import Group
from ..forms import GroupForm


################## views for group crud operations ################## 

class GroupList(ListView): # retrieve all groups
    model = Group
    template_name = 'managers/group/group_list.html'
    context_object_name = 'group_list'
    paginate_by = 5


class GroupDetail(DetailView): # retrieve group detail
    model = Group
    template_name = 'managers/group/group_detail.html'
    context_object_name = 'group'


class GroupCreate(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView): # create new group 
    model = Group
    template_name = 'managers/group/group_form_create.html' 
    form_class = GroupForm
    success_message = "group was created successfully"
    permission_required = 'managers.add_group'

    def form_valid(self, form):
        form.instance.created_by = self.request.user # add group created_by manually
        return super().form_valid(form)


class GroupUpdate(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView): # update group 
    model = Group
    template_name = 'managers/group/group_form_update.html' 
    form_class = GroupForm
    success_message = "group was updated successfully"
    permission_required = 'managers.change_group'

    def form_valid(self, form):
        if form.instance.created_by == self.request.user: # user should be the one who create the group 
            return super().form_valid(form)
        else:
            return HttpResponse("You couldn't perform this opertaion ")

class GroupDelete(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView): # delete group 
    model = Group
    template_name = 'managers/group/group_confirm_delete.html' 
    success_message = "group was deleted successfully"
    success_url = reverse_lazy('managers:group_list')
    permission_required = 'managers.delete_group'

    def form_valid(self, form):
        if form.instance.publisher == self.request.user: # user should be the one who create the group 
            return super().form_valid(form)
        else:
            return HttpResponse("You couldn't perform this opertaion ")


