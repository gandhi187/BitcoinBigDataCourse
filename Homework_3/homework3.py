#@author David_Sharma_A08922101

def calculateEdges(a,b,c,d,e,f,g):
 sumEdges = (a+b+c+d+f+g) + (a*e) + (b*e) + (c*e) + (c*f) + (d*f) + (e*g)
 return sumEdges

def calculatePaths(a,b,c,d,e,f,g):
 sumPaths = g*(a*e+b*e+c*e)+c*f+d*f
 return sumPaths

a,b,c,d,e,f,g = [int(item) for item in input("Please enter the number of nodes for the seven clusters, sperated by an ',': ").split(",")]

print("Number of edges:3 ", calculateEdges(a,b,c,d,e,f,g))
print("Number of paths: ", calculatePaths(a,b,c,d,e,f,g))