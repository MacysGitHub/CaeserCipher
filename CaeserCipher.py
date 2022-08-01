import sys

def cipherceaser(text, ciphersequence):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    appended = []
    deciphered = []
    for i in text:
        appended.append(i)

    for i in appended:
        index = alphabet.index(i)
        print(index)

        if index > 0 & index < 26:
            if index + ciphersequence > 26:
                index -= 26
                index += ciphersequence
                deciphered.append(alphabet[index])
            else:
                deciphered.append(alphabet[index + ciphersequence])


    joined = "".join(deciphered)
    print(joined)


cipherceaser("ynkooejcpdanqxeykjrbdofgkq", -4)