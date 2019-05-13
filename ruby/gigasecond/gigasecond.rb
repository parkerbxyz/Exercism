class Gigasecond
  GIGASECOND = 10**9  # 1,000,000,000 seconds

  def self.from(time)
    time + GIGASECOND
  end
end
