import time
bottles = 10
for x in range(10):
    print("{0} green bottles, hanging on the wall".format(bottles))
    print("{0} green bottles, hanging on the wall".format(bottles))
    print("And if 1 green bottle should acidentally fall,")
    print("There'll be {0} green bottles hanging on the wall.".format(bottles-1))
    bottles-=1
    time.sleep(1)
