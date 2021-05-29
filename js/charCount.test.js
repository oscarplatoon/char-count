// Can you translate this driver code to unit tests?
const { expect } = require("@jest/globals");
const charCount = require("./charCount");
test('will return object that coungting letters', () => {
  expect(charCount("aaabbc")['a']).toBe(3);
  expect(charCount("aaabbc")['b']).toBe(2);
  expect(charCount("aaabbc")['c']).toBe(1);
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['a']).toBe(6)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['e']).toBe(4)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['l']).toBe(3)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['p']).toBe(3)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['w']).toBe(2)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['d']).toBe(2)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['o']).toBe(2)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['t']).toBe(2)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['y']).toBe(2)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['k']).toBe(1)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['h']).toBe(1)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['i']).toBe(1)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['c']).toBe(1)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['n']).toBe(1)
  expect(charCount('rplyoacadawpettlleaodeeywapkniha')['r']).toBe(1)


})
// console.log(char.charCount("aaabbc")['a'] === 3)
// console.log(char.charCount("aaabbc")['b'] === 2)
// console.log(char.charCount("aaabbc")['c'] === 1)

// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['a'] === 6)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['e'] === 4)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['l'] === 3)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['p'] === 3)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['w'] === 2)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['d'] === 2)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['o'] === 2)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['t'] === 2)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['y'] === 2)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['k'] === 1)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['h'] === 1)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['i'] === 1)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['c'] === 1)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['n'] === 1)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['r'] === 1)
