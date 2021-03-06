# 분할정복 // 56ms (10%)
class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def compute(left, right, op):
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l) + op + str(r)))
            return result
        
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        for index, value in enumerate(expression):
            if value in "-+*":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])
                
                #results += compute(left, right, value)
                results.extend(compute(left, right, value))
        
        return results