for i in range(1,101):
    i = ""
if i % 3 == 0 and i % 5 ==0:
    print "FizzBuzz!"
elif i % 3 == 0:
    print "Fizz!"
elif i % 5 == 0:
    print "Buzz!"
else: print str(i)


# Solution Code
# for x in range(1,101):
#     s = ""
#     if x % 3 == 0:
#         s += "Fizz"
#     if x % 5 == 0:
#         s += "Buzz"
#     if s == "":
#         s = x
#     print s
