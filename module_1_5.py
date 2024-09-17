immutable_var = (1,True , "string")
print(immutable_var)
# Нельзя изменить элементы кортежа, так как он является неизмяемым объектом.
# Но можно заменить элементы внутри изменяемого объекта, который находится внутри кортежа :
# immutable_var = ([1,2],3,4)
# immutable_var[1][1]= 4
mutable_list = [1,2,True]
mutable_list[1] = 4
print(mutable_list)