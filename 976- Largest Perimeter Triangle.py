
class Solution():
    def largestPerimeter(self, A):
        A.sort(reverse=True)
        print(A)  

        for i in range(len(A) - 2):
            print(i)  
            if A[i+1] + A[i+2] > A[i]:
                print(A[i+1] , A[i+2] , A[i])
                return A[i] + A[i+1] + A[i+2]  
        return 0


if __name__ == '__main__':
    solu = Solution()
    print(solu.largestPerimeter([]))
    
    


