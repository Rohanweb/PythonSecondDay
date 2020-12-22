# import os
# from contextlib import contextmanager
#
# # #### CD Example ####
# #
# # cwd = os.getcwd()
# # os.chdir('Sample-Dir-One')
# # print(os.listdir())
# # os.chdir(cwd)
# #
# # cwd = os.getcwd()
# # os.chdir('Sample-Dir-Two')
# # print(os.listdir())
# # os.chdir(cwd)
#
#
# @contextmanager
# def change_dir(destination):
#     try:
#         cwd = os.getcwd()
#         os.chdir(destination)
#         yield
#     finally:
#         os.chdir(cwd)
#         print("Came in finally")
#         print(os.listdir())
#
#
# with change_dir('Dir-Ones'):
#     print(os.listdir())
#
# with change_dir('Dir-Two'):
#     print(os.listdir())


## Iterables and Iterators
## Iterable can be iterated upon
## Iterator is an object which iterates upon iterables
## Iterators can also be Iterable in turn

# a=[1,2,3,4,5,6,7,8,9,90,102,133,224,899]
# myiter=iter(a)
# print(type(a))
# print(dir(myiter))
# for i in a:
#     print(i)
#
# for i in range(10):
#     print(i)

data=(x*x for x in range(4))
print(data)
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))

