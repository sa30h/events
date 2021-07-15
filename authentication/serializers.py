from rest_framework import serializers
from .models import SubUser,Task,TaskUpdates,Comment


class SubUserSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	SubUser
		fields 	=	"__all__"


class TaskSerializer(serializers.ModelSerializer):
	updates  	=		serializers.HyperlinkedIdentityField(view_name="tasks:task-updates",lookup_field="id")
	comments  	=		serializers.HyperlinkedIdentityField(view_name="tasks:task-comments",lookup_field="id")
	class Meta:
		model 	=	Task
		fields 	=	"__all__"


class TaskUpdatesSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	TaskUpdates
		fields 	=	"__all__"


class CommentSerializer(serializers.ModelSerializer):
	user 	=		SubUserSerializer()
	class Meta:
		model 	=	Comment
		fields 	=	"__all__"