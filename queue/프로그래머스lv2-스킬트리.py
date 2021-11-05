from collections import deque, defaultdict
def check_skill(key:str, target:str)->int:
    dic = defaultdict(int)
    for i, v in enumerate(key):
        dic[v] = i + 1
    visited = [True] + [False] * 26
    q = deque()
    for a in target:
        q.append(a)
    
    while q:
        x = q.popleft()
        if dic[x]:
            if visited[dic[x] - 1]:
                visited[dic[x]] = True
            else:
                return 0
    if not q:
        return 1


def solution(skill, skill_trees):
    result = 0
    for skill_tree in skill_trees:
        result += check_skill(skill, skill_tree)
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.05ms, 10.3MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
"""