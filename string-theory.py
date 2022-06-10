import re

from bleach import clean


def is_palindrome(text):
    """
    >>> is_palindrome('Mr. Owl ate my metal worm')
    True
    >>> is_palindrome('Eva, can I see bees in a cave?')
    True
    """
    sec_text = re.sub(r'[^\w\s]', '', text)
    print(sec_text)
    sec_text = ''.join(sec_text.split()).lower()
    print(sec_text)
    print(sec_text[::-1])
 
    if (sec_text == sec_text[::-1]):
        return True
    else:
        return False

# print(is_palindrome('Eva, can I see bees in a cave?'))

def is_isogram(text):
    """
    >>> is_isogram('uncopyrightables')
    True
    """
    base_text = text.lower()
    check_list = []
    for letter in base_text:
        if letter in check_list:
            return False
        check_list.append(letter)
    return True
    
    

# print(is_isogram('texx'))

def is_pangram(text):
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    clean_text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxzy'
    for item in alphabet:
        if item not in clean_text:
            return False
    return True
    pass


def is_anagram(text1, text2):
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    clean_text_1 = re.sub(r'[^\w\s]', '', text1).lower()
    clean_text_2 = re.sub(r'[^\w\s]', '', text2).lower()
    if (clean_text_1 == clean_text_2[::-1]):
        return True
    else:
        return False
    pass


def is_blanagram(text1, text2):
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
    text1 = re.sub(r'[^\w\s]', '', text1).lower()
    text1 = ''.join(text1.split())
    sorted_characters1 = sorted(text1)
    print(sorted_characters1)
    text2 = re.sub(r'[^\w\s]', '', text2).lower()
    text2 = ''.join(text2.split())
    sorted_characters2 = sorted(text2)
    print(sorted_characters2) 
    if (sorted_characters1 == sorted_characters2) and len(sorted_characters1)-len(sorted_characters2) == 1:
        return True
    else: 
        return False

    pass
print(is_blanagram('abc', "abcsd"))