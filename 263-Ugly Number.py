class Solution:
    def isUgly(self, n: int) -> bool:
        print(n)
        if n <= 0:
            return False
        
    
        
        for prim in [2,3,5]:
            print("prim = ",prim)
            
            while n % prim == 0:
                n = n // prim
                print("update n = " ,n)
                
        return n == 1
                
