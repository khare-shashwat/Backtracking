def newFun(candidates,target,ds,ind,ans):
    if(target==0):
        ans.append(ds[:])
        return
    for i in range(ind,len(candidates)):
        if(i>ind and candidates[i]==candidates[i-1]):
            continue
        if(candidates[i]>target): 
            break
        ds.append(candidates[i])
        newFun(candidates,target-candidates[i],ds,i+1,ans)
        ds.pop()
    return ans

print(newFun([1,2,2,2,5],5,[],0,[]))
