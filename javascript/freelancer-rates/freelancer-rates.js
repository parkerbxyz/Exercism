// @ts-check

/**
 * The number of hours per day the freelancer works.
 */
const WORKING_HOURS_PER_DAY = 8;

/**
 * The number of billable days in each month.
 */
const BILLABLE_DAYS_PER_MONTH = 22;

/**
 * The day rate, given a rate per hour
 *
 * @param {number} ratePerHour
 * @returns {number} the rate per day
 */
export function dayRate(ratePerHour) {
  return ratePerHour * WORKING_HOURS_PER_DAY;
}

/**
 * Calculates the number of days in a budget, rounded down
 *
 * @param {number} budget: the total budget
 * @param {number} ratePerHour: the rate per hour
 * @returns {number} the number of days
 */
export function daysInBudget(budget, ratePerHour) {
  return Math.floor(budget / dayRate(ratePerHour));
}

/**
 * Calculates the discounted rate for large projects, rounded up
 *
 * @param {number} ratePerHour
 * @param {number} numDays: number of days the project spans
 * @param {number} discount: for example 20% written as 0.2
 * @returns {number} the rounded up discounted rate
 */
export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {
  const DISCOUNT_RATE = 1 - discount;
  const FULL_MONTHS = Math.floor(numDays / BILLABLE_DAYS_PER_MONTH);
  const REMAINING_DAYS = numDays % BILLABLE_DAYS_PER_MONTH;
  const DISCOUNTED_COST = FULL_MONTHS * BILLABLE_DAYS_PER_MONTH * dayRate(ratePerHour) * DISCOUNT_RATE;
  const REMAINING_COST = REMAINING_DAYS * dayRate(ratePerHour);
  return Math.ceil(DISCOUNTED_COST + REMAINING_COST);
}
