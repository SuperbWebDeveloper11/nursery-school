from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone 


# a user with username='default' is mandatory to use it when deleting instances
def default_user():
    return User.objects.get(username='default').pk


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now =True)

    class Meta:
        ordering = ['-created']
        abstract = True


class Babysitter(TimeStampedModel):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_bearth = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to='babysitter_pictures')
    created_by = models.ForeignKey('auth.User', related_name='created_babysitters', on_delete=models.SET_DEFAULT, default=default_user)

    def __str__(self):
        return self.name + ' ' + self.surname

    def get_absolute_url(self):
        return reverse('managers:babysitter_detail', kwargs={'pk': self.pk})
                     

class Group(TimeStampedModel):
    name = models.CharField(max_length=100)
    taken_by = models.ForeignKey(Babysitter, related_name='groups_taken', on_delete=models.SET_NULL, blank=True, null=True)
    created_by = models.ForeignKey('auth.User', related_name='created_groups', on_delete=models.SET_DEFAULT, default=default_user)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('managers:group_detail', kwargs={'pk': self.pk})


class Baby(TimeStampedModel):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_bearth = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to='baby_pictures')
    belong_to = models.ForeignKey(Group, related_name='babies', on_delete=models.SET_NULL, blank=True, null=True)
    created_by = models.ForeignKey('auth.User', related_name='created_baby', on_delete=models.SET_DEFAULT, default=default_user)

    def __str__(self):
        return self.name + ' ' + self.surname

    def get_absolute_url(self):
        return reverse('managers:baby_detail', kwargs={'pk': self.pk})
                     

class Activity(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='activity_pictures', blank=True, null=True)
    created_by = models.ForeignKey('auth.User', related_name='created_activities', on_delete=models.SET_DEFAULT, default=default_user)

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('managers:activity_detail', kwargs={'pk': self.pk})
                     

class Sitting(TimeStampedModel):
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
    activities = models.ManyToManyField(Activity, related_name='done_in_sittings')
    done_by = models.ForeignKey(Group, related_name='sittings_done', on_delete=models.SET_NULL, blank=True, null=True)
    created_by = models.ForeignKey('auth.User', related_name='created_sittings', on_delete=models.SET_DEFAULT, default=default_user)

    def get_absolute_url(self):
        return reverse('managers:sitting_detail', kwargs={'pk': self.pk})
                     


