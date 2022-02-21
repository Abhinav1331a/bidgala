# Standard library imports
from django.urls import path, include

# Related third party imports

# Local application/library specific imports
from . import views


urlpatterns = [
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),
	path('register-user', views.create_user, name='register_user'),
	path('loginuser', views.login_user, name='login_user'),
	path('logout', views.logout, name='logout'),
	path('settings', views.user_settings, name='profile'),
	path('new-verification-link', views.verification_link_generator, name='verification_link_generator'),
	path('profile-update', views.account_update, name='profile_update'),
	path('profile-pic', views.profile_img_update, name='profile_pic'),
	path('track/location', views.track_location, name='track_location'),
 
	path('get-sub-category', views.get_sub_categories, name='get_sub_category'),
	path('set-account-type', views.set_account_type, name='set_account_type'),
	path('invite', views.referral_page, name='invite'),
	
	path('signup/<str:referral>/<str:name>', views.register_referral, name="register_referral"),
	path('signup/<str:referral>', views.register_referral),
	path('referralcheck', views.add_referral, name='referralcheck'),
	path('confirmation/<str:key>', views.account_verification, name="confirmation"),

	path('follow-user', views.follow_user, name="follow_user"),
	path('unfollow-user', views.unfollow_user, name="unfollow_user"),

	path('edit/header', views.edit_header_image, name="edit_header_image"),
	path('add/artist-statement', views.add_artist_statement, name="add_artist_statement"),
	path('add/featured-work', views.add_featured_work, name="add_featured_work"),
	path('add/education', views.add_education, name="add_education"),
	path('add/skills', views.add_skills, name="add_skills"),
	path('add/interests', views.add_interests, name="add_interests"),
	path('add/accomplishment', views.add_accomplishment, name="add_accomplishment"),
	path('add/exhibition', views.add_exhibition, name="add_exhibition"),
	path('edit/artist-statement', views.edit_artist_statement, name="edit_artist_statement"),
	path('delete/artist-statement', views.delete_artist_statement, name="delete_artist_statement"),
	path('edit/education/<int:educationid>', views.edit_education, name="edit_education"),
	path('delete/education/<int:educationid>', views.delete_education, name="delete_education"),
	path('edit/accomplishment/<int:accid>', views.edit_accomplishment, name="edit_accomplishment"),
	path('delete/accomplishment/<int:accid>', views.delete_accomplishment, name="delete_accomplishment"),
	path('edit/exhibition/<int:exid>', views.edit_exhibition, name="edit_exhibition"),
	path('delete/exhibition/<int:exid>', views.delete_exhibition, name="delete_exhibition"),
	path('delete/skills', views.delete_skills, name="delete_skills"),
	path('edit/skills', views.edit_skills, name="edit_skills"),
	path('delete/interests', views.delete_interests, name="delete_interests"),
	path('edit/interests', views.edit_interests, name="edit_interests"),
	path('delete/featured-work/<int:artid>', views.delete_featured_work, name="delete_featured_work"),
	path('edit/exhibition/<int:id>', views.edit_exhibition, name="edit_exhibition"),

	path('donate-credits', views.donate_credits, name="donate_credits"),

	path('p/<str:slug>', views.public_profile, name="public_profile"),
]