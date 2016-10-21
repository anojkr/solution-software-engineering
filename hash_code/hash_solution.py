LETTER = 'acdegilmnoprstuw' #Global variable

def indexOf(s):
    """
    @:param: s - character
    This function return index of character in LETTER"""
    for i in range(0, len(LETTER)-1):
        if s == LETTER[i]:
            return i

def reverse_a_string(a_string):
    """
    @:param : a_string - input string
    This function retuns reverse of string
    """
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1
        new_strings.append(a_string[index])
    return ''.join(new_strings)

def hash(string):
    """
    @:param: string - input string
    Given string function return corresponding hashcode
    """
    h=7
    for i in string:
        h = h*37 + indexOf(i)
    return h

def dehash(hashcode):
    """
    @:param: hashcode : given hashcode as input
    Given hashcode, function returns corresponding string"""
    result = ''
    while hashcode >7 :
        r = (hashcode % 37)
        if r < len(LETTER):
            result = result + LETTER[int(r)]
            hashcode = (hashcode - r)/37
        else :
            return "HashCode Invalid"
    if hashcode !=7:
        print 'HashCode Invalid'
    else:
        return reverse_a_string(result)

if __name__ == "__main__":
    print hash('leepadg')
    print dehash(930846109532517)