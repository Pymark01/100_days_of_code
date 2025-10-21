number = int(input("Type a positive integer: "))

bottom_square_number = 0
top_square_number = 0
x = 0

while top_square_number <= number:
    top_square_number = x*x
    bottom_square_number = (x - 1) * (x - 1)
    x += 1
    result_top = top_square_number - number
    result_bottom = number - bottom_square_number
#print(top_square_number)
#print(bottom_square_number)
#print(result_bottom)
#print(result_top)
if result_top < result_bottom:
    print(top_square_number)
else:
    print(bottom_square_number)




