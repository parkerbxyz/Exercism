# Manage a game player's High Score list
class HighScores
  attr_reader :scores, :latest, :personal_best, :personal_top_three

  def initialize(scores)
    @scores = scores
    @latest = scores.last
    @personal_best = scores.max
    @personal_top_three = scores.max(3)
  end
end
