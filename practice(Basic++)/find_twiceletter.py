# There is a twice letter in a string named s find the twice leter.
def fi_twice(s):
  s0 = s.lower()
  s1 = list(s0)
  s1.sort()
  for i in range(1,len(s1)):
    if s1[i]==s1[i-1]:
      print(s1[i])

fi_twice("heymeitsmo")

  
