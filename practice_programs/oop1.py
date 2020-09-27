result=None
a=float(eval(input("Number 1:")))
b=float(eval(input("Number 2:")))

try:
    result=a/b
except Exception as e:
    print(("Error=",type(e)))
    print("end")
print(result)

