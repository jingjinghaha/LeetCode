'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''
class Codec:
    import random
    mapping_long_to_short = {}
    mapping_short_to_long = {}
    
    def generate_random_str(self):
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        s = ""
        for i in range(6):
            s += chars[random.randint(0, length)]
        return s
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.mapping_long_to_short:
            return "http://tinyurl.com/" + self.mapping_long_to_short[longUrl]
        short = self.generate_random_str()
        while short in self.mapping_short_to_long:
            short = self.generate_random_str()
        self.mapping_short_to_long[short] = longUrl
        self.mapping_long_to_short[longUrl] = short
        return "http://tinyurl.com/" + short
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        short = shortUrl.strip().split('/')[-1]
        return self.mapping_short_to_long[short]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

