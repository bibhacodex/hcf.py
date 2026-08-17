m ,n = int(input("enter first no: ")), int(input("enter second no.: "))

def gcd(m,n):
       if (m<n):       #assume m>n
              (m,n)=(n,m)

       if (m%n==0):
              return(n)
       else:
              diff = m-n
              return(gcd(max(diff,n),min(diff,n)))

print("GCD =", gcd(m, n))           