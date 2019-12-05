from abc import ABC,abstractmethod

class Db(ABC):
	@abstractmethod
	def connect(self):
		return 0
	@abstractmethod
	def disconnect(self):
		return 0
class Oracle(Db):
	def connect(self):
		print("oracle is connected")
	def disconnect(self):
		print("oracle disconnected")
class Mysql(Db):
	def connect(self):
		print("mysql is connected")
	def disconnect(self):
		print("mysql disconnected")
		
dbname=input("Oracle/Mysql")
classname=globals()[dbname]
x=classname()
x.connect()
x.disconnect()
		