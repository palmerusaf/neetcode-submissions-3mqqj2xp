class Solution {
  /**
   * @param {string[]} strs
   * @returns {string}
   */
  encode(strs) {
    let result = "";
    for (let s of strs) {
      result += s.length + "#" + s;
    }
    return result;
  }

  /**
   * @param {string} str
   * @returns {string[]}
   */
  decode(str) {
    const result = [];
    const strA = str.split("");
    while (strA.length) {
      //get encoded number
      let encodedNumber = "";
      while (true) {
        let char = strA.shift();
        console.log(char)
        if (char == "#") break;
        encodedNumber += char;
      }
      encodedNumber = +encodedNumber;

      // get word
      let word = "";
      for (let i = 0; i < encodedNumber; i++) {
        word += strA.shift();
      }
      result.push(word)
    }
    return result;
  }

}
