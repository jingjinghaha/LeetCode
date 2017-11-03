'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''
class Solution(object):
    mapping = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
    mapping_add = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        cnt = 0
        ans = ""
        while num > 0:
            last_3 = num % 1000
            s = self.parse(last_3)
            if s:
                if cnt == 1:
                    s = s + ' Thousand'
                elif cnt == 2:
                    s = s + ' Million'
                elif cnt == 3:
                    s = s + ' Billion'
                if ans:
                    ans = s + ' ' + ans
                else:
                    ans = s
            num /= 1000
            cnt += 1
        return ans
    
    def parse(self, num):
        ans = ""
        if num == 0:
            return ans
        if num >= 100:
            head = num / 100
            ans = self.mapping[head] + ' Hundred'
        last_2 = num % 100
        if last_2 == 0:
            return ans
        if last_2 < 20:
            if ans:
                ans = ans + ' ' + self.mapping[last_2]
            else:
                ans = self.mapping[last_2]
            return ans
        unit = last_2 % 10
        tens = last_2 / 10
        if ans:
            ans = ans + ' ' + self.mapping_add[tens]
        else:
            ans = self.mapping_add[tens]
        if unit:
            ans = ans + ' ' + self.mapping[unit]
        return ans

# add memorization
class Solution(object):
    mapping = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
    mapping_add = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
    hashmap = {}
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        orig_num = num
        if orig_num in self.hashmap:
            return self.hashmap[orig_num]
        if num == 0:
            return 'Zero'
        cnt = 0
        ans = ""
        while num > 0:
            last_3 = num % 1000
            s = self.parse(last_3)
            if s:
                if cnt == 1:
                    s = s + ' Thousand'
                elif cnt == 2:
                    s = s + ' Million'
                elif cnt == 3:
                    s = s + ' Billion'
                if ans:
                    ans = s + ' ' + ans
                else:
                    ans = s
            num /= 1000
            cnt += 1
        self.hashmap[orig_num] = ans
        return ans
    
    def parse(self, num):
        if num in self.hashmap:
            return self.hashmap[num]
        ans = ""
        if num == 0:
            return ans
        if num >= 100:
            head = num / 100
            ans = self.mapping[head] + ' Hundred'
        last_2 = num % 100
        if last_2 == 0:
            return ans
        if last_2 < 20:
            if ans:
                ans = ans + ' ' + self.mapping[last_2]
            else:
                ans = self.mapping[last_2]
            return ans
        unit = last_2 % 10
        tens = last_2 / 10
        if ans:
            ans = ans + ' ' + self.mapping_add[tens]
        else:
            ans = self.mapping_add[tens]
        if unit:
            ans = ans + ' ' + self.mapping[unit]
        self.hashmap[num] = ans
        return ans
        
# more briefly
class Solution(object):
    mapping = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
    tens = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
    thousands = {1:'Thousand', 2: 'Million', 3: 'Billion'}
    hashmap = {}
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        orig_num = num
        if orig_num in self.hashmap:
            return self.hashmap[orig_num]
        if num == 0:
            return 'Zero'
        cnt = 0
        ans = ""
        while num > 0:
            last_3 = num % 1000
            if last_3:
                s = self.parse(last_3)
                if cnt in self.thousands:
                    s = s + ' ' + self.thousands[cnt]
                if ans:
                    ans = s + ' ' + ans
                else:
                    ans = s
            num /= 1000
            cnt += 1
        self.hashmap[orig_num] = ans
        return ans
    
    def parse(self, num):
        if num in self.hashmap:
            return self.hashmap[num]
        ans = ""
        if num == 0:
            return ""
        elif num < 20:
            ans =  self.mapping[num]
        elif num < 100:
            tmp = self.parse(num % 10)
            if tmp:
                ans = self.tens[num / 10] + ' ' + tmp
            else:
                ans = self.tens[num / 10]
        else:
            tmp = self.parse(num % 100)
            if tmp:
                ans = self.mapping[num / 100] + ' Hundred ' + tmp
            else:
                ans = self.mapping[num / 100] + ' Hundred'
        self.hashmap[num] = ans
        return ans
