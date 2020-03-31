def countPalindromes(s):
    # Write your code here
    tot_pal = len(s)
    for i in range(len(s)):
        l_p = i - 1
        r_p = i + 1
        ind = True
        while l_p >= 0 and r_p < len(s) and ind:
            ind = False
            if s[l_p: r_p+1] == s[l_p: r_p+1][::-1]:
                tot_pal += 1
                ind = True
            if s[l_p: i+1] == s[l_p: i+1][::-1]:
                tot_pal += 1
                ind = True
            if s[i: r_p+1] == s[i: r_p+1][::-1]:
                tot_pal += 1
                ind = True
            l_p -= 1
            r_p += 1
    return tot_pal


print(countPalindromes("aaa"))