tuple_immutable_var = (1,"2",[2,3])
print(tuple_immutable_var)
#tuple_immutable_var [1] = 1 - нельзя поменять, так как в кортеже нет ображения к элементам
tuple_immutable_var[2] [1] = 4
print(tuple_immutable_var)
mutable_list = [1, 3,"basket",[1,2,3,4,5]]
mutable_list [0] = 5
mutable_list [2] = "bin"
mutable_list [1] = 'mister'
mutable_list [3] = [6,7,8,9]
print(mutable_list)
