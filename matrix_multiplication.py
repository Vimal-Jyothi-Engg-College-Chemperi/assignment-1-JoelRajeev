def multiply_matrices(mat1, mat2):
    """Multiplies two matrices and returns the result."""
    # Check if multiplication is mathematically possible
    if len(mat1[0]) != len(mat2):
        raise ValueError("Number of columns in first matrix must equal number of rows in second matrix.")

    # Create a result matrix with dimensions: len(mat1) x len(mat2[0])
    # filled with zeros.
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    # Perform matrix multiplication
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

if __name__ == "__main__":
    # Example usage
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    
    print("Matrix A:")
    for row in A:
        print(row)
        
    print("\nMatrix B:")
    for row in B:
        print(row)
        
    print("\nResult of A * B:")
    try:
        result = multiply_matrices(A, B)
        for row in result:
            print(row)
    except ValueError as e:
        print(f"Error: {e}")
