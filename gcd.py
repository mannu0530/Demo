#!/usr/bin/python

def gcd(m,n):
  #let assume m >n
  if m<n :
    (m,n)=(n,m)

  if (m%n==0):
    return n
  else:
    return(gcd(n,m%n))

a=int(input("enter first number"))
b=int(input("enter second number"))
print "gcd of numbers is : ",gcd(a,b)

      
