class employee:  # basic syntax of class 
  lang = "py"
  package = 600000

ahmed = employee() # object instatiation
ahmed.name = "ahmed" # as i mentioned the name after creating the class 
print(ahmed.name, ahmed.lang, ahmed.package)  # its now called as object or instance
# Here name is an obbject or instance attribute while lang and package are class attribute.
rohit = employee()
rohit.name = "rohit"
rohit.package = 1200000 # here in rohit.package 1200000 will print instead of 600000 bcz instance attribute take more preferences than class attribute
print(rohit.name, rohit.lang, rohit.package)

