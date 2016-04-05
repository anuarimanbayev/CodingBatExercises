## CodingBat
## Warmup-1 > makes10

## PROBLEM STATEMENT
## Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10. 
## makes10(9, 10) → True
## makes10(9, 9) → False
## makes10(1, 9) → True

## MY SOLUTION:
def makes10(a, b):
  if (a == 10 or b == 10) or (a + b == 10):
     return True
  else:
     return False

## OFFICIAL SOLUTION:
def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)