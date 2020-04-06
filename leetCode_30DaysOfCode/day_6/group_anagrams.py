def groupAnagrams(strs):
    new_arr = []
    for i in range(len(strs)):
        k = list(strs[i])
        new_arr.append("".join(sorted(k)))

    out = []
    seen = {}
    for v1, v2 in zip(strs, new_arr):
        if v2 in seen:
            out[seen[v2]].append(v1)
        else:
            seen[v2] = len(out)
            out.append([v1])
    print(out)


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
