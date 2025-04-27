class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dict={}
        value=[]
        for i in points:
            ans=0
            for j in i:
                ans+=j*j
            ans=ans**0.5
            value.append(ans)
            if ans in dict:
                dict[ans].append(i)
            else:
                dict[ans]=[i]
        sorted_values=sorted(dict.keys())
        value1=[]
        
        for i in range(len(sorted_values)):
            
            if len(dict[sorted_values[i]])>1:
                
                for j in range(len(dict[sorted_values[i]])):
                    
                    value1.append(dict[sorted_values[i]][j])
                    
            else:
                value1.append(dict[sorted_values[i]][0])
        return value1[0:k]      
