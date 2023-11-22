
def get_maximum_subarray(arr):
    
    sum = 0
    max_sum = -999999

    for i in range(len(arr)):
        sum = sum + arr[i]

        if(sum < arr[i]):
            sum = arr[i]
        
        if(max_sum < sum):
            max_sum = sum

    return max_sum

def main():

    arr_list = list(map(int, input().split())) #[1,2,3,1]

    result = get_maximum_subarray(arr_list)

    print(result)

main()