def string_count ():
    string =  input("Enter your your text here: ").strip() #strip() för att ta bort mellanslag i början och slutet av stringen
    num_chars = 0
    num_words = 0
    for spaces in string: #for loop för att kolla antal mellanslag och räkna antal bokstäver
        if spaces == " ":
            num_words+=1
            removed_spaces = string.replace(" ", "")
            num_chars = len(removed_spaces)
        else:
            num_chars = len(string)


    if len(string) > 0:
        print (f"Number of words:  {num_words + 1}, number of characters:  {num_chars }") 
    else:
        print (f"Number of words:  {num_words}, number of characters:  {num_chars }") 


#problem om man sätter två mellanslag, hur löser man detta?




#string_count()


#Given a string s, find the length of the longest substring without repeating characters.

#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def find_longest_substring():
    input_string = input("Enter your string: ")
    output = 0

    print(input_string[0])
    #for substring in input_string:
        #leta efter längsta substringen som inte upprepar sig
        #antingen kolla varje index i stringen 
        #eller göra en variabel som blir tilldelad längsta strängen sen anväda len()
        #print(input_string.count(0,len(input_string)))



#find_longest_substring()


def bounce(i):
    start_value = i

    while True:
        if i > 0:
            i -= 1
            print(i)
            if i == 0:
                while i < start_value:
                    i += 1
                    print(i)
        if i == start_value:
            break


#bounce(20)






#Given an integer x, return true if x is a palindrome, and false otherwise.

#ta in integer x
# kör en reverse på x
#kolla om x och revers x är samma sak, annars false
def intPalindrome(i : int):
    intReverse = 0

    while i > 0:
        a = i % 10
        intReverse = intReverse * 10 + a
        i = i // 10

    if i == intReverse:
        print("Hej :D")
        return intReverse
    else:
        print("False")


intPalindrome(44)



def stringPalindrome(s :str):
    string_reversed = s[::-1].lower()


    if s == string_reversed:
        print(string_reversed)
    else:
        print("NEj :D")


    

stringPalindrome("otto")



def reverse(i : str):
    backwards = str(i[::-1])
    print(backwards)

reverse("21")