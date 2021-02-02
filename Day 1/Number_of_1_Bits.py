def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # print(n)
        # print(Counter(bin(n).replace('0b','')))
        return Counter(bin(n).replace('0b',''))['1']
