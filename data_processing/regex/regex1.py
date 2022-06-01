"""
https://programmingwithmosh.com/interviews/interview-questions-in-python-regular-expressions/
Q1

ref
https://docs.python.org/3/library/re.html

match vs search
https://www.geeksforgeeks.org/python-re-search-vs-re-match/


"""


def is_strong_password(string_):
    """

    :param string_:
    :return:
    """
    """
    A strong password is defined as follows:

        at least eight characters long
        contains one uppercase character
        contains one lowercase character
        has at least one digit
        has at least one special character
    """
    print('checking strong password')
    len_pattern = r".{8,}"
    if re.fullmatch(pattern=len_pattern, string=string_) is None:
        return False
    uppercase_pattern = r"[A-Z]"
    if re.search(pattern=uppercase_pattern, string=string_) is None:
        print('does not contain uppercase')
        return False
    uppercase_pattern = r"[a-z]"
    if re.search(pattern=uppercase_pattern, string=string_) is None:
        print('does not contain lowercase')
        return False
    digit_pattern = r"[0-9]"
    if re.search(pattern=digit_pattern, string=string_) is None:
        print('does not contain digit')
        return False
    special_pattern = r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]"
    if re.search(pattern=special_pattern,string=string_) is None:
        print('no special')
        return False
    return True


import re

if __name__ == '__main__':
    substring = r"hello"
    string1 = 'hally hello hello'
    string2 = 'hello hey hello'
    print('match')
    print(re.match(substring, string1, re.IGNORECASE))
    print(re.match(substring, string2, re.IGNORECASE))
    print('search')
    print(re.search(substring, string1, re.IGNORECASE))
    print(re.search(substring, string2, re.IGNORECASE))
    print('findall')
    print(re.findall(substring, string1, re.IGNORECASE))
    print(re.findall(substring, string2, re.IGNORECASE))

    # Q1 remove vowels
    vowels = r"[aiey]"
    string3 = "I am a happy man, yaay"
    res = re.sub(pattern=vowels, repl="", string=string3, flags=re.IGNORECASE)
    print(res)

    # Q2 valid phone number
    pattern1 = r"^\([0-9]{3,3}\)-[0-9]{3,3}-[0-9]{4,4}$"
    pattern2 = r"^[0-9]{3,3}-[0-9]{3,3}-[0-9]{4,4}$"
    pattern = re.compile(f"({pattern1})|({pattern2})")
    phone1 = "017-643-2175"  # OK
    phone2 = "(017)-643-2175"  # OK
    phone3 = "(0178)-643-2175"  # NO
    phone4 = "(017-643-2175"  # NO
    phone5 = "017-643-21759"  # NO
    assert re.match(pattern=pattern, string=phone1) is not None
    assert re.match(pattern=pattern, string=phone2) is not None
    assert re.match(pattern=pattern, string=phone3) is None
    assert re.match(pattern=pattern, string=phone4) is None
    assert re.match(pattern=pattern, string=phone5) is None

    # Q3
    assert not is_strong_password("abcdefghiABC")
    assert is_strong_password("123a4567@A")
    assert not is_strong_password("1234567a")
    assert is_strong_password("12c345@6A8")
    assert not is_strong_password("123456a8")
