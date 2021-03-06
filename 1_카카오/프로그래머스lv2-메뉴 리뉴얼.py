# 옛날 풀이... 나 뭐했니? // 2달만에 다시 봤는데 내가 짰던 코드인데도 이해가 1도 안된다...ㅋ
import itertools
from collections import defaultdict
def solution(orders, course):
    orders = sorted(orders, key = lambda x : len(x))
    # 경우의 수
    c = defaultdict(int)
    for order in orders:
        order = sorted(order)
        l = len(order)
        for i in range(2, l+1):
            temp = ""
            nCr = list(itertools.combinations(order, i))
            for t in nCr:
                r = "".join(t)
                c[r] += 1
    #print(c)
    numbers = []
    for i in course:
        _max = 0
        for k in c.keys():
            l = len(k)
            if i == l and _max <= c[k]:
                _max = c[k]
        numbers.append(_max)
    
    result = []
    for i in range(len(course)):
        number = numbers[i]
        _course = course[i]
        for k in c.keys():
            if c[k] == number and len(k) == _course and c[k] != 1:
                result.append(k)
                
    result = sorted(result)
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.14ms, 10.3MB)
테스트 2 〉	통과 (0.09ms, 10.2MB)
테스트 3 〉	통과 (0.12ms, 10.3MB)
테스트 4 〉	통과 (0.12ms, 10.4MB)
테스트 5 〉	통과 (0.10ms, 10.3MB)
테스트 6 〉	통과 (0.27ms, 10.3MB)
테스트 7 〉	통과 (0.50ms, 10.3MB)
테스트 8 〉	통과 (3.80ms, 10.5MB)
테스트 9 〉	통과 (3.12ms, 10.5MB)
테스트 10 〉	통과 (4.87ms, 10.9MB)
테스트 11 〉	통과 (3.12ms, 10.6MB)
테스트 12 〉	통과 (2.85ms, 10.7MB)
테스트 13 〉	통과 (6.94ms, 10.9MB)
테스트 14 〉	통과 (8.34ms, 10.9MB)
테스트 15 〉	통과 (6.46ms, 11MB)
테스트 16 〉	통과 (3.44ms, 10.6MB)
테스트 17 〉	통과 (7.05ms, 10.9MB)
테스트 18 〉	통과 (8.07ms, 11MB)
테스트 19 〉	통과 (4.55ms, 10.6MB)
테스트 20 〉	통과 (8.64ms, 10.6MB)
"""

# 220107 의 풀이 .. 개선 성공, 실력상승 성공!
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    # 전체 딕셔너리
    dic = defaultdict(dict)
    for i in course:
        dic[i] = defaultdict(int)
        for order in orders:
            nCr = list(combinations(sorted(order), i))
            for tup in nCr:
                key = "".join(tup)
                dic[i][key] += 1
                
    result = []
    for i in course:
        # 원소가 없거나 1개만 있다면 pass
        if len(dic[i]) < 2:
            continue
        # 가장 많은 빈도
        _max = max(dic[i].values())
        for key, value in dic[i].items():
            # 빈도가 1이 아니면서 가장 많은 빈도가 나온 key(메뉴조합)가 결과가 됨
            if _max != 1 and value == _max:
                result.append(key)
    return sorted(result)

"""
정확성  테스트
테스트 1 〉	통과 (0.13ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (0.09ms, 10.3MB)
테스트 5 〉	통과 (0.09ms, 10.2MB)
테스트 6 〉	통과 (0.20ms, 10.3MB)
테스트 7 〉	통과 (0.21ms, 10.3MB)
테스트 8 〉	통과 (1.79ms, 10.5MB)
테스트 9 〉	통과 (1.40ms, 10.4MB)
테스트 10 〉	통과 (1.82ms, 10.6MB)
테스트 11 〉	통과 (0.98ms, 10.5MB)
테스트 12 〉	통과 (1.22ms, 10.5MB)
테스트 13 〉	통과 (1.58ms, 10.6MB)
테스트 14 〉	통과 (2.04ms, 10.5MB)
테스트 15 〉	통과 (1.61ms, 10.6MB)
테스트 16 〉	통과 (0.37ms, 10.3MB)
테스트 17 〉	통과 (0.25ms, 10.3MB)
테스트 18 〉	통과 (0.11ms, 10.2MB)
테스트 19 〉	통과 (0.04ms, 10.3MB)
테스트 20 〉	통과 (0.26ms, 10.3MB)
"""