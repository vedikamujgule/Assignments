# (Geography: estimate areas) Find the GPS locations for Atlanta, Georgia;
# Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina from
# www.gps-data-team.com/map/ and compute the estimated area enclosed by these
# four cities. (Hint: Use the formula in Programming Exercise 3.2 to compute the
# distance between two cities. Divide the polygon into two triangles and use the formula
# in Programming Exercise 2.14 to compute the area of a triangle.)

import math

x1 = 33.748783 #Atlanta
y1 = -84.388168

x2 = 28.538336 #orlando
y2 = -81.379234

x3 = 32.076176
y3 = -81.088371 #Savannah

x4 = 35.227085
y4 = -80.843124 #Charlotte

side1 = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
side2 = math.sqrt(math.pow(x2 - x3, 2) + math.pow(y2 - y3, 2))
side3 = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))
s = (side1 + side2 + side3) / 2 
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

side1 = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))
side2 = math.sqrt(math.pow(x4 - x3, 2) + math.pow(y4 - y3, 2))
side3 = math.sqrt(math.pow(x1 - x4, 2) + math.pow(y1 - y4, 2))
s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3)) + area

print("The area covered by 4 cities is", area, "km^2")