import re

def checkIP(ip):
    def checkIPNum(num):
        return 0 <= int(num) <= 255
    pattern = re.compile('^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$')
    m = pattern.match(ip)
    if (m):
        for num in m.groups():
            if not checkIPNum(num):
                return False
        return True
    return False


num = int(input())
for i in range(num):
    if checkIP(input()):
        print("True")
    else:
        print("False")



"""

import re
n = int(input())
list3 = []
for i in range(n):
    ip = ""
    a = 0
    count = 0
    list1 = []
    ip = str(input())
    a = ip.count(".")
    m = re.match(r"\.",ip)
    if m:
        list3.append("False")
        continue
    text = re.search(r"\.{2,100}" , ip)
    if text is None:
        if a >= 4:
            list3.append("False")
            continue
        list1 = ip.split(".")
        list2 = list(map(int,list1))
        for j in range(4):
            if list2[j] >= 0 and list2[j] <=255:
                count+=1
                if count == 4:
                    list3.append("True")
            else:
                list3.append("False")
    else:
        list3.append("False")
        continue
for n in range(len(list3)):
    print(list3[n])
"""
