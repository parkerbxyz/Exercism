class SpaceAge
  attr_reader :seconds

  def initialize(seconds)
    @seconds = seconds.to_f
    @earth_years = @seconds / 31_557_600
  end

  {
    earth: 1.0,
    mercury: 0.2408467,
    venus: 0.61519726,
    mars: 1.8808158,
    jupiter: 11.862615,
    saturn: 29.447498,
    uranus: 84.016846,
    neptune: 164.79132
  }.each do |planet, orbital_period|
    define_method("on_#{planet}") do
      @earth_years / orbital_period
    end
  end
end
