

class UserNameExistsException(Exception):
	""" This exception is raised when user tries to pick 
	the username that already exists.
	"""
	def __init__(self, message):
		super(UserNameExistsException, self).__init__(message)
		self.message = message

	def __str__(self):
		return repr(self.message)


class UserNameEmptyException(Exception):
	""" This exception is raised when user enters empty string for
	user name.
	"""
	def __init__(self, message):
		super(UserNameEmptyException, self).__init__(message)
		self.message = message

	def __str__(self):
		return repr(self.message)



class InvalidFormatException(Exception):
	""" This exception is raised when user send invalid data 
	in post request.
	"""
	def __init__(self, message):
		super(InvalidFormatException, self).__init__(message)
		self.message = message
	
	def __str__(self):
		return repr(self.message)


class NotPostRequestException(Exception):
	""" This exception is raised when user send invalid data 
	in post request.
	"""
	def __init__(self, message):
		super(NotPostRequestException, self).__init__(message)
		self.message = message
	
	def __str__(self):
		return repr(self.message)

class PostDataMissingException(Exception):
	""" This exception is raised when user do not provided required 
	data during post request.
	"""
	def __init__(self, message):
		super(PostDataMissingException, self).__init__(message)
		self.message = message
	
	def __str__(self):
		return repr(self.message)

