/*** 2021년 3월 25일의 풀이 */
function solution(answers) {
  const Children = {
    A: [1, 2, 3, 4, 5],
    B: [2, 1, 2, 3, 2, 4, 2, 5],
    C: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  };

  const returnScore = (arr) => {
    var i = 0;
    var j = 0;
    var score = 0;
    while (i < answers.length) {
      if (answers[i] == arr[j]) {
        score++;
      }
      i++;
      j++;
      if (j === arr.length) {
        j = 0;
      }
    }
    return score;
  };

  let score = [];

  score.push(returnScore(Children.A));
  score.push(returnScore(Children.B));
  score.push(returnScore(Children.C));

  let result = [];

  for (var i = 0; i < score.length; i++) {
    if (Math.max(...score) == score[i]) {
      result.push(i + 1);
    }
  }
  return result;
}
/*
통과 (0.16ms, 29.9MB)
테스트 2 〉	통과 (0.23ms, 30.2MB)
테스트 3 〉	통과 (0.15ms, 30.1MB)
테스트 4 〉	통과 (0.13ms, 30.1MB)
테스트 5 〉	통과 (0.17ms, 29.9MB)
테스트 6 〉	통과 (0.17ms, 30.1MB)
테스트 7 〉	통과 (16.92ms, 32.5MB)
테스트 8 〉	통과 (0.61ms, 29.9MB)
테스트 9 〉	통과 (4.81ms, 32.8MB)
테스트 10 〉	통과 (4.70ms, 33MB)
테스트 11 〉	통과 (4.73ms, 32.3MB)
테스트 12 〉	통과 (4.90ms, 32.9MB)
테스트 13 〉	통과 (0.35ms, 29.9MB)
테스트 14 〉	통과 (4.77ms, 32.9MB)
*/

// 2021년 10월 29일, 개선된 풀이(반복문을 1번만에 끝내면서 2배 빨리진 성능)
function solution(answers) {
  const a = [1, 2, 3, 4, 5];
  const b = [2, 1, 2, 3, 2, 4, 2, 5];
  const c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let score = [0, 0, 0];
  let aIdx = 0;
  let bIdx = 0;
  let cIdx = 0;
  answers.forEach((v, i) => {
    if (v === a[aIdx++]) score[0]++;
    if (v === b[bIdx++]) score[1]++;
    if (v === c[cIdx++]) score[2]++;

    if (aIdx === 5) aIdx = 0;
    if (bIdx === 8) bIdx = 0;
    if (cIdx === 10) cIdx = 0;
  });

  const max = Math.max(...score);
  const result = [];
  for (let i = 0; i < 3; i++) {
    if (score[i] === max) result.push(i + 1);
  }

  return result;
}
/*
테스트 1 〉	통과 (0.12ms, 30.2MB)
테스트 2 〉	통과 (0.13ms, 30.3MB)
테스트 3 〉	통과 (0.10ms, 30.5MB)
테스트 4 〉	통과 (0.12ms, 30.4MB)
테스트 5 〉	통과 (0.11ms, 30.3MB)
테스트 6 〉	통과 (0.15ms, 30.3MB)
테스트 7 〉	통과 (1.84ms, 33.3MB)
테스트 8 〉	통과 (0.42ms, 30.3MB)
테스트 9 〉	통과 (2.53ms, 33.1MB)
테스트 10 〉	통과 (1.61ms, 32.9MB)
테스트 11 〉	통과 (2.55ms, 33.2MB)
테스트 12 〉	통과 (2.47ms, 32.8MB)
테스트 13 〉	통과 (0.23ms, 30.4MB)
테스트 14 〉	통과 (2.67ms, 33MB)
*/
