def is_vowel(c):
    list_ = ['a', 'e', 'i', 'o', 'u']
    return c in list_


def get_char_idx(s):
    chr_idx = {}
    for i, c in enumerate(s):
        if c in chr_idx.keys():
            chr_idx[c].append(i)
        else:
            chr_idx[c] = [i]
    return chr_idx


# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def fn1(s):
    s = s.lower()
    vowel_counter = 0
    non_vowel_counter = 0
    n = len(s)
    for i,c in enumerate(s):
        if is_vowel(c):
            vowel_counter+=n-i
        else:
            non_vowel_counter+=n-i
    if vowel_counter>non_vowel_counter:
        r = f"KEVEN {vowel_counter}"
    elif non_vowel_counter > vowel_counter:
        r = f"STUART {non_vowel_counter}"
    else:
        r = "Draw"
    return r




if __name__ == '__main__':
    s = "BAANANAS"
    r = fn1(s)
    print(r)
