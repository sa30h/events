from django.shortcuts import render,redirect
from .models import *
from .serializers import SubUserSerializer,TaskSerializer,TaskUpdatesSerializer,CommentSerializer
from rest_framework import generics,response
from .form import *
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout



# Create your views here.

class LoginAPIView(generics.GenericAPIView):
	serializer_class 		=		SubUserSerializer
	queryset 				=		SubUser.objects.all()

	def get(self,request):
		name 		 	=		self.request.GET.get('name')
		password 		=		self.request.GET.get('password')
		subuser 		=		SubUser.objects.filter(name=name)
		if subuser.count()!=0:
			subuser 		=		SubUser.objects.get(name=name)
			if subuser.password==password:
				serialize 	=	SubUserSerializer(subuser)
				return response.Response(serialize.data)
			return response.Response({"message":"invalid password"})
		return response.Response({"message":"Invalid Credentails"})


class TasksListAPIViews(generics.ListAPIView):
	serializer_class 		=		TaskSerializer
	queryset 				=		Task.objects.all()


class MyTasksListAPIView(generics.GenericAPIView):
	serializer_class 		=		TaskSerializer
	queryset 				=		Task.objects.all()

	def get(self,request,id=None):
		subuser 		=		SubUser.objects.get(id=id)
		tasks  			=		Task.objects.filter(user=subuser)
		serialize      =		TaskSerializer(tasks,many=True)
		return response.Response(serialize.data)



class UpdatesCreateAPIView(generics.CreateAPIView):
	serializer_class 	=	TaskUpdatesSerializer
	queryset 			=	TaskUpdates.objects.all()



class TaskUpdatesListAPIView(generics.GenericAPIView):
	serializer_class 	=	TaskUpdatesSerializer
	queryset 			=	TaskUpdates.objects.all()

	def get(self,request,id=None):
		task 			=	Task.objects.get(id=id)
		query  			=	TaskUpdates.objects.filter(task=task)
		serialize 		=	TaskUpdatesSerializer(query,many=True)
		return  response.Response(serialize.data)


class CommentCreateAPIView(generics.CreateAPIView):
	serializer_class 		 =		CommentSerializer
	queryset 				 =		Comment.objects.all()



class TaskCommentListAPIView(generics.GenericAPIView):
	serializer_class 		=		CommentSerializer
	queryset 				=		Comment.objects.all()


	def get(self,request,id=None):
		task 				=		Task.objects.get(id=id)
		query 				=		Comment.objects.filter(task=task)
		serialize 			=		CommentSerializer(query,many=True)
		return response.Response(serialize.data)

# def home(request):
# 	context={}
# 	data=[]
# 	taskA=[]
# 	updateA=[]
# 	updatexx=[]
# 	member=SubUser.objects.all()
# 	task=Task.objects.all()
# 	taskupdates=TaskUpdates.objects.all()
# 	for xx in task:
# 		# taskx=Task.objects.filter(Q(user__user=xx.name))
# 		updatex=TaskUpdates.objects.filter(Q(task__task=xx.task))
# 		taskA.append({'task':xx,'update':updatex.update})
# 	print('updxx',updatexx)
# 	# context['updates']=
# 	context['member']=member
# 	context['taskA']=taskA
# 	context['taskupdates']=taskupdates
# 	for x in task :
# 		updates=TaskUpdates.objects.filter(task__task=x.task)
# 		updateA.append({'task':x.task,'update':updates})

# 	print(updateA)

# 	# for i in member:
# 	# 	task=Task.objects.filter(user__name=i.name)
# 	# 	data.append({'member':i,'task':})
# 	# context['data']=data




# 	return render(request,'authentication/dashboard.html',context)

