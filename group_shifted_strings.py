'''
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if not strings:
            return []
        mapping = {}
        for string in strings:
            offset = ord(string[0]) - ord('a')
            key = ''
            for i in xrange(len(string)):
                c = chr(ord(string[i]) - offset)
                if c < 'a':
                    c = chr(ord(c) + 26)
                key += c
            if key not in mapping:
                mapping[key] = [string]
            else:
                mapping[key].append(string)
        results = []
        for key in mapping.keys():
            results.append(sorted(mapping[key]))
        return results

