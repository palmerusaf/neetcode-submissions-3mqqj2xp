class Solution {
  /**  @typedef {{start:number,end:number}} Interval */
  /** @param {Interval[]} intervals @returns {boolean} */
  canAttendMeetings(intervals) {
    if (intervals.length === 0) return true;
    intervals.sort((a, b) => a.start - b.start);
    let prevEnd = intervals[0].end;
    for (const { start, end } of intervals.slice(1)) {
      if (prevEnd > start) {
        return false;
      }
      prevEnd = end;
    }
    return true;
  }
}

