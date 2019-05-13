# Calculate the moment when someone has lived for 10^9 seconds.
class Gigasecond
  SECONDS = 10**9 # 1,000,000,000

  def self.from(birthdate)
    birthdate + SECONDS
  end
end
