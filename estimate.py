import random
import math

def wallis(num):
  pi = 1
  for x in range(1,num):
      pi=pi*((4*x**2)/((4*x**2)-1))
  print("Value of pi is:",pi*2)
  return pi


def monte_carlo(darts):
  point_circle=0
  for y in range(1,darts):
     point_x=random.random()
     point_y=random.random()
     d=math.sqrt(point_x**2+point_y**2)
     if d<=1:
        point_circle=point_circle+1
  pi=4*(point_circle/darts)
  return pi      
           
        
