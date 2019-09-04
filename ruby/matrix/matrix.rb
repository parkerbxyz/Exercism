# Return the rows and columns of a string representing a matrix of numbers.
class Matrix
  def initialize(matrix_string)
    @matrix = matrix_string
  end

  def rows
    @rows ||= @matrix.lines.map { |line| line.split.map(&:to_i) }
  end

  def columns
    @columns ||= rows.transpose
  end
end
