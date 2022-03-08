Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[1,15,2,66,45,12]
>>> x[0]
1
>>> x[1]
15
>>> x[2]
2
>>> x[4]
45
>>> x[3]
66
>>> x=10
>>> type(x)
<class 'int'>
>>> x="Chennai")
SyntaxError: unmatched ')'
>>> x="Chennai"
>>> type(x)
<class 'str'>
>>> x=False
>>> type(x)
<class 'bool'>
>>> x=10
>>> x="Chennai"
>>> x=10
>>> x+=1
>>> x
11
>>> x>10
True
>>> x<10
False
>>> x==10
False
>>> x!=10
True
>>> name="Raghul Ramesh"
>>> len(name)
13
>>> name[0]
'R'
>>> name[1]
'a'
>>> name[2]
'g'
>>> name[0:5]
'Raghu'
>>> name[0:6]
'Raghul'
>>> name[-1]
'h'
>>> name[-2]
's'
>>> name[7:]
'Ramesh'
>>> name[7:13]
'Ramesh'
>>> name[-6:]
'Ramesh'
>>> name[-6:0]
''
>>> name[-6:-1]
'Rames'
>>> name[-6:]
'Ramesh'
>>> name[-6:-3]
'Ram'
>>> name[-3:-6]
''
>>> nam
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    nam
NameError: name 'nam' is not defined
>>> ma,e
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    ma,e
NameError: name 'ma' is not defined
>>> name
'Raghul Ramesh'
>>> name[-6:-3].reverse()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    name[-6:-3].reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> name[-6:-3][::-1]
'maR'
>>> name
'Raghul Ramesh'
>>> name[0:6]
'Raghul'
>>> name[:6]
'Raghul'
>>> name[:]
'Raghul Ramesh'
>>> name[::2]
'Rgu aeh'
>>> name[::3]
'Rh mh'
>>> name[::1]
'Raghul Ramesh'
>>> name[::-1]
'hsemaR luhgaR'
>>> name
'Raghul Ramesh'
>>> name.index('s')
11
>>> name.index('z')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    name.index('z')
ValueError: substring not found
>>> name.index('Ram')
7
>>> name.find('s')
11
>>> name.find('Ram')
7
>>> name.find('z')
-1
>>> name.find('a')
1
>>> name.find('a',1)
1
>>> name.find('a',2)
8
>>> name.find('a')
1
>>> name.rfind('a')
8
>>> test="Iamatrainer"
>>> test.find('a')
1
>>> test.find('a',4)
6
>>> name
'Raghul Ramesh'
>>> mystr="Raghul Ramesh from chennai"
>>> mystr.replace("chennai","bangalore")
'Raghul Ramesh from bangalore'
>>> 5=7
SyntaxError: cannot assign to literal
>>> x=5
>>> x+1
6
>>> x
5
>>> x=10
>>> x
10
>>> mystr
'Raghul Ramesh from chennai'
>>> mystr=mystr.replace("chennai","bangalore")
>>> mystr
'Raghul Ramesh from bangalore'
>>> mystr
'Raghul Ramesh from bangalore'
>>> mystr.replace('a','-')
'R-ghul R-mesh from b-ng-lore'
>>> #mystr.translate('abcde','12345')
>>> ord('a')
97
>>> ord(1)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    ord(1)
TypeError: ord() expected string of length 1, but int found
>>> ord('1')
49
>>> mystr.translate(97:49)
SyntaxError: invalid syntax
>>> mystr.translate({97:49})
'R1ghul R1mesh from b1ng1lore'
>>> mystr.translate({97:49,98:50})
'R1ghul R1mesh from 21ng1lore'
>>> str.maketrans('abcde','12345')
{97: 49, 98: 50, 99: 51, 100: 52, 101: 53}
>>> change=str.maketrans('abcde','12345')
>>> mystr.translate(change)
'R1ghul R1m5sh from 21ng1lor5'
>>> mycompany="VM-wa$ew"
>>> str.maketrans("~!@#$%^&*()_:><?","111111111111111"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> str.maketrans("~!@#$%^&*()_:><?","111111111111111")
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    str.maketrans("~!@#$%^&*()_:><?","111111111111111")
ValueError: the first two maketrans arguments must have equal length
>>> str.maketrans("~!@#$%^&*()_:><?","1111111111111111")
{126: 49, 33: 49, 64: 49, 35: 49, 36: 49, 37: 49, 94: 49, 38: 49, 42: 49, 40: 49, 41: 49, 95: 49, 58: 49, 62: 49, 60: 49, 63: 49}
>>> chng={126: None, 33: None, 64: None, 35: None, 36: None, 37: None, 94: None, 38: None, 42: None, 40: None, 41: None, 95: None, 58: None, 62: None, 60: None, 63: None}
>>> mycompany.translate(chng)
'VM-waew'
>>> str.maketrans("~!@#$%^&*-()_:><?","11111111111111111")
{126: 49, 33: 49, 64: 49, 35: 49, 36: 49, 37: 49, 94: 49, 38: 49, 42: 49, 45: 49, 40: 49, 41: 49, 95: 49, 58: 49, 62: 49, 60: 49, 63: 49}
>>> c={126: None, 33: None, 64: None, 35: None, 36: None, 37: None, 94: None, 38: None, 42: None, 45: None, 40: None, 41: None, 95: None, 58: None, 62: None, 60: None, 63: None}
>>> mycompany.translate(c)
'VMwaew'
>>> mycompany="VMw!a$r&e*"
>>> mycompany
'VMw!a$r&e*'
>>> mycompany.translate(c)
'VMware'
>>> dir(mycompany)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> company="VMWARE"
>>> company.center(100)
'                                               VMWARE                                               '
>>> company.center(50)
'                      VMWARE                      '
>>> company.center(50,"*")
'**********************VMWARE**********************'
>>> company.center(50,"-")
'----------------------VMWARE----------------------'
>>> company.center(50,".")
'......................VMWARE......................'
>>> company.ljust(50,".")
'VMWARE............................................'
>>> company.rjust(50,".")
'............................................VMWARE'
>>> city="Chennai-Bangalore-Hyderabad-Mumbai-Pune-Kolkatta-Delhi"
>>> city.split("-")
['Chennai', 'Bangalore', 'Hyderabad', 'Mumbai', 'Pune', 'Kolkatta', 'Delhi']
>>> c=city.split("-")
>>> c
['Chennai', 'Bangalore', 'Hyderabad', 'Mumbai', 'Pune', 'Kolkatta', 'Delhi']
>>> "-".join(c)
'Chennai-Bangalore-Hyderabad-Mumbai-Pune-Kolkatta-Delhi'
>>> ":".join(c)
'Chennai:Bangalore:Hyderabad:Mumbai:Pune:Kolkatta:Delhi'
>>> tech="   Python technology  "
>>> if tech=="Python technology":
	print("YES")

	
>>> tech.strip()
'Python technology'
>>> t=tech.strip()
>>> if t=="Python technology":
	print("YES")

	
YES
>>> tech.lstrip()
'Python technology  '
>>> tech.rstrip()
'   Python technology'
>>> tech.strip()
'Python technology'
>>> help(tech.strip())
No Python documentation found for 'Python technology'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help(str.strip)
Help on method_descriptor:

strip(self, chars=None, /)
    Return a copy of the string with leading and trailing whitespace removed.
    
    If chars is given and not None, remove characters in chars instead.

>>> tech="Python$"
>>> tech.strip("$")
'Python'
>>> help(str.index)
Help on method_descriptor:

index(...)
    S.index(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Raises ValueError when the substring is not found.

>>> help(str.find)
Help on method_descriptor:

find(...)
    S.find(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

>>> tech="Py$thon$"
>>> tech.strip("$")
'Py$thon'
>>> city
'Chennai-Bangalore-Hyderabad-Mumbai-Pune-Kolkatta-Delhi'
>>> city.partition("-")
('Chennai', '-', 'Bangalore-Hyderabad-Mumbai-Pune-Kolkatta-Delhi')
>>> city.partition("-",2)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    city.partition("-",2)
TypeError: partition() takes exactly one argument (2 given)
>>> city.partition("-")
('Chennai', '-', 'Bangalore-Hyderabad-Mumbai-Pune-Kolkatta-Delhi')
>>> city.rpartition("-")
('Chennai-Bangalore-Hyderabad-Mumbai-Pune-Kolkatta', '-', 'Delhi')
>>> x=10
>>> y=x
>>> x=x+5
>>> x
15
>>> y
10
>>> nums=list(range(1,101))
>>> nums
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> nums.index(66)
65
>>> str(nums).find(66)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    str(nums).find(66)
TypeError: must be str, not int
>>> str(nums).find("66")
252
>>> str(nums)
'[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]'
>>> ",".join(nums)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    ",".join(nums)
TypeError: sequence item 0: expected str instance, int found
>>> nums
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> ",".join(nums)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    ",".join(nums)
TypeError: sequence item 0: expected str instance, int found
>>> clrscr
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    clrscr
NameError: name 'clrscr' is not defined
>>> clr
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    clr
NameError: name 'clr' is not defined
>>> t1=(1,2,3)
>>> sum(t1)
6
>>> min(t1)
1
>>> max(t1)
3
>>> 