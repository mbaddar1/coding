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
def fn(s):
    n = len(s)
    substr_dict = dict()
    s = s.lower()
    c_idx = get_char_idx(s)
    vowel_count = 0
    non_vowel_count = 0
    for i, (k, v) in enumerate(c_idx.items()):
        if len(v) == 1:
            if is_vowel(k):
                vowel_count += n - v[0]
            else:
                non_vowel_count += n - v[0]
        else:

            for str_len in range(1,n-v[0]+1):
                start_idx = v[0]
                end_index = min(n,v[0]+str_len)
                substr = s[start_idx:end_index]
                if is_vowel(k):
                    vowel_count+=1
                else:
                    non_vowel_count+=1
                for start_idx2 in v[1:]:
                    end_index2 = min(n,start_idx2+str_len)
                    substr2 = s[start_idx2:end_index2]
                    if substr==substr2:
                        if is_vowel(k):
                            vowel_count+=1
                        else:
                            non_vowel_count+=1

    if non_vowel_count > vowel_count:
        return_str = f"STUART {non_vowel_count}"
    elif vowel_count > non_vowel_count:
        return_str = f"KEVIN {vowel_count}"
    else:
        return_str = "Draw"
    return return_str


if __name__ == '__main__':
    s = "BANANA"
    r = fn(s)
    print(r)
