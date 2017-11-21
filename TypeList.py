list1 = ['magical unicorns',19,'hello',98.98,'world']

sum = 0
str = ''

for data in list1:
    if isinstance(data, str):
        str = str + data + ' '
    else:
        sum = sum + data

if sum != 0 and str != '':
    print "The list you entered is of mixed type"
    print "Sum:", sum
    print "String:", str
elif sum != 0:
    print "The list you entered is of integer type"
    print "Sum:", sum
else:
    print "The list you entered is of string type"
    print "String:", str