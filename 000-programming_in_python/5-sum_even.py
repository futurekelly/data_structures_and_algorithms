def sum_even_number(my_list):
    return sum(y for y in my_list if y %2 ==0)

if __name__=="__main__":
     print( sum_even_number([2,4,5,7,9]))