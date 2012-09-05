#!/usr/bin/env python

# -------
# Test.py
# -------

print "Test.py"

a = [2, 3, 4]
a += [5]
assert a == [2, 3, 4, 5]

s = "a + [6]"
t = eval(s)
print t

print "Done."
