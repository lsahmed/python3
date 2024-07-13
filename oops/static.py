class employee:
  language = "python"
  pkg = "120k"

  @staticmethod # marking as static method
  def greet(): 
    print("Good morning sir") # in this function i am not usign any attribute but to run the function i have to pass the whole object through it using self which increase time v  
                              # and space complexity to maintain it you can use @staticmethod

rohan = employee() # initiate the object
rohan.greet()