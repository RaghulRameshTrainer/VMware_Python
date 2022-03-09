import re
"""
match
search
findall
replace
split
compile-finditer

import re
str="pet:cat i love cat and pet:dog i love dog"
#res=re.match('\w+:\w+',str)
#res=re.search('...:...',str)
res=re.findall('...:...',str)
print(res)
"""
text_to_search="""abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Metacharacters (needs to e escaped):
. ^ $ * + ? { } [ ] \ |( )

https://www.vmware.com
http://www.vmware.com
https://vmware.com
https://www.vmware.co.us

VMware in india

Ha HaHa

+91-9898383849
9898383849
989838384
98983838455
8898383849
7898383849
6898383849
5898383849
4898383849
3898383849
2898383849
1898383849

321-555-4321
123.535.5775
323_545_5456
545 544 2345"""
#pattern=re.compile(r'https?://(www\.)?vmware\.com?(\.us)?')
#pattern=re.compile(r'(\d{3})[^\s](\d{3}[^\s]\d{4})')
#pattern=re.compile(r'\bHa\b')
pattern=re.compile(r'(2345)$')
#pattern=re.compile(r'vmware',re.I)
#pattern=re.compile(r'(\+91\-)?\b[5-9]\d{9}\b')
matches=pattern.finditer(text_to_search)
for x in matches:
    print(x.group())


