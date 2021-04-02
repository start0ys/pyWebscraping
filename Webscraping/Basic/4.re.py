import re

p=re.compile("ca.e")
m=p.match("caffe")
def asd(m):   
    if m:
        print("m.group():",m.group())
        print("m.string():",m.string)
        print("m.start():",m.start())
        print("m.end():",m.end())
        print("m.span():",m.span())

    else:
        print("매칭되지않음")

m=p.match("careless")
asd(m)