__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''

def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    if base<2 or base>36:
        raise ValueError()
    k=[]
    x=number
    y=base
    n=0
    if x<0:
        n=1
        x=x*-1
    while x>y or x==y :
        l=x%y
        x=x//y
        if l==10:
            l='A'
        if l==11:
            l='B'
        if l==12:
            l='C'
        if l==13:
            l='D'
        if l==14:
            l='E'
        if l==15:
            l='F'
        if l==16:
            l='G'
        if l==17:
            l='H'
        if l==18:
            l='I'
        if l==19:
            l='J'
        l="{0}".format(l)
        k.append(l)
    l=x
    if l == 10:
        l = 'A'
    if l == 11:
        l = 'B'
    if l == 12:
        l = 'C'
    if l == 13:
        l = 'D'
    if l == 14:
        l = 'E'
    if l == 15:
        l = 'F'
    if l == 16:
        l = 'G'
    if l == 17:
        l = 'H'
    if l == 18:
        l = 'I'
    if l == 19:
        l = 'J'
    x="{0}".format(l)
    k.append(x)
    if n==1:
        k.append('-')
    k.reverse()
    str="".join(k)
    return str


def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        assert False, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert(10, 40)
        assert False, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert("100", 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print(te)

    try:
        convert(None, 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print(te)


    try:
        convert(100, "10")
        assert False, "Invalid base did not raise error"
    except TypeError as te:
        print(te)
