# def maps(a):
#     #pass
#     list = []
#     for i in a:
#         list.append(i*2)
#     return(list)
#
# # or
def maps(a):
    return [2 * x for x in a]


print(maps([1, 2, 3, 4]))