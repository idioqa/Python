
#1) Создать переменную типа String
str0 = "Test string"

#2) Создать переменную типа Integer
num = 123

#3) Создать переменную типа Float
floatNum = 1.2

#4) Создать переменную типа Bytes
byteStr = b"some bytes string"

#5) Создать переменную типа List
mylist = [str0, num, floatNum]

#6) Создать переменную типа Tuple
myTuple = ('1', 'text', 3)

#7) Создать переменную типа Set
mySet = {1,2,3}

#8) Создать переменную типа Frozen set
frozenSet = frozenset(mySet)

#9) Создать переменную типа Dict
myDict = {
    'key' : 'value'
}

#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
for item in [str0, num, floatNum, byteStr, mylist, myTuple, mySet, frozenSet, myDict]:
    print(item, ' type of ' , type(item), '\n')

#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
str1 = 'First part and'
str2 = ' Second part'
str3 = str1 + str2
print(str3)

#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(str0, ' ', num)

#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(str0 + str(num))


