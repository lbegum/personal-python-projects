class Person:
  def __init__(self, name, profession, location):
    self.name = name
    self.profession = profession
    self.location = location

# this code instantiates an aspiring software engineer who enjoys solving problems.

LATHIFA = Person("Lathifa Begum", \
    "Science teacher by day, aspiring software engineer by night", \
    "London")

print(LATHIFA.profession)