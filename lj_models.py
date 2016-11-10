class User(object):
	"""docstring for User"""
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
	def get_details(self):
		return "Name: {} Email: {}".format(self.name, self.email)

		