#Problem set 2c
#Name: Aastha Gupta
#Time Spent: 3 hours

def evaluate_poly(poly, x):
    result=0
    for i in poly:
        result+=(poly[poly.index(i)]) * (x**(poly.index(i)))
    return result

poly =(0.0, 0.0, 5.0, 9.3, 7.0)
x=-13
print (evaluate_poly(poly,-13))



def Compute_deriv(poly):
    Result=()
    for i in poly:
        if(poly.index(i))>0:
            Result= Result+(((poly.index(i))*i),)
    return Result
poly=(-13.39, 0.0, 17.5, 3.0, 1.0)
print (Compute_deriv(poly))



def compute_root(poly, x_0, epsilon):

   root = x_0
   counter = 1
   while (abs(evaluate_poly(poly, root)) >= epsilon):
        root = root - (evaluate_poly(poly, root) /(evaluate_poly(Compute_deriv(poly), root)))
        counter += 1
   return (root, counter)

poly = (-13.39, 0.0, 17.5, 3.0, 1.0) 
x_0 = 0.1
epsilon = .0001
print (compute_root(poly, x_0, epsilon))
