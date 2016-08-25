def alphabet_position(letter):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for l in alphabet:
        if l == letter.lower():
            return alphabet.index(l)
    return "error. input should be a single letter"

def get_letter_by_position(pos):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    return alphabet[pos]
    
def rotate_character(ch, rot):
    if ch.isalpha() == True:
        initPosition = alphabet_position(ch)
        newPosition = (initPosition + int(rot))%26
        newCh = get_letter_by_position(newPosition)
        if ch.isupper() == True:
            return newCh.upper()
        return newCh
    else:
        return ch