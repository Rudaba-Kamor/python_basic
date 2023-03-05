x = lambda a: a + 10
print(x(6))


x = lambda a, b: a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))
