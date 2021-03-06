def solution(a, b):
    result = 0
    
    for x, y in zip(a, b):
        result += (x * y)
    
    return result
    

"""
정확성  테스트
테스트 1 〉	통과 (0.14ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.07ms, 10.1MB)
테스트 9 〉	통과 (0.11ms, 10.2MB)
"""

# 조금 더 스마트한 풀이
def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])

"""
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.08ms, 10.3MB)
테스트 7 〉	통과 (0.07ms, 10.2MB)
테스트 8 〉	통과 (0.14ms, 10.3MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
"""