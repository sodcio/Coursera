import sys

a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

d = b**2 - 4*a*c

x1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
x2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)

print('{0}\r\n{1}'.format(int(x1),int(x2)))
