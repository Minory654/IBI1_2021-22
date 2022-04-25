class stuff (object):
	def __init__(self, first_name,last_name, location, role):
		self.first_name =first_name
		self.last_name=last_name
		self.location = location
		self.role = role
a=stuff("Bai","Yu","ZJE", "student")
print(a.first_name,a.last_name,a.location,a.role)
