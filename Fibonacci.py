def fib(num):
   a = 1
   b = 1
   # Create a list for the Fibonacci sequence
   fibsequence = []
   for i in range (num):
      #Append the value of a to the Fibonacci sequence list
      fibsequence.append(a)
      a, b = b, a + b

   return fibsequence

