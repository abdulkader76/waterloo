# Coding Exercise: Hypotenuse

#Define a function hypotenuse(a, b) which returns the length of the hypotenuse c, if the other two sides have lengths a and b.

def hypotenuse(a, b):
   c_squared = (a**2) + (b**2)
   return c_squared**(1/2)
   
# Coding Exercise: The Triangles are Right
# Using hypotenuse(a, b), define a function rightTrianglePerimeter(a, b) which returns the length of the perimeter in a right triangle whose non-hypotenuse sides have lengths a and b.

def rightTrianglePerimeter(a, b):
   c = hypotenuse(a, b)
   return a + b + c
   
   
# Coding Exercise: 2D Distance

#Assume hypotenuse(a, b) has already been defined. Using it, define a function distance2D(x1, y1, x2, y2) which calculates the distance between the point (x1, y1) and the point (x2, y2).

def distance2D(x1, y1, x2, y2):
   a = x1 - x2
   b = y1 - y2
   c = hypotenuse(a, b)
   return c
   
# Coding Exercise: Secure the Perimeter

# Assume distance2D(x1, y1, x2, y2) has already been defined. Using it, define a function trianglePerimeter(xA, yA, xB, yB, xC, yC) which calculates the perimeter of a triangle whose three points are (xA, yA), (xB, yB) and (xC, yC).

def trianglePerimeter(xA, yA, xB, yB, xC, yC):
   a = distance2D(xA, yA, xB, yB)
   b = distance2D(xA, yA, xC, yC)
   c = distance2D(xB, yB, xC, yC)
   return a + b + c