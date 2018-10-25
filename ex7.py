try:
    f = open("1.txt","r")
    f.read()
except Exception as msg:
    print(msg)
else:
    print(1)