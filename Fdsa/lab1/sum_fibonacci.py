def recurssionfibo(n):
   if n <= 1:
       return n
   else:
       return(recurssionfibo(n-1) + recurssionfibo(n-2))
nterms = 10
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recurssionfibo(i), end =" ")
