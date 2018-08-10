#!/usr/bin/python

def gcd(m,n):
  #let assume m >n
  if m<n :
    (m,n)=(n,m)

  if (m%n==0):
    return n
  else:
    diff=m-n
    return(gcd(max(n,diff),min(n,diff)))


a=int(input("enter first number"))
b=int(input("enter second number"))
print "gcd of numbers is : ",gcd(a,b)
