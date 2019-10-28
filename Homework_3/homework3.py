#@author David_Sharma_A08922101


def calculateEdges(a,b,c,d,e,f,g):
 sumEdges = (a+b+c+d+f+g) + (a*e) + (b*e) + (c*e) + (c*f) + (d*f) + (e*g)
 return sumEdges

def calculatePaths(a,b,c,d,e,f,g):
 sumPaths = g*(a*e+b*e+c*e)+c*f+d*f
 return sumPaths

# read the user's input
a,b,c,d,e,f,g = [int(nodes) for nodes in input("Please enter the number of nodes for the seven clusters, sperated by an ',' (seven numbers): ").split(",")]

print("Number of edges:3 ", calculateEdges(a,b,c,d,e,f,g))
print("Number of paths: ", calculatePaths(a,b,c,d,e,f,g))