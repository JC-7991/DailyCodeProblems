def print_max(arr, X, Y):

    max = 0
 
    for i in range(X - Y + 1):

        max = arr[i]
        for j in range(1, Y):
            if arr[i + j] > max:
                max = arr[i + j]

        print(str(max) + " ", end = "")
 
if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    X = len(arr)
    Y = 3
    print_max(arr, X, Y)