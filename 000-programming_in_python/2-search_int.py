def find_first_occurence(my_list, num):
    try:
        return my_list.index(num)
    except ValueError:
      return -1
if __name__=="__main__":
    print(find_first_occurence([2,3,4,5,6,7],5))

 
