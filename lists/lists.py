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

print("sum_list = ", sum_list(separate(whole_nums, 5)))

#13. Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка. 
# В одном списке внутренние списки из 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100. 
# Если какого-то списка не получится, то вместо него вернуть текст “No lists”

def two_sum_list(arr):
  sum_arr_less = []
  sum_arr_more = []
  temp_arr = []
  for i in arr:
    sum = 0
    for j in range(len(i)):
      sum += i[j]
      temp_arr.append(i[j])
    if(sum >= 100):
      sum_arr_more.append(temp_arr)
    elif( sum < 100):
      sum_arr_less.append(temp_arr)
    temp_arr = []
  if(len(sum_arr_less) == 0): 
    sum_arr_less == "No lists"
  if(len(sum_arr_more) == 0): 
    sum_arr_more == "No lists"
  return sum_arr_less, sum_arr_more

print("Two lists with >= 100 and < 100", two_sum_list(separate(whole_nums, 5)))

#16. Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.
#17. Написать скрипт который сгенерирует список имён файлов. К каждому имени  
# файла надо прикрепить номер итерации цикла как порядковый номер. 

def create_users(pattern, n):
  users = [pattern + str(i) for i in range(n)]
  return users

print("Users: ", create_users("User", 100))

#18. Написать скрипт который сгенерирует список списков. Каждый элемент списка это список в котором 
# 0-й элемент - это имя пользователя, а 1-й - элемент это дата регистрации.

from random import randrange
from datetime import timedelta

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

from datetime import datetime
d1 = datetime.strptime('1/1/1993 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')

def create_users_list(pattern, n): return [[pattern + str(i), str(random_date(d1, d2))] for i in range(n)]

my_users = create_users_list("login", 100)
print(my_users)

#19. Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором:
#0-й - элемент - это имя пользователя,
#1-й - элемент - это логин,
#2-й - элемент - это пароль,
#3-й - элемент - это email (email тоже генерировать),
#4-й - элемент - это дата регистрации

import secrets
import string

def get_password():
  return ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(20))

def get_email(name, login):
  return name + login + "@" + "gmail.com"

def create_employees_list(n): 
  return [
    [
      "name" + str(i),
      "login" + str(i), 
      str(datetime.now()), 
      get_email("Name" + str(i), "Login" + str(i)),
      get_password()
      ] 
    for i in range(n)]

print(create_employees_list(100))

#20.Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
#0-й - элемент - это логин,
#1-й - элемент - это имя,
#2-й - элемент - семейный статус (True, False - генерировать рандомно)

def generate_family_list(n):
  return [[
    "login" + str(i), 
    "name" + str(i),
    random.choice([True, False])
    ] for i in range(n)]
  
print("\nFamily: ", generate_family_list(10))

#21. Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
#0-й - элемент - это логин,
#1-й - элемент - это имя,
#2-й - элемент - гендер (1-м, 0-ж)

def get_genders(n):
  return [[
      "login" + str(i), 
      "name" + str(i),
      random.randint(0, 1)
    ] for i in range(n)]
  
print("\nGenders: ", get_genders(10))

#22. Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
#0-й - элемент - это логин,
#1-й - элемент - это имя,
#2-й - элемент - зарплата (генерироовать от 300$ до 5000$)

def get_salaries(n):
  return [[
      "login" + str(i), 
      "name" + str(i),
      str(random.randint(300, 5000))
  ] for i in range(n)]
  
print("\nSalaries: ", get_salaries(10))

#23. Написать скрипт который создаст список имён работников из salary у которых ЗП от 1500$ до 3000$
avg_salaries = []
for item in get_salaries(100):
  if int(item[2]) > 1500 and int(item[2]) > 3000: avg_salaries.append(item[0])
  
print("avg_salaries: ", avg_salaries)

#24.Написать скрипт который создаст список имён мужчин из gender.
#25.Написать скрипт который создаст список имён женщин из gender.
man = [i[0] for i in get_genders(100) if i[2] == 0]
print("\nMan: ", man)

woman = [i[0] for i in get_genders(100) if i[2] == 1]

#26.Написать скрипт который создаст список имён неженатых мужчин из family.
#27.Написать скрипт который создаст список имён незамужних женщин из family.

unmarried = [i[0] for i in generate_family_list(100) if i[2] == False]
unm_man = []
for i in man:
  for j in unmarried:
    if i == j: unm_man.append(i)

print("Unmarried man: ", unm_man)

unm_woman = []
for i in woman:
  for j in unmarried:
    if i == j: unm_woman.append(i)

print("Unmarried woman: ", unm_woman)