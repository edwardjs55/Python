name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(list1, list2):
  new_dict = {}
  # your code here
  new_tuple = zip(list1,list2) #creates a list of tuples
  new_dict = dict(new_tuple)   # creates a dict from an Array
  print 'new tuple', new_tuple
  return new_dict


print  make_dict(name,favorite_animal)