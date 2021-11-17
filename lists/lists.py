import random

#1.Написать скрипт который создаст список целых чисел. 
#2.Написать скрипт который создаст список целых чётных чисел.
#3.Написать скрипт который создаст список целых нечётных чисел.

whole_nums = list(range(-35, 35))
print("Whole numbers = ", whole_nums)

even_nums = [x for x in whole_nums if not(x % 2)]
print("Even numbers = ", even_nums)

odd_nums = [x for x in whole_nums if x % 2]
print("Odd numbers = ", odd_nums)

#4.Написать скрипт который из списка целых чисел выведет чётные числа.
print("Even:")
[print(x) for x in whole_nums if not(x % 2)]


#5.Написать скрипт который из списка целых чисел выведет нечётные числа.
print("Odd:")
[print(x) for x in whole_nums if x % 2]

#6.Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
print("\n Divided by 5")
[print(x) for x in whole_nums if not(x % 5)]

#7.Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
count = 0
for x in whole_nums:
  if not(x % 5) : count +=1 
print("Even nums divided by 5 = ", count)

#8.Написать скрипт который создаст список целых рандомных чисел.
rand_whole_nums = [random.randint(0,100) for x in range(100)]
print("Random whole numbers = ", rand_whole_nums)

#9.Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
#separated_list = 

print("----------------")
temp_list = []
data = []
for i in range(len(whole_nums)):
  print("i = ", i, "value = ", whole_nums[i])
  if len(temp_list) == 5:
    data.append(temp_list)
    print("i = ", i, "data = ", data)
    print("i = ", i, "temp_list = ", temp_list)
    temp_list.clear()
  temp_list.append(whole_nums[i])

print("temp_list = ", temp_list)
print("data = ", data)
