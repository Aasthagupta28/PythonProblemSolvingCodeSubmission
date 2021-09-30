#Problem set 2a
#Name: Aastha Gupta
#Time Spent: 2 hours

def evaluate_poly(poly, x):
    result=0
    for i in poly:
        result+=(poly[poly.index(i)]) * (x**(poly.index(i)))
    return result

poly =(0.0, 0.0, 5.0, 9.3, 7.0)
x=-13
print (evaluate_poly(poly,-13))
