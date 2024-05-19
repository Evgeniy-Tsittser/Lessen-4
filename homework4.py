immutable_var = (3,6,'work',12,'это кортеж')
print(immutable_var)
# immutable_var[1] = 10 Error Содержимое кортежа неизменно
mutable_list = [2,5,'engin', 'motor','это список']
print(mutable_list)
mutable_list[4] = ' это измененный список! '
print(mutable_list)