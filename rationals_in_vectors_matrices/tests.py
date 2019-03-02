from matrix import *
from vector import *
from rational import *

def tests( ) :
    a11 = Rational( 1, 2 )     
    a12 = Rational( 1, 3 )
    a21 = Rational( -2, 7 )
    a22 = Rational( 2, 8 )
    b11 = Rational( -1, 3 )
    b12 = Rational( 2, 7 )
    b21 = Rational( 2, 5 )
    b22 = Rational( -1, 7 )


    m1 = Matrix( a11, a12, a21, a22 )
    m2 = Matrix( b11, b12, b21, b22 )
    m3 = m1.inverse()
    i = Matrix(a11=Rational(1), a22=Rational(1))

    m4 = m1 @ m2
    print ("m1 * m2: ")
    print( m4 )

    print ("The inverse of m1: ")
    print( m1.inverse())

    print("(m1 * m2) * m3 - m1 * (m2 * m3) = ")
    print((m1 @ m2) @ m3 - m1 @ (m2 @ m3))

    print("m1 * (m2 + m3) = m1 * m2 + m1 * m3  and  (m1 + m2) * m3 = m1 * m3 + m2 * m3")
    print("m1*(m2+m3) - m1*m3 - m1*m3: ")
    print(m1 @ (m2 + m3) - m1 @ m2 - m1 @ m3)

    print("(m1 + m2) * m3 - m1 * m3 - m2 * m3 =")
    print((m1 + m2) @ m3 - m1 @ m3 - m2 @ m3)
 
    v = Vector( 1, 2 )
    print("m1(m2(v)) - (m1 * m2)(v)")
    print(m1(m2(v)) - (m1 @ m2)(v))

    print("det(m1) * det(m2): ")
    print (m1.determinant() * m2.determinant())
        
    m19 = m1 @ m2
    d3 = m19.determinant()
    print( "det(m1*m2): " )
    print( d3 )

    m20 = m1.inverse( ) 
    print( "m1 * inverse( m1 ): ")
    print( m1 @ m20 )

    print( "inv( m1 ) * m1: " )
    print( m20 @ m1 )

    print(" m1*(inv(m1)) - inv(m1)*m1 : ")
    print( m1 @ m20 - m20 @ m1)
                
         





