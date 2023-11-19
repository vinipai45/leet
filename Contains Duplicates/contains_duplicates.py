
def has_duplicates(arr):

    hash_map = {}

    for i in arr:
        if i in hash_map:
            return True

        hash_map[i] = i


    return False


def main():

    arr_list = list(map(int, input().split())) #[1,2,3,1]

    result = has_duplicates(arr_list)

    print(result)

main()

