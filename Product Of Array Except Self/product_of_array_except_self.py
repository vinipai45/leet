
def get_product_of_array_except_self(arr) : 
   
    reversed_arr = arr[::-1]
    
    product = 1
    
    forward_product = []
    reverse_product = []
    result_product = []

    for i in range(0,len(arr)):
        res = arr[i] * product
        forward_product.append(res)
        product = res

    product = 1

    for i in reversed(range(0,len(arr))):
        res = arr[i] * product
        reverse_product.append(res)
        product = res

    reverse_product.reverse()

    for i in range(len(arr)):
        if(i==0):
            result_product.append(reverse_product[i+1])

        elif(i==len(arr)-1):
            result_product.append(forward_product[i-1])

        else:
            result_product.append( forward_product[i-1] * reverse_product[i+1] )

    return result_product

def main():

    arr_list = list(map(int, input().split())) #[1,2,3,1]

    result = get_product_of_array_except_self(arr_list)

    print(result)

main()