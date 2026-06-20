def hcf(a, b):
       while b!= 0 :
              a, b = b, a%b
              return a
a = int(input("enter no. :")) 
b = int(input("enter no. :"))
result = hcf(a, b)
print(result)
