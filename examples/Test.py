#!/usr/bin/env python

# -------
# Test.py
# -------

print "Test.py"

x = 5
e = 0.01
print "e =", e
l = 0
h = max(x, 1.0)
a = (h + l) / 2.0
print "l =", l, "a =", a, "h =", h
print "d =", a**2 - x
while (abs(a**2 - x) >= e) :
    if a**2 < x :
        l = a
    else :
        h = a
    a = (h + l) / 2.0
    print "l =", l, "a =", a, "h =", h
    print "d =", a**2 - x
print "a =", a

print "Done."
