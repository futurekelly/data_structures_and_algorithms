def two_indces(nums,target):
    num_to_index={}
    for i, num in enumerate(nums):
        complement =target-num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
if __name__=="__main__":
    print(two_indces([2,7,11,15],9))
