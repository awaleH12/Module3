#1 - Sort
#2 - Add 3 numbers
#3 - slice 5 largest numbers
#4 - slice 3 smallest numbers
#5 - delete even numbers


my_list = []
for number in range(1,21):
    my_list.append(number)
    

my_list2 = [21,22,23]
for number in my_list2:
    my_list.append(number)



print(my_list)

my_list.sort()
print(my_list[18:24])
print(my_list[0:3])
my_list.reverse()

for numbers in my_list:
    if numbers%2 == 0:
        my_list.remove(numbers)
     


print(my_list)




