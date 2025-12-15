def find_permutations(s):
    return find_permutations_aux(list(s))
def find_permutations_aux(s):
    if len(s) == 1:
        res = [s]
    else:
        res = []
        res_tmp = find_permutations_aux(s[1:])
        for sub_s in res_tmp:
            u = [s[0]]
            u.extend(sub_s)
            res.append(u)

        for i in range(1,len(s)):
            # swap
            tmp = s[0]
            s[0]=s[i]
            s[i] = tmp
            # recurse
            res_tmp= find_permutations_aux(s[1:])

            for sub_s in res_tmp:
                u = [s[0]]
                u.extend(sub_s)
                res.append(u)
            # swap back
            tmp = s[0]
            s[0] = s[i]
            s[i] = tmp

    return res


if __name__ == '__main__':
    s = "ABC"
    r = find_permutations(s)
    print(r)