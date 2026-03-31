class Solution {
  /**  @typedef {{start:number,end:number}} Interval */
  /** @param {Interval[]} intervals @returns {number} */
  minMeetingRooms(intervals) {
    const starts = intervals.map(({ start }) => start).sort((a, b) => a - b);
    const ends = intervals.map(({ end }) => end).sort((a, b) => a - b);
    let [count, res, s, e] = Array(4).fill(0);
    while (s < intervals.length) {
      if (starts[s] < ends[e]) {
        count++;
        s++;
      } else {
        count--;
        e++;
      }
      res = Math.max(res, count);
    }
    return res;
  }
}

