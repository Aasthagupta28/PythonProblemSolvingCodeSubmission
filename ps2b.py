#Problem set 2b
#Name: Aastha Gupta
#Time Spent: 1 hours


def Compute_deriv(poly):
    Result=()
    for i in poly:
        if(poly.index(i))>0:
            Result= Result+(((poly.index(i))*i),)
    return Result
poly=(-13.39, 0.0, 17.5, 3.0, 1.0)
print (Compute_deriv(poly))
