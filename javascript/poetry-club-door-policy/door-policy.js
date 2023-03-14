// @ts-check

/**
 * Respond with the correct character, given the line
 * of the poem, if this were said at the front door.
 *
 * @param {string} line
 * @returns {string}
 */
export function frontDoorResponse(line) {
  // Return the first character of the line
  return line[0];
}

/**
 * Format the password for the front-door, given the response letters.
 *
 * @param {string} word the letters you responded with before
 * @returns {string} the front door password
 */
export function frontDoorPassword(word) {
  // Return the word with only the first letter capitalized
  return word[0].toUpperCase() + word.slice(1).toLowerCase();
}

/**
 * Respond with the correct character, given the line
 * of the poem, if this were said at the back door.
 *
 * @param {string} line
 * @returns {string}
 */
export function backDoorResponse(line) {
  // Return the last character of the line (excluding whitespace)
  return line.trim().slice(-1);
}

/**
 * Format the password for the back door, given the response letters.
 *
 * @param {string} word the letters you responded with before
 * @returns {string} the back door password
 */
export function backDoorPassword(word) {
  // Return the word with the first letter capitalized
  // and append the word "please" to the end
  return word[0].toUpperCase() + word.slice(1) + ", please";
}
