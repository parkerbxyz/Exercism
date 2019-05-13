# Calculate the moment when someone has lived for 10^9 seconds.
class Gigasecond
  SECONDS = 10**9

  def self.from(birthdate)
    birthdate + SECONDS
  end
end
