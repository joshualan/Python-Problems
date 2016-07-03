class TempTracker:
	def __init__(self):
		self._max = None
		self._min = None
		self._mode = None
		self._highest_mode = 0
		self._temp_distribution = {i: 0 for i in range(111)}
		self._num_temps = 0
		self._total = 0
		self._mean = 0.0
	
	def insert(temp):
		self._total += temp
		self._num_temps = 0
		self._mean = self._total / self._num_temps
		self._temp_distribution[temp] += 1

		if self._temp_distribution[temp] > self._highest_mode:
			self._mode = [temp]
			self._highest_mode = self.temp_distribution[temp]
		elif self._temp_distribution[temp] == self._highest_mode:
			self._mode.append(temp)

		if self._max is None or self._max < temp: 
			self._max = temp

		if self._min is None or self._min > temp: 
			self._min = temp

	@property
	def max(self):
		return self._max

	@property
	def min(self):
		return self._min
	
	@property
	def mean(self):
		return self._mean
	
	@property
	def mode(self):
		if len(self._mode) == 1:
			return self._mode[0]
		else:
			return self._mode
	
