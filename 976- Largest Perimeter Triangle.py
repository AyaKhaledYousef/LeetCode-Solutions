
class Solution():
    def largestPerimeter(self, A):
        A.sort(reverse=True)
        
        for i in range(len(A) - 2):
            if A[i+1] + A[i+2] > A[i]:
                return A[i] + A[i+1] + A[i+2]  
        return 0


if __name__ == '__main__':
    solu = Solution()
    print(solu.largestPerimeter([3,2,3,6]))
    
    


