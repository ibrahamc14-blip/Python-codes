import random
list1 =[]
list2 =[]
list3 =[]

for n in range(0,31):
    list1.append(n)
for n in range(31,70):
    list2.append(n)
for n in range(70,101):
    list3.append(n)

print(list1)
print(list2)
print(list3)

# assign grades to 2 students

print('printing grades now')

all_grades = list1+list2+list3

print(all_grades)


for s in range(20):
    student=random.choice(all_grades)
    print(student)
