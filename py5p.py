Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={1,2,3,4,5,6}
>>> si={1,2,40}
>>> s.intersection(si)
{1, 2}
>>> si.intersection(s)
{1, 2}
>>> s
{1, 2, 3, 4, 5, 6}
>>> si
{40, 1, 2}
>>> s.intersection_update(si)
>>> s
{1, 2}
>>> s={1,2,3,4,5,6}
>>> si
{40, 1, 2}
>>> si.intersection_update(s)
>>> si
{1, 2}
>>> 
>>> s
{1, 2, 3, 4, 5, 6}
>>> s.difference_update(si)
>>> s
{3, 4, 5, 6}
>>> si.difference_update(s)
>>> si
{1, 2}
>>> del(si)
>>> si
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    si
NameError: name 'si' is not defined
>>> si={1,2,3,4}
>>> s={1,2,3,4,5,6}
>>> s.symmetric_difference_update(si)
>>> s
{5, 6}
>>> si
{1, 2, 3, 4}
>>> s={1,2,3,4,5,6}
>>> s.issubset(si)
False
>>> s.issuperset(si)
True
>>> s.isdisjoint(si)
False
>>> s.pop()
1
>>> s
{2, 3, 4, 5, 6}
>>> s.pop()
2
>>> s
{3, 4, 5, 6}
>>> s={1,2,3,4,5,6}
>>> s1=frozenset({1,2,3,4})
>>> s1
frozenset({1, 2, 3, 4})
>>> s2=frozenset({2,3})
>>> s2
frozenset({2, 3})
>>> s2.union(s)
frozenset({1, 2, 3, 4, 5, 6})
>>> s
{1, 2, 3, 4, 5, 6}
>>> s2
frozenset({2, 3})
>>> l=[1,2,'Hi',5.0]
>>> for x in l:
	print(x)

	
1
2
Hi
5.0
>>> for y in l:
	print(y)

	
1
2
Hi
5.0
>>> for z in l:
	print(z)

	
1
2
Hi
5.0
>>> for a in l:
	print(a)

	
1
2
Hi
5.0
>>> for b in l:
	print(b)

	
1
2
Hi
5.0
>>> d={'a':1,'b':2}
>>> type(d)
<class 'dict'>
>>> d
{'a': 1, 'b': 2}
>>> for x in d:
	print(x)

	
a
b
>>> for y in d:
	print(y)

	
a
b
>>> for z in d:
	print(z)

	
a
b
>>> for a in d:
	print(a)

	
a
b
>>> for x in d.keys()
SyntaxError: invalid syntax
>>> for x in d.keys():
	print(x)

	
a
b
>>> for y in d.keys():
	print(y)

	
a
b
>>> for z in d.keys():
	print(z)

	
a
b
>>> for a in d.keys():
	print(a)

	
a
b
>>> for x in d.values():
	print(x)

	
1
2
>>> for y in d.values():
	print(y)

	
1
2
>>> for z in d.values():
	print(y)

	
2
2
>>> d
{'a': 1, 'b': 2}
>>> for a in d.values():
	print(z)

	
2
2
>>> for b in d.values():
	print(b)

	
1
2
>>> for x,y in d.items():
	print(x,z)

	
a 2
b 2
>>> for x,y in d.items():
	print(x,y)

	
a 1
b 2
>>> for a,b in d.items():
	print(a,b)

	
a 1
b 2
>>> 