class employee:
  language = "python"
  pkg = "120k"

  def __init__(self, name, language, pkg): # all __x__ methods in python are known as dunder method which is automatically called even if you dont call the function.
    self.name = name
    self.language = language
    self.pkg = pkg
    print("Good morning sir")

rohan = employee("rohit", "javascript", 130000 ) # even when the object is only initiate the dunder method will called only __init__ method called automatically evertimer
print(rohan.name, rohan.language, rohan.pkg)