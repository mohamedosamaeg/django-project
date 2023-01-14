from django.urls import path
from . import views
from . import index

urlpatterns = [
    path('', views.BoardListView.as_view(), name='home'),
    path('boards/<int:board_id>/', views.board_topics, name='board_topics'),
    path('boards/<int:board_id>/new/', views.new_topic, name='new_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>', views.topic_posts, name='topic_posts'),
    path('boards/<int:board_id>/topics/<int:topic_id>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/edit/', views.PostUpdateView.as_view(),
         name='edit_post'),
    path('home.html', index.webhome, name='home.html'),
    path('demand.html', index.webdemand, name='demand.html'),
    path('skills.html', index.webskills, name='skills.html'),
    path('geography.html', index.webgeo,name='geography.html'),
    path('latest_jobs.html', index.weblatest_jobs, name='latest_jobs.html'),
]
