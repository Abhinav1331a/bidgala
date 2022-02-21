from .models import Like
from django.db.models import Q


def get_liked_post(post_id, user_obj):
	liked_obj = Like.objects.filter(Q(post_id__in=post_id)).filter(user=user_obj)
	return liked_obj