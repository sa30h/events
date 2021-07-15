from django.urls import path
from .views import LoginAPIView,TasksListAPIViews,MyTasksListAPIView,UpdatesCreateAPIView,TaskUpdatesListAPIView,CommentCreateAPIView,TaskCommentListAPIView
from . import views
app_name="tasks"


urlpatterns =[


	#login API for subsuser send name and password in url given below
	#http://localhost:8000/login/?name={name}&password={password}
	#if credentails are right it will return all data of that subuser
	#from data save id in local storage of that subuser
	path('login/',LoginAPIView.as_view(),name="login"),
	#this API will return all tasks with there updates and comments urls 
	path('tasks/',TasksListAPIViews.as_view(),name="tasks"),
	#pass saved id of subuser at here <id> 
	path("my-tasks/<id>/",MyTasksListAPIView.as_view(),name="my-tasks"),
	#this api is used for updation of there task given to subuser
	path("update-task/",UpdatesCreateAPIView.as_view(),name="update-task"),
	#this api will return all the updates of a task
	#<id> is a id of a task not of a subuser
	#also i had provided a hyperlinkedidentityfield it will return updates and comments urls of a particular task in tasks api
	path("task-updates/<id>/",TaskUpdatesListAPIView.as_view(),name="task-updates"),
	#this api is used to comment a task
	path("comment-task/",CommentCreateAPIView.as_view(),name="comment-create"),
	#this api will return all the comments of a task
	#<id> is a id of a task not of a subuser
	#also i had provided a hyperlinkedidentityfield it will return updates and comments urls of a particular task in tasks api
	path("task-comments/<id>/",TaskCommentListAPIView.as_view(),name="task-comments"),


	#NOTE
	#in all tasks only comments are allowed
	#any one can comment
	#show all the update and commnets in all tasks
	path("dashboard/",views.home,name="homepage"),
	path("register/",views.register,name="register"),
	path("userdelete/<int:id>",views.userdelete,name="userdelete"),
	path("userlogin/",views.userlogin,name="userlogin"),
	path("userlogout/",views.userlogout,name="logout"),
	path("mytask/",views.mytask,name="mytask"),
	path("task/",views.Task,name="task"),
	path("task/<str:task>/",views.TaskId,name="taskid"),
	path("taskupdate/",views.Taskupdate,name="taskupdate"),
	path("comment/",views.Comment,name="comment"),

]