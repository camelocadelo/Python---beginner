from scipy import *
from scipy.linalg import *
from timeit import *

#Python takes ~from 200-800 times as much time it takes C++ to run the method approx/ main. It can be explained by the fact that Python is dynamic language, so a lot of things that are done during compile time in static languages like C++ is done during runtime. As Python has dynamic typing, there are no types in it, and the programmer does not define them during writing the code, instead the types are being decided during runtime. We observed the clear demonstration of this difference while implementing C++ Runge_Kutta methods in Python. If the methods in C++ were implemented as templates, in Python we didn't do that on account of its dynamic typing.
#Tables can be printed by calling methods print_table() for Python values for error and print_table2() for time values comparison. 
# runge_kutta1 is Euler's method:

def runge_kutta1( F, x, h ) : 
   k1 = F( x ) 

   return x + h * k1 

# runge_kutta 21:

def runge_kutta21( F, x, h ) :
    k1 = F( x )
    k2  = F( x + h*k1 )
    
    return x + h * ( 0.5 * k1 + 0.5 * k2 )
    
# runge_kutta 22:

def runge_kutta22( F, x, h) :
    k1 = F( x )
    k2 = F( x + 0.5 * h * k1 )
    
    return x + h * k2
    
# runge_kutta 31:

def runge_kutta31( F, x, h ) :
    k1 = F( x )
    k2 = F( x + h * (2.0 / 3.0) * k1 )
    k3 = F( x + h * ( (1.0 / 3.0) * k1 + (1.0 / 3.0) * k2 ) )
    
    return x + h * ( (1.0/4.0) * k1 + (3.0/4.0) * k2 ) 
    
# The Standard Runge Kutta method

def runge_kutta41( F, x, h ) :
    k1 = F( x )
    k2 = F( x + 0.5 * h * k1)
    k3 = F( x + 0.5 * h * k2)
    k4 = F( x + h * k3 )
    
    return x + (1.0 / 6.0 ) * h * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    
# A fourth order method by J.Kuntzmann. Accuracy is 
# approximately two times better than standard Runge Kutta. 

def runge_kutta4_kuntzman( F, x, h ) :
    k1 = F( x )
    k2 = F( x + h * (2.0/5.0) * k1 )
    k3 = F( x + h * ( (-3.0/20.0) * k1 + (3.0/4.0) * k2 ) )
    k4 = F( x + h * ( (19.0/44.0) * k1 + (-15.0/44.0) * k2 + (40.0/44.0) * k3 ) )

    return x + h * ( (55.0/360.0) * k1 + (125.0/360.0) * k1 + 
           (125.0/360.0) * k3 + (55.0/360.0) * k4 )
                    
#A fifth-order Runge Kutta method with six stages:
#(Page 92 in J.C.Butcher, Numerical Methods for Ordinary Differential
#Equations.) 

def runge_kutta5( F, x, h) : 
    k1 = F( x )
    k2 = F( x + h * (1.0/4.0) * k1 )
    k3 = F( x + h * ( (1.0/8.0) * k1 + (1.0/8.0) * k2 ) )
    k4 = F( x + h * (1.0/2.0) * k3 )
    k5 = F( x + h * ( (3.0/16.0) * k1 + (-3.0/8.0) * k2 + 
         (3.0/8.0) * k3 + (9.0/16.0) * k4 ) )
    k6 = F( x + h * ( (-3.0/7.0) * k1 + (8.0/7.0) * k2 + 
         (6.0/7.0) * k3 + (-12.0/7.0) * k4 + (8.0/7.0) * k5 ) )
    
    return x + h * ( (7.0 / 90.0 ) * k1 + ( 32.0 / 90.0 ) *k3 + 
           ( 12.0 / 90.0 ) * k4 + (32.0 / 90.0 ) * k5 + (7.0 / 90.0 ) * k6)
    
#approx
def approx( h = 1.0E-5 ) :
   print( "testing Runge-Kutta methods on the catenary" )

   x0 = 0.0
   x1 = 1.0

   mu = 2.0

   s0 = array( [ 1.0 / mu, 0.0 ] )

   p = s0
   x = x0

   def cat( p ) :
      return array( [ p[1], mu * sqrt( 1.0 + p[1] * p[1] ) ] )

   while x + h < x1 :
      p = runge_kutta1( cat, p, h )
      x += h

   p = runge_kutta1( cat, p, x1 - x )
   x = x1

   print( "h = ", h )
   print( "final value = ", p )

   expected = array( [ cosh( mu * x1 ) / mu, sinh( mu * x1 ) ] )
   error = p - expected

   print( "error = ", error )

def print_table () :

    print('Table for python results: ')
    print('h1 = 1*10^-3, h2 = 2*10^-3, h3 = 4*10^-3')

    methods = ['Euler', 'Heun', 'Standard']
    h1 = ['[-0.00304834 -0.00497444]', '[-1.03556852e-06 -1.38790976e-06]',
         '[-1.67421632e-13     -2.38031816e-13]']
    h2 = ['[-0.00608604 -0.00992802]', '[-4.13730925e-06 -5.54565811e-06]', 
         '[-2.66120459e-12 -3.72901710e-12]']
    h3 = ['[-0.01212979 -0.01977312]', '[-1.65094891e-05 -2.21345750e-05]',
         '[-4.24467128e-11 -5.95541394e-11]']

    titles = ['Method', 'h1', 'h2', 'h3']
    data = [titles] + list(zip(methods, h1, h2, h3))

    for i, d in enumerate(data):
        line = '|'.join(str(x).ljust(39) for x in d)
        print(line)
    if i == 0:
        print('-' * len(line))

def print_table2 () :
    print('Table time values: ')
    print('h1 = 1*10^-5, h2 = 1*10^-6, h3 = 1*10^-6')
    
    Language = ['C++', 'Python']
    Euler, h1 = ['0m0,008s', '1.608 s' ]
    Heun, h2 = [ '0m0.071 s', '39.734']
    Standard, h3 = ['0m0.101 s','65.535 s ']

    titles = ['Language', 'Euler, h1', 'Heun, h2', 'Standard, h3']
    data = [titles] + list(zip(methods, h1, h2, h3))

    for i, d in enumerate(data):
        line = '|'.join(str(x).ljust(20) for x in d)
        print(line)
    if i == 0:
        print('-' * len(line))

