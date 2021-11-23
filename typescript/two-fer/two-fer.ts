/**
 * Given name, returns a string with the message "One for name, one for me."
 * If no name is provided, returns "One for you, one for me."
 */

export function twoFer(name: string = 'you'): string {
  return `One for ${name}, one for me.`;
}
