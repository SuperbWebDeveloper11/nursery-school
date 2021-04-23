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
from ..models import Baby
from ..forms import BabyForm


################## views for baby crud operations ################## 

class BabyList(ListView): # retrieve all babys
    model = Baby
    template_name = 'managers/baby/baby_list.html'
    context_object_name = 'baby_list'
    paginate_by = 5


class BabyDetail(DetailView): # retrieve baby detail
    model = Baby
    template_name = 'managers/baby/baby_detail.html'
    context_object_name = 'baby'


class BabyCreate(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView): # create new baby 
    model = Baby
    template_name = 'managers/baby/baby_form_create.html' 
    form_class = BabyForm
    success_message = "baby was created successfully"
    permission_required = 'managers.add_baby'

    def form_valid(self, form):
        form.instance.created_by = self.request.user # add baby created_by manually
        return super().form_valid(form)


class BabyUpdate(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView): # update baby 
    model = Baby
    template_name = 'managers/baby/baby_form_update.html' 
    form_class = BabyForm
    success_message = "baby was updated successfully"
    permission_required = 'managers.change_baby'

    def form_valid(self, form):
        if form.instance.created_by == self.request.user: # user should be the one who create the baby 
            return super().form_valid(form)
        else:
            return HttpResponse("You couldn't perform this opertaion ")

class BabyDelete(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView): # delete baby 
    model = Baby
    template_name = 'managers/baby/baby_confirm_delete.html' 
    success_message = "baby was deleted successfully"
    success_url = reverse_lazy('managers:baby_list')
    permission_required = 'managers.delete_baby'

    def form_valid(self, form):
        if form.instance.publisher == self.request.user: # user should be the one who create the baby 
            return super().form_valid(form)
        else:
            return HttpResponse("You couldn't perform this opertaion ")


