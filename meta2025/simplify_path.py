"""
https://leetcode.com/problems/simplify-path/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
Assumptions
1.
"""


def simplify_slashes(i: int, path: str):
    j = i
    while j < len(path):
        if path[j] == '/':
            j = j + 1
        else:
            break
    return j


def simplify_path(path: str):
    n = len(path)
    assert path[0] == '/'
    out_path = [''] * n
    out_path[0] = '/'
    j = 1
    i = 1
    if n == 1:
        return "".join(out_path[:j])
    while i < n:
        if path[i] == '/':
            k = simplify_slashes(i, path)
            i = k
            out_path[j] = '/'
            j = j + 1
            continue
        elif path[i] == '.':
            if path[i-1]=='/' and i + 1 <= n - 1 and path[i + 1] == '/':
                k = simplify_slashes(i + 1, path)
                i = k
                continue
            elif path[i-1]=='/' and i + 2 <= n - 1 and path[i + 1] == '.' and path[i + 2] == '/':
                if path[i + 2] == '/':
                    k = simplify_slashes(i + 2, path)
                    i = k
                    u = j
                    slash_count = 0
                    while u > 0 and slash_count < 2:
                        if out_path[u] == '/':
                            slash_count += 1

                        u = u - 1
                    j = u + 2 if slash_count==2 else u+1
                    continue
        out_path[j] = path[i]
        j = j + 1
        i = i + 1

    return "".join(out_path[:j])


if __name__ == '__main__':
    #path = "/ab/cd/..///"  # expected output /
    #path = "/ab//..//cd/" # /cd/
    # path = "/home//foo/"
    # path = "/home/user/Documents/../Picture"
    # path = "/../"
    path = "/.../a/../b/c/../d/./" # FIXME
    simp = simplify_path(path)
    print(simp)