def home(request):
	if request.user.is_authenticated:
		context={}

		member=User.objects.all()
		task=EventTask.objects.all().order_by('user')
		update=TaskUpdates.objects.all()
		comment=TaskComment.objects.all()
		data=[]
		data2=[]

		for i in member:
			taskx=EventTask.objects.filter(user__username=i.username)
			data.append({'member':i,'task':taskx})
		for j in task:

			memberxx=j.user
			taskxx=EventTask.objects.filter(id=j.id)
			my_t = [item.task for item in taskxx]
			updatexx=TaskUpdates.objects.filter(task__id=j.id)
			my_u = [item.update for item in updatexx]
			commentxx=TaskComment.objects.filter(task__id=j.id)
			my_c = [item.comment for item in commentxx]
			my_cb=[item.user for item in commentxx]

			if len(my_t)>0:
				my_t=my_t
			else:
				my_t.append("...")

			if len(my_u)>0:
				my_u=my_u
			else:
				my_u.append("...")
			
			if len(my_c)>0:
				my_c=my_c
			else:
				my_c.append("...")


			if len(my_cb)>0:
				my_cb=my_cb
			else:
				my_cb.append("...")

		
			data2.append({'member':memberxx,'task':my_t[0],'update':my_u[0],'comment':my_c[0],'commentby':my_cb[0]})



		context['data2']=data2
		print('data',data2)
		context['member']=member
		context['task']=task
		context['update']=update
		context['comment']=comment

		return render(request,'authentication/dashboard.html',context)
	return redirect('/auth/userlogin/')

def register(request):
	context={}
	users=User.objects.all().order_by('username')
	context['users']=users
	if request.method == "POST":
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			context['msg']="Added!"
			redirect('/auth/register/')
		else:
			context['err']="Something went wrong!"
			redirect('/auth/register')


	form=RegistrationForm()
	context['form']=form
	return render(request,'authentication/register.html',context)

def userlogin(request):
    context={}

    user=request.user
    # if user.is_authenticated:
    #     return redirect("userlogin")

    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():

            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('/auth/dashboard/')

    form=UserLoginForm()
    context['form']=form
    return render(request,'authentication/login.html',context)

def userlogout(request):
    logout(request)
    return redirect('/auth/userlogin/')

def userdelete(request,id):
    pi=User.objects.get(pk=id)
    pi.delete()
    # messages.success(request,"successful")
    return redirect('/auth/register/')
   

def mytask(request):
	context={}
	task=EventTask.objects.filter(user__username=request.user)
	context['task']=task
	updates=TaskUpdates.objects.filter(task__user__username=request.user)
	context['updates']=updates
	comment=TaskComment.objects.filter(user__username=request.user)
	context['comment']=comment
	data=[]
	for j in task:

		# memberxx=j.user
		taskxx=EventTask.objects.filter(id=j.id)
		my_t = [item.task for item in taskxx]
		updatexx=TaskUpdates.objects.filter(task__id=j.id)
		my_u = [item.update for item in updatexx]
		commentxx=TaskComment.objects.filter(task__id=j.id)
		my_c = [item.comment for item in commentxx]
		my_cb=[item.user for item in commentxx]

		if len(my_t)>0:
			my_t=my_t
		else:
			my_t.append("...")

		if len(my_u)>0:
			my_u=my_u
		else:
			my_u.append("...")
		
		if len(my_c)>0:
			my_c=my_c
		else:
			my_c.append("...")


		if len(my_cb)>0:
			my_cb=my_cb
		else:
			my_cb.append("...")

	
		data.append({'task':my_t[0],'update':my_u[0],'comment':my_c[0],'commentby':my_cb[0]})



	context['data']=data
	return render(request,'authentication/mytask.html',context)

def Task(request):
	context={}
	if request.method == "POST":
		form=Taskform(request.POST)
		print(request.POST)
		if form.is_valid():
			form.save()
			context['msg']="Added!"
			redirect('/auth/task/')


	context['form']=Taskform()
	return render(request,'authentication/task.html',context)

def TaskId(request,task):
	context={}
	task=EventTask.objects.filter(task=task)
	context['task']=task
	print(task)
	update=TaskUpdates.objects.filter(task__task=task[0])
	print(update)
	context['update']=update
	comment=TaskComment.objects.filter(task__task=task[0])
	context['comment']=comment
	return render(request,'authentication/taskid.html',context)

def Taskupdate(request):
	context={}
	if request.method=="POST":
		form=Taskupdatesform(request.POST)
		if form.is_valid():
			form.save()
			context['msg']="Added!"
			redirect('/auth/taskupdate/')

	context['form']=Taskupdatesform()
	return render(request,'authentication/taskupdate.html',context)

def Comment(request):
	context={}
	if request.method=="POST":
		form=Commentform(request.POST)
		if form.is_valid():
			form.save()
			context['msg']="Added!"
			redirect('/auth/comment/')

	context['form']=Commentform()
	return render(request,'authentication/comment.html',context)

