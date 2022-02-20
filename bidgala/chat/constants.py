from django.conf import settings

def get_purchase_message(user_info, product_info):
	name = user_info.user.first_name if user_info.user.first_name else ''
	artist_name = product_info.owner.user.first_name if product_info.owner.user.first_name else ''
	return 'Hi ' + name  + '! Thank you for purchasing ' + product_info.art_title + '. Your card will not be charged until the artist ships your order and submits a tracking number. If the artist does not accept within 7 days, your order will be cancelled automatically. Feel free to ask ' + artist_name + ' any questions in this chat.'

def get_buyer_message(artName, artID):
	return 'Hi, I would like to buy the following piece from you. \n' + 'Art Name: ' +  artName + '.' + '\nKindly confirm the order and you will automatically receive your funds once you submit a tracking number for the shipment.'


def get_decline_message(user_info, product_info):
	name = user_info.user.first_name if user_info.user.first_name else ''
	artist_name = product_info.owner.user.first_name if product_info.owner.user.first_name else ''
	show_by = ' by ' if artist_name else ''
	return 'Hi ' + name  + '! Your request to purchase ' + product_info.art_title + ' has been declined' + show_by + artist_name + '. Feel free to send ' + artist_name + 'a message here.'

def get_accept_message(user_info, product_info):
	name = user_info.user.first_name if user_info.user.first_name else ''
	artist_name = product_info.owner.user.first_name if product_info.owner.user.first_name else 'The artist'
	return 'Congratulations' + name + '! Your request to purchase ' + product_info.art_title + ' has been accepted. ' + artist_name + ' should provide you with a tracking number within 7 days. Your card will not be charged until your order is shipped. Feel free to send ' + artist_name.lower() + ' any questions in this chat.'
	