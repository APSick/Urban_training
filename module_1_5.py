immutable_var = (1, 2, 3, 4, 5, "rdf", True)
print(immutable_var)
#immutable_var[0] = 777
#print(immutable_var)
#Кортеж так же, как и список, является коллекцией, но в отличие от него он неизменяем. К неизменяемым объектам помимо кортежей относятся числа и строки.

mutable_list = [1, 2, 3, 4, 5]
print(mutable_list)
mutable_list[3] = 777
print(mutable_list)
mutable_list[1] = True
print(mutable_list)
mutable_list[0] = "qwerty"
print(mutable_list)