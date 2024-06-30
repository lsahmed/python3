#Spam filter 

l = ["clcik here","free mac","free money"]
n = input("enter your post: ")
for i in l:
  if(i.lower() in n.lower()):
    print("This post has spams")
    break
else:
  print("This post doesnt contain spams")