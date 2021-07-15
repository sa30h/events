from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()

class SubUser(models.Model):
	user 		=		models.ForeignKey(User,on_delete=models.CASCADE)
	name 		=		models.CharField(max_length=120,unique=True)
	password    =		models.CharField(max_length=120)


	def __str__(self):
		return self.name



class Task(models.Model):
	user 		=		models.ForeignKey(SubUser,on_delete=models.CASCADE)
	task		=		models.TextField(max_length=1000)

	def __str__(self):
		return F"{self.user}"

class EventTask(models.Model):
	user 		=		models.ForeignKey(User,on_delete=models.CASCADE)
	task		=		models.TextField(max_length=1000)
	def __str__(self):
		return self.task
       
  
class TaskUpdates(models.Model):
	task 		=		models.ForeignKey(EventTask,on_delete=models.CASCADE)
	update 		=		models.TextField(max_length=1000)

	def __str__(self):
		return F"{self.task}"


class Comment(models.Model):
	user 		=		models.ForeignKey(SubUser,on_delete=models.CASCADE)
	task 		=		models.ForeignKey(Task,on_delete=models.CASCADE)
	comment		=		models.TextField(max_length=1000)

	def __str__(self):
		return F"{self.task}"

class TaskComment(models.Model):
	user 		=		models.ForeignKey(User,on_delete=models.CASCADE)
	task 		=		models.ForeignKey(EventTask,on_delete=models.CASCADE)
	comment		=		models.TextField(max_length=1000)
	def __str__(self):
		return self.task.task
