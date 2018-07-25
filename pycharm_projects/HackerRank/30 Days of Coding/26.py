actual = [int(i) for i in raw_input().split(" ")]
due = [int(i) for i in raw_input().split(" ")]
print actual
print due
if actual[2]>due[2]:
    print 10000
elif actual[2]<due[2]:
    print 0
else:
    if actual[1]>due[1]:
        print 500*(actual[1]-due[1])
    elif actual[1]<due[1]:
        print 0
    else:
        if actual[0] > due[0]:
            print 15*(actual[0]-due[0])
        else:
            print 0