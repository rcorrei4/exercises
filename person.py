class person():
	def __init__(self, name, years_old, weight, height):
		self.name = name
		self.years_old = int(years_old)
		self.weight = float(weight)
		self.height = float(height)

	def get_older(self, years):
		for year in range(years):
			if self.years_old < 21:
				self.height += 0.5

			year = 1
			self.years_old += year
				

	def get_fat(self, kg):
		self.weight += kg

	def get_skinny(self, kg):
		self.weight -= kg

	def get_tall(self, cm):
		self.height += cm

	def describe_person(self):
		print("Name: {} \nAge: {} years".format(self.name, self.years_old),
			  "\nWeight: {}kg \nHeight: {}cm".format(self.weight, self.height))

ricardo = person("Ricardo", 16, 55, 182)
ricardo.describe_person()
ricardo.get_older(1)
ricardo.describe_person()