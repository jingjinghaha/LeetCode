'''
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case.
'''
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count = 0
        while count < n:
            buf4 = [""] * 4
            tmp = read4(buf4)
            if tmp == 0:
                return count
            buf[count:count+tmp] = buf4
            count += tmp
            if tmp < 4:
                break
        return min(count, n)

'''
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.
'''
# use globla value to store results from read4() for futher read
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    bufprt = 0
    bufsize = 0
    buff = [""] * 4
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count = 0
        while count < n:
            if self.bufprt == 0:
                self.bufsize = read4(self.buff)
            if self.bufsize == 0:
                break
            while count < n and self.bufprt < self.bufsize:
                buf[count] = self.buff[self.bufprt]
                count += 1
                self.bufprt += 1
            if self.bufprt == self.bufsize:
                self.bufprt = 0
        return count
