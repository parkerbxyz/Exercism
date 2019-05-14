# Given a year, report if it is a leap year.
class Year
  def self.leap?(year)
    (year % 4).zero? && year % 100 != 0 || (year % 400).zero?
  end
end
