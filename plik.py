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

print (suma_ciagu([6,7,8,9,25]))
print (iloczyn_ciagu([6,7,8,9,45]))
print (srednia_ar([6,7,8,9,5]))
print (srednia_dod([-15,6,7,8,9,75]))
print (suma_iloczynow([5,6,7,8,9]))
