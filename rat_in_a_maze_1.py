class Solution:
    def findPath(self, m, n):
        ans=[]
        if(m[0][0]==0):
            return []
        self.myFun(m,n,0,0,["0-0"],"",ans)
        return ans
    def myFun(self,m,n,i,j,visited,ds="",ans=[]):
        if(i==(n-1) and j==(n-1)):
            ans.append(ds[:])
            return
        for opt in ["U","D","R","L"]:
            if(self.isValid(opt,m,visited,i,j,n)):
                if(opt=="U"):
                    i=i-1
                elif(opt=="D"):
                    i=i+1
                elif(opt=="R"):
                    j=j+1
                else:
                    j=j-1
                ds=ds+opt
                visited.append(str(i)+"-"+str(j))
                self.myFun(m,n,i,j,visited,ds,ans)
                ds=ds[:-1]
                visited.pop()
                if(opt=="U"):
                    i=i+1
                elif(opt=="D"):
                    i=i-1
                elif(opt=="R"):
                    j=j-1
                else:
                    j=j+1
        return ans
    
    def isValid(self,opt,m,visited,i,j,n):
        if(opt=="U"):
            if(i>0 and (str(i-1)+"-"+str(j) not in visited) and m[i-1][j]==1):
                return True
        elif(opt=="D"):
            if(i<(n-1) and (str(i+1)+"-"+str(j) not in visited) and m[i+1][j]==1):
                return True
        elif(opt=="R"):
            if(j<(n-1) and (str(i)+"-"+str(j+1) not in visited) and m[i][j+1]==1):
                return True
        elif(opt=="L"):
            if(j>0 and (str(i)+"-"+str(j-1) not in visited) and m[i][j-1]==1):
                return True
        
        return False
        
s=Solution()
print(s.findPath([[1,1],[1,1]],2))
