import time
i = input("What is your character? ")
v = 0
q = 0
io = ord(i)
binarynumflipped = []
binarynum = []

while io != 0:
 io = int(io / 2)
 binarynumflipped.insert(v, io % 2)
 v += 1
 if io == 0:
     while v != 0:
         binarynum.insert(q, binarynumflipped[v - 1])
         v = v - 1
         q = q + 1
     if v == 0:
         print(binarynum)
         time.sleep(1)