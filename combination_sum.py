def combinationSum(candidates, target,ds=[],i=0,ans=[]):
        if(target==0):
            ans.append(ds[:])
            return
        if(i==len(candidates)):
            return
        if(candidates[i]<=target):
            ds.append(candidates[i])
            combinationSum(candidates,target-candidates[i],ds,i,ans)
            ds.pop()
        combinationSum(candidates,target,ds,i+1,ans)
        return ans

print(combinationSum([2,3,6,7],7))
