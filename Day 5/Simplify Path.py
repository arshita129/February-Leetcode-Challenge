class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s=[]
        path=path.split('/')
        print(path)
        for p in path:
            print(p)
            if not p:
                continue
            if p=="..":
                if len(s)!=0:
                    s.pop()
            elif p==".":
                continue
            else:
                s.append(p)
        ans=""
        print(s)
        # for i in s:
        #     if i=="":
        #         continue
        #     ans+="/"+i
        return "/"+"/".join(s)
        
