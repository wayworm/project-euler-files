#<p>If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are $3 + 3 + 5 + 4 + 4 = 19$ 
# letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used? </p>
#Do not count spaces or hyphens. 
# #For example, $342$ (three hundred and forty-two) contains 23
# #letters and $115$ (one hundred and fifteen) contains 20 letters. 
# #The use of "and" when writing out numbers is in compliance with British usage.</p>



#I did this
# Some issues I encountered:

#the len(string) would include the space character for "hundred and", so i made it "hundredand"
#I had to create lots of if statements, it doesn't feel like an elegant solution.
# I had to ensure that the word for the "Ones" column was removed when considering the "teen" numbers e.g. "fourteen"
# Currently num_2_letter does not output a list such that printing the elements in order would recover the name of the number.
# I think that would be a useful functionality. e.g input : 133 outputs : ['three', 'thirty', 'one', 'hundredand'] not ['one','hundredand','three]


def num_2_letters(num):
    words = []
    listed = []
    strnum = str(num)
    for i in strnum:
        listed.append(i)
    listed = list(reversed(listed))

    for i in range(0,len(listed)):
        listed[i] = int(listed[i])


    for i in range(0, len(listed)):
        if i == 0:
            if listed[i] == 1:
                words.append("one")
            if listed[i] == 2:
                words.append("two")
            if listed[i] == 3:
                words.append("three")
            if listed[i] == 4:
                words.append("four")
            if listed[i] == 5:
                words.append("five")
            if listed[i] == 6:
                words.append("six")
            if listed[i] == 7:
                words.append("seven")
            if listed[i] == 8:
                words.append("eight")
            if listed[i] == 9:
                words.append("nine")          
            
        #tens column
        elif i == 1:            
            if listed[i] == 2:
                words.append("twenty")
            if listed[i] == 3:
                words.append("thirty")
            if listed[i] == 4:
                words.append("forty")
            if listed[i] == 5:
                words.append("fifty")
            if listed[i] == 6:
                words.append("sixty")
            if listed[i] == 7:
                words.append("seventy")
            if listed[i] == 8:
                words.append("eighty")
            if listed[i] == 9:
                words.append("ninety") 
            
            if listed[i] == 1 and listed[i-1] == 0:
                words.append("ten")
            elif listed[i] == 1 and listed[i-1] == 1:
                words.append("eleven")
                words.remove("one")
            elif listed[i] == 1 and listed[i-1] == 2:
                words.append("twelve")
                words.remove("two")
            elif listed[i] == 1 and listed[i-1] == 3:
                words.append("thirteen")
                words.remove("three")
            elif listed[i] == 1 and listed[i-1] == 4:
                words.append("fourteen")
                words.remove("four")
            elif listed[i] == 1 and listed[i-1] == 5:
                words.append("fifteen")
                words.remove("five")
            elif listed[i] == 1 and listed[i-1] == 6:
                words.append("sixteen")
                words.remove("six")
            elif listed[i] == 1 and listed[i-1] == 7:
                words.append("seventeen")
                words.remove("seven")
            elif listed[i] == 1 and listed[i-1] == 8:
                words.append("eighteen")
                words.remove("eight")
            elif listed[i] == 1 and listed[i-1] == 9:
                words.append("nineteen")
                words.remove("nine")
        # #hundreds column
        elif i == 2 and listed[1] == 0 and listed[0] == 0:            
            if listed[i] == 1:
                words.append("one")
            if listed[i] == 2:
                words.append("two")
            if listed[i] == 3:
                words.append("three")
            if listed[i] == 4:
                words.append("four")
            if listed[i] == 5:
                words.append("five")
            if listed[i] == 6:
                words.append("six")
            if listed[i] == 7:
                words.append("seven")
            if listed[i] == 8:
                words.append("eight")
            if listed[i] == 9:
                words.append("nine")    

            words.append("hundred")


        else:
            if listed[i] == 1:
                words.append("one")
            if listed[i] == 2:
                words.append("two")
            if listed[i] == 3:
                words.append("three")
            if listed[i] == 4:
                words.append("four")
            if listed[i] == 5:
                words.append("five")
            if listed[i] == 6:
                words.append("six")
            if listed[i] == 7:
                words.append("seven")
            if listed[i] == 8:
                words.append("eight")
            if listed[i] == 9:
                words.append("nine")    
            words.append("hundredand")


    return words


def letter_counter(list_of_words):
    letters = 0
    for i in list_of_words:
        letters += len(i)

    return(letters)


total_letters = 0

for i in range(1,1000):
    total_letters += letter_counter(num_2_letters(i))

total_letters = total_letters + len("onethousand")

print(total_letters)
