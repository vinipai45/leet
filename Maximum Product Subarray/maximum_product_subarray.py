
def get_maximum_product_subarray(arr):
    
    reversed_arr = arr[::-1]
    product = 1
    max_product = -999999

    for i in range(len(arr)):

        product = product * arr[i]

        max_product = max(product,max_product)

        if(product == 0):
            product = 1

    product = 1

    for i in range(len(arr)):
        product = product * reversed_arr[i]

        max_product = max(product,max_product)

        if(product == 0):
            product = 1

    return max_product

def main():

    arr_list = list(map(int, input().split())) #[1,2,3,1]

    result = get_maximum_product_subarray(arr_list)

    print(result)

main()