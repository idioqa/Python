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

def separate(arr, size):
    sep_arr = []
    while len(arr) > size:
        piece = arr[:size]
        sep_arr.append(piece)
        arr = arr[size:]
    sep_arr.append(arr)
    return sep_arr

print(separate(whole_nums, 5))

#10.Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел. 

def split_odd_even(arr):
  odd = []
  even = []
  for i in arr:
    if i % 2: odd.append(i)
    elif not(i % 2): even.append(i)
  return [odd, even]

print(split_odd_even(whole_nums))

#11.Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.

def unite(arr):
  unite_arr = []
  for i in arr:
    unite_arr += i
  return unite_arr
    
print("unite = ", unite(separate(whole_nums, 5)))

#12.Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars 

def sum_list(arr):
  sum_arr = []
  for i in arr:
    sum = 0
    for j in range(len(i)):
      sum += i[j]
    sum_arr.append(sum)
  return sum_arr

print(sum_list(separate(whole_nums, 5)))
      