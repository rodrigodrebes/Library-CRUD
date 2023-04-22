def fibonacci(n):
 if n <= 1:
  return 1
 else:
  return fibonacci(n-1) + fibonacci (n-2)

list =[]

for i in range(10):
 list.append(fibonacci(i))

print(list)