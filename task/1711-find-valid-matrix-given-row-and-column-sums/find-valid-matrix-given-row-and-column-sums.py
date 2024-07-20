class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        col=len(colSum)
        row=len(rowSum)
        mat=[[0 for i in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                rsum ,csum=rowSum[i],colSum[j]
                minn=min(rsum,csum)
                mat[i][j]=minn
                rowSum[i]-=minn
                colSum[j]-=minn
        return mat