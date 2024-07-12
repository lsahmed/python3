with open("/home/runner/python3/file i/gog.txt") as f:
  c = f.read()
  if("twinklle" in c):
    print("yes it is present")
  else:
    print("no it is not present")