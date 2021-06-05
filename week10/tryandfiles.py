f = open("test.txt", "a")
f.write("Test\n")
f.close()


try:
	f = open("tt.txt", "r")
	print(f.read())
	f.close()
except:
	print("File Error")

# r: Opens a file for reading only

# r+: Opens a file for both reading and writing
# w: Opens a file for writing only
# w+: Open a file for writing and reading.

# a: Opens a file for appending
# a+: Opens a file for both appending and reading

while True:
	try:
		x = int(input("Please enter a number"))
		break
	except ValueError:
		print("That was not a number")

class Monster:
	def __init__(self):
		self.x = 1
	def printNumPlusOne(self, y):
		try:
			z = self.x + y
			print(z)
		except:
			raise Exception('number error')


monster = Monster()
try:
	monster.printNumPlusOne("lol")
except Exception as inst:
	print(type(inst))