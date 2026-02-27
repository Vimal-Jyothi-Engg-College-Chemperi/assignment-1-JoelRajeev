def reverse_integer(n):
    
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = int(str(n)[::-1])
    return sign * reversed_n

if __name__ == "__main__":
    try:
        num_str = input("Enter an integer: ")
        num = int(num_str)
        print(f"Reversed integer: {reverse_integer(num)}")
    except ValueError:
        print("Please enter a valid integer.")
