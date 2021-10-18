import mod1

print(mod1.add(1, 2))
print(mod1.sub(3, 2))

from mod1 import add, sub

print(add(1, 2))
print(sub(1, 2))

from mod1 import *

print(add(1, 2))
print(sub(1, 2))

print()

import mod2

print(mod2.PI)

print()

a = mod2.Math()
print(a.solv(5))

print(a.add(mod2.PI, 4.4))

print()

import game.sound.echo

game.sound.echo.echo_test()

from game.sound.echo import *

echo_test()