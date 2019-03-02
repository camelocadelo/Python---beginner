from scipy import *
from scipy.linalg import *

def solution ( ) :
    print( "here are the answers of Kamilla Kenzhekhankyzy\n" )

    m1 = array( [ [ 1/2, 1/3 ], [ -2/7, 2/ 8 ]] )
    m2 = array( [ [ -1/3, 2/7 ], [ 2/5, -1/7 ]] )
    m3 = array( [ [ -1/5,2/3], [1/8, 3/11]] )
    p = array( [ [ -1/30, 2/21 ], [ 41/210, -23/196 ] ] )
    I = array( [ [ 42, -56 ], [ 48, 84 ]] ) / 37
    v = array( [ 3.0, -1 ] )
    
    print( "This is part 1\n" )

    print( "The product of m1 and m2 is " )
    print( dot(m1, m2) )

    print( "The comparison of 2 products is: " )
    print( dot(m1, m2) - p )

    print( "This is part 2\n" )

    print( "The inverse of m1 is " )
    print( inv(m1) )

    print( "The inverse of m1 minus I is" )
    print( inv(m1) - I)
   
    print( "This is part 3\n" )

    temp = dot( m1, m2 )
    print( "The product (m1*m2)*m3 is" )
    print( dot( temp, m3 ) )

    temp2 = dot( m2, m3 )
    print( "The product m1*(m2*m3) is" )
    print( dot( m1, temp2 ) )

    print( "This is part 4\n" )

    print( "The matrix multiplication m1*(m2+m3) is: ")
    temp3 = m2+m3
    print( dot( m1, temp3 ) )

    print( "The matrix multiplication and addition m1*m2 + m1*m3 is: " )
    temp4 = dot(m1, m2)
    temp5 = dot(m1, m3)
    print( temp4+temp5 )

    print( "The matrix multiplication (m1+m2)*m3 is: ")
    temp6 = m1+m2
    print( dot( temp6, m3 ) )

    print( "The matrix multiplication and addition m1*m3 + m2*m3 is: ")
    temp7 = dot( m1, m3 )
    temp8 = dot( m2, m3 )
    print( temp7 + temp8 )

    print( "This is part 5\n" )

    temp9 = dot( m2, v)
    print( "The composition m1(m2(v)) is")
    print( dot( m1, temp9 ) )

    temp10 = dot(m1, m2)   
    print( "The composition (m1*m2)(v) is")
    print( dot( temp10, v ) )

    print( "This is part 6\n" )

    print( "The det(m1)*det(m2) is" )
    print( dot( det(m1), det(m2) ) )

    print( "The det(m1*m2) is" )
    print( det( dot( m1, m2) ) )

    print( "This is part 7\n" )

    print( "The inverse of a matrix is indeed an inverse: m1*inv(m1)" )
    print( dot( m1,inv(m1) ) )

    print( "The inverse of a matrix is indeed an inverse: inv(m1)*m1" )
    print( dot ( inv(m1), m1 ) ) 

