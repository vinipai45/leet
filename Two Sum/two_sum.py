
def get_indexs(arr:list,target:int):

    numsMap = {}
    nums_length = len(arr)

    for i in range(nums_length):
        numsMap[arr[i]] = i

    for i in range(nums_length):
        difference = target - arr[i]
        if (difference) in numsMap and numsMap[difference] != i :
            return[
                i,
                numsMap[difference]
            ]

    return []

def main():

    nums = list(map(int, input().split())) 
    target = int(input()) #9

    # temp_arr = nums
    # temp_arr.sort()
    # print(nums)
    # removed_larger_number = eliminate_number_larger_than_target(temp_arr,target)
    result = get_indexs(nums,target)

    print(result)


main()