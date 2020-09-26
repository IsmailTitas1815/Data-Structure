days = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}

li = list(days)
li=li*52
li.append("monday")
firstdayofmonths = []
firstdayofmonths.append(li[1])
firstdayofmonths.append(li[32])
firstdayofmonths.append(li[60])
firstdayofmonths.append(li[90])
firstdayofmonths.append(li[121])
firstdayofmonths.append(li[151])
firstdayofmonths.append(li[182])
firstdayofmonths.append(li[213])
firstdayofmonths.append(li[243])
firstdayofmonths.append(li[274])
firstdayofmonths.append(li[304])
firstdayofmonths.append(li[335])
print(firstdayofmonths)

