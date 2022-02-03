def restoreString(s, indices):
    for i in range(len(indices)):
        if type(indices[i]) != int:
            continue
        curr = root = indices[i]
        index = i
        while indices[i] == root:
            next_ = indices[curr]
            indices[curr] = s[index]
            index = curr
            curr = next_

    return indices


restoreString("codeleet", [4,5,6,7,0,2,1,3])