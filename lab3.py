

def palindrom(text):

    #put the words from imput to word list

    word_list =[]
    temp = ''
    for character in text:
        if character.isalpha(): #checking is it every character is from alphabet
            temp += character #add to the temporary variable
        else:  #if it's not the character is alphabet, add our word to wordlist, and clear the temp variable
            word_list.append(temp)
            temp = ''

    #checking is the word is palinrom

    pal_words = []
    for i in word_list:
        reversed_word = i[::-1] #making words reversed
        if reversed_word == i: #checking is it read same as the original word,if yes add to pal_words
            pal_words.append(i)
    return pal_words


palindrom("abc addd ababa qwertyytrewq ada ")



