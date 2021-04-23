from django.urls import include, path
from .views import babysitter, group, baby, activity, sitting


app_name = 'managers'


urlpatterns = [

    #------------------------ urls for 'babysitter' curd operations ------------------------
    path('babysitter/', babysitter.BabysitterList.as_view(), name='babysitter_list'),
    path('babysitter/add/', babysitter.BabysitterCreate.as_view(), name='babysitter_add'),
    path('babysitter/<int:pk>/detail/', babysitter.BabysitterDetail.as_view(), name='babysitter_detail'),
    path('babysitter/<int:pk>/update/', babysitter.BabysitterUpdate.as_view(), name='babysitter_update'),
    path('babysitter/<int:pk>/delete/', babysitter.BabysitterDelete.as_view(), name='babysitter_delete'),

    #------------------------ urls for 'group' curd operations ------------------------
    path('group/', group.GroupList.as_view(), name='group_list'),
    path('group/add/', group.GroupCreate.as_view(), name='group_add'),
    path('group/<int:pk>/detail/', group.GroupDetail.as_view(), name='group_detail'),
    path('group/<int:pk>/update/', group.GroupUpdate.as_view(), name='group_update'),
    path('group/<int:pk>/delete/', group.GroupDelete.as_view(), name='group_delete'),

    #------------------------ urls for 'baby' curd operations ------------------------
    path('baby/', baby.BabyList.as_view(), name='baby_list'),
    path('baby/add/', baby.BabyCreate.as_view(), name='baby_add'),
    path('baby/<int:pk>/detail/', baby.BabyDetail.as_view(), name='baby_detail'),
    path('baby/<int:pk>/update/', baby.BabyUpdate.as_view(), name='baby_update'),
    path('baby/<int:pk>/delete/', baby.BabyDelete.as_view(), name='baby_delete'),

    #------------------------ urls for 'activity' curd operations ------------------------
    path('activity/', activity.ActivityList.as_view(), name='activity_list'),
    path('activity/add/', activity.ActivityCreate.as_view(), name='activity_add'),
    path('activity/<int:pk>/detail/', activity.ActivityDetail.as_view(), name='activity_detail'),
    path('activity/<int:pk>/update/', activity.ActivityUpdate.as_view(), name='activity_update'),
    path('activity/<int:pk>/delete/', activity.ActivityDelete.as_view(), name='activity_delete'),

    #------------------------ urls for 'sitting' curd operations ------------------------
    path('sitting/', sitting.SittingList.as_view(), name='sitting_list'),
    path('sitting/add/', sitting.SittingCreate.as_view(), name='sitting_add'),
    path('sitting/<int:pk>/detail/', sitting.SittingDetail.as_view(), name='sitting_detail'),
    path('sitting/<int:pk>/update/', sitting.SittingUpdate.as_view(), name='sitting_update'),
    path('sitting/<int:pk>/delete/', sitting.SittingDelete.as_view(), name='sitting_delete'),


]


