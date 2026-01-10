def matrix_multiply(M1,M2):
    result_matrix=[]              #For the final result matrix
    for i in range (len(M1)):       #For looping over the rows of M1
        row_matrix=[]                   #For storing one row value at a time
        for j in range (len(M2[0])):       #For looping over columns of M2
            total_sum=0                     #It stores the value of one cell in the result matrix
            for k in range(len(M2)):        
                total_sum+=M1[i][k]*M2[k][j]     #Performs matrix multiplication 
            row_matrix.append(total_sum)
            result_matrix.append(row_matrix)
    return result_matrix

def matrix_power(A,m):                  
    if m==1:
        return A
    result=A
    for i in range(m-1):      
        result=matrix_multiply(result,A)
    return result
A=[
    [2,3],
    [3,4]
  ]
m=int(input('Enter the value of m:'))
result_matrix=matrix_power(A,m)
print('Result Matrix:',result_matrix)
