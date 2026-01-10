def count_pair(no_in_list,sum_target):
    count=0
    for i in range(0,len(no_in_list)):                  #Taking the first element within the range of list except the element itself.
        for j in range(i+1,len(no_in_list)):            #Comparing the first element with the next element in the given range without itself which avoids duplicate or reverse pairs.
           if no_in_list[i]+no_in_list[j]==sum_target:  #Add the elements and if it is equal to the given sum target then it is a valid pair
               count+=1                                 # Increment the count pair whenever a sum pair is found
    return count
no_in_list=[2,7,4,1,3,6]
sum_target=10
cnt=count_pair([2,7,4,1,3,6],10)                       #Function call
print('Number of count pairs:',cnt)
