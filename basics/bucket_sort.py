def bucket_sort(arr, bucket_size):
    x_min = min(arr)
    x_max = max(arr)
    num_buckets = ((x_max-x_min)//bucket_size)+1
    buckets = [[] for _ in range(num_buckets)]
    # scatter phase https://en.wikipedia.org/wiki/Bucket_sort
    n = len(arr)
    for i in range(n):
        idx = int(arr[i] / bucket_size)
        buckets[idx].append(arr[i])
    sorted_arr = []
    for bucket in buckets:
        if len(bucket) > 0:
            sorted_bucket= sorted(bucket)
            sorted_arr.extend(sorted_bucket)
    return sorted_arr


def assert_sorted(a):
    for i in range(1, len(a)):
        assert a[i - 1] <= a[i]


if __name__ == "__main__":
    a = [29, 25, 3, 49, 9, 37, 21, 43]
    bucket_size = 10
    b = bucket_sort(a, bucket_size=10)
    assert_sorted(b)
    pass
