#a variable defined inside a function can be used by functions defined inside that function

def Spaceship():
  x = 5
  def Lasers():
    print(x)
  Lasers()

Spaceship() 