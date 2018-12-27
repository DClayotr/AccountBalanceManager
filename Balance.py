# # Kivy Dependecies
import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# # End Kivy Dependencies
class fileHandler():

	def __init__(self):
		return None

	def __read(self):
		#Read in Balance information
		with open("Balance.txt") as f:
			content = f.readlines()
		#create variables for information
		if content:
			content = [x.strip() for x in content]
			return content
		else:
			content = [0,0]
			return content

	def getCheckings(self):
		content = self.__read()
		return int(content[0])

	def getSavings(self):
		content = self.__read()
		return int(content[1])

	def write(self,Checkings, Savings):
		with open("Balance.txt", 'w') as f:
			f.seek(0)
			f.truncate()
			f.write(str(Checkings) + "\n" + str(Savings))
			return 0

class BalanceOperator(object):

	
	def __init__(self, Checkings, Savings):
		self.Checkings = Checkings
		self.Savings = Savings
		self.Handle = fileHandler()
	
	def update(self):
		self.Checkings = self.Handle.getCheckings() 
		self.Savings = self.Handle.getSavings()
		return None

	def Despoite(self,Account, Amount):
		self.update()
		if(Account == 0):
			self.Checkings = self.Checkings + int(Amount)
			self.Handle.write(self.Checkings, self.Savings)
			return None
		elif(Account == 1):
			self.Savings = self.Savings + int(Amount)
			self.Handle.write(self.Checkings, self.Savings)
			return None

	def Withdraw(self, Amount):
		self.update();
		self.Checkings = self.Checkings - int(Amount)
		self.Handle.write(self.Checkings, self.Savings)
		return None

	def TransferIn(self, Amount):
		self.update()
		self.Savings = self.Savings - int(Amount)
		self.Checkings = self.Checkings + int(Amount)
		self.Handle.write(self.Checkings, self.Savings)
		return None

	def TransferOut(self, Amount):
		self.update()
		self.Savings = self.Savings + int(Amount)
		self.Checkings = self.Checkings - int(Amount)
		self.Handle.write(self.Checkings, self.Savings)
		return None

class BalanceGridLayout(BoxLayout):

		def withdraw(self, Amount):
			BP = BalanceOperator(0,0)
			BP.Withdraw(Amount)
			return None
		def Deposite(self, Account, Amount):
			BP = BalanceOperator(0,0)
			BP.Despoite(Account, Amount)
			return None
		def TransferIn(self, Amount):
			BP = BalanceOperator(0,0)
			BP.TransferIn(Amount)
			pass
		def TransferOut(self, Amount):
			BP = BalanceOperator(0,0)
			BP.TransferOut(Amount)
			return None

class BalanceApp(App):
	kv_directory = 'template'

	def build(self):
		Window.size = (750,225)
		return BalanceGridLayout()


if __name__ == '__main__':
	BalanceApp = BalanceApp()
	BalanceApp.run()

