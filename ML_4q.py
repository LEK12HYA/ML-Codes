input_string=input("Enter the String")
freq={}
def highest_count(input_string):
    for character in input_string:
        if character in freq:
           freq[character]+=1
        else:
            freq[character]=1
        occurence_of_character=None
        occurence_of_count=0
    for character in freq:
        if freq[character]>occurence_of_count:
            occurence_of_count=freq[character]
            occurence_of_character=character
    return occurence_of_count,occurence_of_character
occurence_of_count,occurence_of_character=highest_count(input_string)
print("occurence_of_character:",occurence_of_character)
print("occurence_of_count:",occurence_of_count)
