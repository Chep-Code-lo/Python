def prefix_sum(n):
    if n <= 0:
        return 0
    full_groups = n // 3
    rem = n % 3
    total = 6 * full_groups + 9 * full_groups * (full_groups - 1) // 2
    if rem == 0:
        return total
    a = 1 + 3 * full_groups
    if full_groups % 2 == 0:
        if rem == 1 :
            total += a
        else:
            total += 2 * a + 1
    else:
        if rem == 1:
            total += a + 2
        else:
            total += 2 * a + 3
    return total
l , r = map (int , input(). split())
print(prefix_sum(r) - prefix_sum(l - 1))

