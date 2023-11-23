
def get_maximum_subarray(arr):
    
    sum = 0
    max_sum = -999999

    for i in range(len(arr)):
        sum = sum + arr[i]

        sum = max(sum,arr[i])
        
        max_sum = max(max_sum,sum)

    return max_sum

def main():

    arr_list = list(map(int, input().split())) #[1,2,3,1]

    result = get_maximum_subarray(arr_list)

    print(result)

main()