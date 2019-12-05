from abc import ABC,abstractmethod

class Vehicle(ABC):
	def __int__(self,r_id,tank_cap):
		self.r_id=r_id
		self.tank_cap=tank_cap
	@abstractmethod
	def brake(self,x):
		pass
		
class Hyundai(Vehicle):
	def brake(self,x):
		print('appled brake strength is {}'.format(x))
		
class Suzuki(Vehicle):
	def brake(self,x):
		print('appled brake strength is {}'.format(x))
#v=Vehicle(2,34)
h=Hyundai()
s=Suzuki()

h.brake(45)
s.brake(34)