def list_manipulator(nums, *args):
    command_1, command_2 = args[0:2]

    if command_1 == "add":
        nums_to_add = list(args[2:])
        if command_2 == "beginning":
            new_nums = nums_to_add + nums
        elif command_2 == "end":
            new_nums = nums + nums_to_add
        
    elif command_1 == "remove":
        count_to_remove = 1
        if len(args) > 2:
            count_to_remove = args[-1]

        if command_2 == "beginning":
            new_nums = nums[count_to_remove:]
        elif command_2 == "end":
            for _ in range(count_to_remove):
                nums.pop()
            new_nums = nums

    return new_nums


# print(list_manipulator([1,2,3], "remove", "end"))                   
# print(list_manipulator([1,2,3], "remove", "beginning"))             
# print(list_manipulator([1,2,3], "add", "beginning", 20))            
# print(list_manipulator([1,2,3], "add", "end", 30))                  
# print(list_manipulator([1,2,3], "remove", "end", 2))                
# print(list_manipulator([1,2,3], "remove", "beginning", 2))          
# print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))    
# print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))          