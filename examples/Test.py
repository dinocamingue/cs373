#!/usr/bin/env python

# -----------
# Closures.py
# -----------

print "Closures.py"

def f () :
    v = [2, 3, 4]
    def g () :
        print v
        v += [5]
        return v
    return [g, g]

a = f()
assert a[0]() == [2, 3, 4, 5]

print "Done."
