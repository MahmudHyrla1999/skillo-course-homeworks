ls = [1, 2, 3]
tpl = (4, 5, 5, 5)


ls.remove(1)

ls.insert(2,1)
ls.pop(2)
print(ls)
print(ls.pop())
print(ls.index(2))

print(tpl.count(5))
print(tpl.index(5))

tpl += tpl
print(tpl)