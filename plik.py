def suma_ciagu(a):
    w = 0
    for i in a:
        w += i
    return w

def iloczyn_ciagu(a):
    w = 1
    for i in a:
        w *= i
    return w

def srednia_ar(a):
    w = 0
    for i in a:
        w += i
    return w/len(a)

def srednia_dod(a):
    w = 0
    il = 0
    for i in a:
        if (i > 0):
            w += i
            il += 1
    return w/il

def suma_iloczynow(a):
    w = 0
    w2 = 1
    for i in a:
        w2 *= i
        w += w2
    return w

print (suma_ciagu([1,2,3,4,5]))
print (iloczyn_ciagu([1,2,3,4,5]))
print (srednia_ar([1,2,3,4,5]))
print (srednia_dod([-15,1,2,3,4,5]))
print (suma_iloczynow([1,2,3,4,5]))
