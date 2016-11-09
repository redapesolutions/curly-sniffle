class User(object):
	"""docstring for User"""
	def __init__(self, u_id, name, email, password):
		self.u_id = u_id
		self.name = name
		self.email = email
		self.password = password
	def get_details(self):
		return "Name: {} Email: {}".format(self.name, self.email)

		