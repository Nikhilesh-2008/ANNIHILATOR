class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        xxx=0
        for i in operations:
            if "++" in i:
                xxx+=1
            else:
                xxx-=1
        return xxx