# x=0
# while x<=10:
#     x += 1
#     if x == 5:
#         #break
#         continue
#     print(x)
#
# print("I am out of the loop")
# while x<=10:
#     print(x)
#     x=x+1

# for x in [1,15,2,66,45,12]:
#     print(x)
#
#
# x=[1,15,2,66,45,12]
#
# s=0
# while s<len(x):
#     print(x[s])
#     s+=1   #s=s+1    #break and continue

import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,3],label="Example-One",width=0.5)
plt.bar([2,4,6,8,10],[8,6,2,5,6],label="Example-Two",color="g",width=0.5)
plt.legend()
plt.title("Bar Graph")
plt.xlabel("height")
plt.ylabel("Weight")
plt.show()