def find_range(arr):    #function to find range (max-min) 
    if len(arr) < 3:          #making sure length is less than 3
        return "Range determination not possible"
    arr_range = max(arr) - min(arr)
    return arr_range
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):       #checking for only real numbers
    while True:
        try:
            val = float(input(f"Enter a real number {i+1}: "))
            arr.append(val)
            break
        except ValueError:
            print("Invalid input")
print("Range: ", find_range(arr))
