"""
https://www.interviewbit.com/problems/valid-email-address/
"""
import re


def print_match_object(match_):
    if match_ is None:
        print('None')
    else:
        for i in range(match_.lastindex + 1):
            print(match_.group(i))


if __name__ == '__main__':
    pattern = r"([a-zA-Z][a-zA-Z0-9-_+,.]*)@([a-zA-z][a-zA-Z0-9-_+,]*).([a-z]{3}|[a-z]{1,3}.[a-z]{1,3})"
    print('1')
    print_match_object(re.fullmatch(pattern=pattern, string="meme@here.com"))
    print('2')
    print_match_object(re.fullmatch(pattern=pattern, string="meme@here.co.uk"))
    print('3')
    print_match_object(re.fullmatch(pattern=pattern, string="meme@here.co.u.k"))
    print('4')
    print_match_object(re.fullmatch(pattern=pattern, string="1eme@here.co.uk"))
    print('5')
    print_match_object(re.fullmatch(pattern=pattern, string="meme$@here.co.uk"))
    print('6')
    print_match_object(re.fullmatch(pattern=pattern, string="meme@here.com.uk"))
    """
    For simplicity, assume that a vaild email addresses has the following rules-

        Email should be of the form local@domain.com
        There can only be alphanumberic characters in the local part email address.
        The following characters are valid in the local part of the email as long as they are not the first character.
        
          -, _, +, .
        
        Email address can not start with a number.
        Domain name can only contain alphanumeric characters and -.
        com part can have atmost one ., for e.g. co.uk or co.in is valid but as.df.gh is invalid
    """
    # There can only be alphanumberic characters in the local part email address.
