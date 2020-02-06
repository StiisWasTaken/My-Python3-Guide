import rob
import pro             #import whole file and use anything you need as pro.variable or rob.function

print(rob.g,pro.g)            # before   pro g = 15   #  rob g = 10xpro g= 150
rob.g,pro.g=pro.g,rob.g       # swap
print(rob.g,pro.g)            # after   pro g = 150 a rob g = 15 ( po zamianie)



pro.fib(rob.g)
rob.fib2(rob.g)
rob.fib2(pro.g)  # you can import just one thing from whole file (you dont have to write "pro.smthg" all the time
                  # but it can be complicated if you use same names of variables
d=rob.add(rob.g,pro.g) # d= return from rob.add
print(rob.g,pro.g,d)

f=("text inversion")              #
print("text inversion",f[::-1])  # text inversion
