function solution(n) {
  return [...n.toString()].map((x) => parseInt(x, 10)).reverse()
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.05ms, 29.8MB)
// 테스트 2 〉	통과 (0.04ms, 29.7MB)
// 테스트 3 〉	통과 (0.04ms, 29.9MB)
// 테스트 4 〉	통과 (0.05ms, 30.1MB)
// 테스트 5 〉	통과 (0.05ms, 30MB)
// 테스트 6 〉	통과 (0.07ms, 29.9MB)
// 테스트 7 〉	통과 (0.07ms, 29.8MB)
// 테스트 8 〉	통과 (0.04ms, 29.8MB)
// 테스트 9 〉	통과 (0.12ms, 30.1MB)
// 테스트 10 〉	통과 (0.09ms, 29.9MB)
// 테스트 11 〉	통과 (0.04ms, 29.8MB)
// 테스트 12 〉	통과 (0.04ms, 30MB)
// 테스트 13 〉	통과 (0.06ms, 29.8MB)
