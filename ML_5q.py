import random
list_of_numbers=[]
for i in range(25):
    x=random.randint(1,10)
    list_of_numbers.append(x)
def find_mean(list_of_numbers):
    mean=sum(list_of_numbers)/len(list_of_numbers)
    return mean
def find_median(list_of_numbers):
    m=sorted(list_of_numbers)
    middle_index=len(m)//2
    return m[middle_index]
def find_mode(list_of_numbers):
    freq={}
    for num in list_of_numbers:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    max_count=0
    mode=None
    for num in freq:
        if freq[num]>max_count:
            max_count=freq[num]
            mode=num
    return mode
print('Numbers:',list_of_numbers)
print('Mean:',find_mean(list_of_numbers))
print('Median:',find_median(list_of_numbers))
print('Mode:',find_mode(list_of_numbers))
