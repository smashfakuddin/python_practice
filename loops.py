# the for loop 

# with list 

name_list = ["ash","jay","rabin"]

for name in name_list:
    print("Good Morning", name)

# with range
for n in range(1,11):
    print(n)

# extract odd number with loop
for n in range(100):
    if n % 2 != 0:
        print(n)



# the While loops

count = 0
while count < 5:
    print(count)
    count += 1


# break and continue 

count = 0

while True:
    print(count)
    count += 1
    if count >= 5:
        break


for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)