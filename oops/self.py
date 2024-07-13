class employee:
  language = "python"
  salary = "120k"

  def getinfo(self): # you have to give a arguement it can be anything but self is used frequently in codes.
    print(f"The language is {self.language} and the salary is {self.salary}")

rohit = employee() # initiating the object

rohit.getinfo() # calling the function from the class
employee.getinfo(rohit) # This is same as the line above but the python covert the code from line(10) to that syntax.