from collections import defaultdict
class Solution(object):

    
    def groupAnagrams(self, strs):
        group=defaultdict(list) # hashmap for storing

        for i in strs:
            key = "".join(sorted(i)) # dorted word i is join or made back into a string from list
            group[key].append(i) # group[keu] checks key in group and appends current word into the list

        return list(group.values())

        
             