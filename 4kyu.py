class User:
	all_rank = (-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8)

	def __init__(self):
		self.__rank = self.all_rank[0]
		self.__progress = 0

	@property
	def rank(self):
		return self.__rank

	@property
	def progress(self):
		if self.__rank == 8:
			self.__progress = 0
		return self.__progress

	def inc_progress(self, task):
		if task < -8 or task == 0 or task > 8:
			raise ValueError("Invalid activity rank")
		diff = self.all_rank.index(task) - self.all_rank.index(self.__rank)
		if diff == 0:
			self.__progress += 3
		elif diff == -1:
			self.__progress += 1
		elif diff > 0:
			self.__progress += 10 * diff * diff
			print(self.__progress)

		while self.progress >= 100:
			self.__progress -= 100
			if self.rank == 8:
				break
			self.__rank += 1
			if self.rank == 0:
				self.__rank = 1


user = User()
print(user.rank)  # => -8
print(user.progress)  # => 0
print(user.inc_progress(8))
print(user.rank)  # => -8
print(user.progress)  # => 0
print(user.inc_progress(8))
print(user.rank)  # => -8
print(user.progress)  # => 0
print(user.inc_progress(8))
print(user.rank)  # => -8
print(user.progress)
print(user.inc_progress(8))
print(user.rank)  # => -8
print(user.progress)

print(user.inc_progress(1))
print(user.rank)  # => -8
print(user.progress)

print(user.inc_progress(1))
print(user.rank)  # => -8
print(user.progress)
# => 0
