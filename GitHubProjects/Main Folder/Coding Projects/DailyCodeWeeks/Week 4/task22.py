def wordBreak(word):
    
    global dictionary
 
    size = len(word)
 
    if(size == 0):
        return True

    for i in range(1, size + 1):
        if (word[0: i] in dictionary and wordBreak(word[i: size])):
            return True

    return False

if __name__ == "__main__" :

    dictionary = set()   
    temp_dictionary = [ "sonic", "heroes", "is", "the", "best", "game", "ever", "made"]

    for temp in temp_dictionary:
        dictionary.add(temp)

    print("Yes" if wordBreak("sonic") else "No")
    print("Yes" if wordBreak("sanic") else "No")
    print("Yes" if wordBreak("") else "No")
    print("Yes" if wordBreak("sooooonic") else "No")
    print("Yes" if wordBreak("sonicheroesis") else "No")
    print("Yes" if wordBreak("sonicheroesismyjam") else "No")