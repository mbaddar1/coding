def merge_the_tools(s, k):
    n = len(s)
    assert n % k == 0, " k must factor of n"
    substr_list = []
    for i in range(0, n, k):
        chr_set = set()
        substr = ''
        for j in range(i, i + k):
            if s[j] not in chr_set:
                chr_set.add(s[j])
                substr += s[j]
        del chr_set
        substr_list.append(substr)
    for substr in substr_list:
        print(substr)


if __name__ == '__main__':
    s = "AABCAAADA"
    merge_the_tools(s, 3)

