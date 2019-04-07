class Gigasecond
  GIGASECOND = 10**9  # 1,000,000,000

  def self.from(time)
    time + GIGASECOND
  end
end
