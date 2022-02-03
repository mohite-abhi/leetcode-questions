from collections import Counter

def partitionLabels(s):
    # original appraoch
    partitions = dict()
    for i in range(len(s)):
        if not partitions.get(s[i]):
            partitions[s[i]] = [i,i]
        else:
            partitions[s[i]][1] = i
    return resolvePartitions(partitions)
    
def resolvePartitions(partitions):
    finalPartition = [[0, 0]]
    i = 0
    for left, right in partitions.values():                
        if finalPartition[i][0] < left < finalPartition[i][1]:
            finalPartition[i][1] = max(right, finalPartition[i][1])
        else:
            finalPartition.append([left, right])
            i += 1
            
    return [i[1]-i[0]+1 for i in finalPartition[1:]]
        