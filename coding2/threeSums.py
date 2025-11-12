from typing import List


def threeSum(arr: List[int]):
    # create hash of indices
    # time O(N)
    # mem O(N)
    N = len(arr)
    indices = {}
    for i in range(N):
        if arr[i] in indices.keys():
            indices[arr[i]].append(i)
        else:
            indices[arr[i]] = [i]
    unique_values = list(indices.keys())
    N = len(unique_values)
    results = set()
    for i in range(N):
        for j in range(N):
            v = unique_values[i] + unique_values[j]
            if -v in indices.keys():
                for i1 in indices[unique_values[i]]:
                    for j1 in indices[unique_values[j]]:
                        if i1 != j1:
                            for k1 in indices[-v]:
                                if k1 != i1 and k1 != j1:
                                    result = tuple(sorted((arr[i1], arr[j1], arr[k1])))
                                    results.add(result)
    return list(results)
    # arr_sorted = sorted(arr)
    # i = 0
    # j = N - 1
    # results = []
    # while i < j:
    #     u = arr_sorted[i] + arr_sorted[j]
    #     if -u in indices.keys():
    #         neg_u_indices = indices[-u]
    #         indices_arr_i = indices[arr_sorted[i]]
    #         indices_arr_j = indices[arr_sorted[j]]
    #         for i1 in indices_arr_i:
    #             for j1 in indices_arr_j:
    #                 if i1 != j1:
    #                     for neg_u_index in neg_u_indices:
    #                         if neg_u_index != i1 and neg_u_index != j:
    #                             results.append((arr_sorted[i1], arr_sorted[j1], arr_sorted[neg_u_index]))
    #     else:


if __name__ == "__main__":
    r = threeSum(arr=[-1, 0, 1, 2, -1, -4])
    print(r)
    r = threeSum(arr=[0, 0, 0])
    print(r)
