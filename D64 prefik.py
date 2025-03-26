class Solution:
    def productExceptSelf(self, arr):
        #code here
        product = 1
        res = []
        zero = 0
        for num in arr:
            
            if zero > 1:
                product = 0
                break
            if num == 0:
                zero +=1
                continue
                
            product *=num
        l = len(arr) 
        
        
        for x in range(0,l):
            if zero > 1:
                res.append(0)
                continue
            if zero ==1:    
                if arr[x]==0:
                    res.append(product)
                else:
                    res.append(0)
            
                continue
            res.append(int(product/arr[x]))
            
        
        return res
