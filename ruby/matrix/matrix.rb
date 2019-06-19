# Return the rows and columns of a string representing a matrix of numbers.
class Matrix
  attr_reader :rows, :columns

  def initialize(matrix_string)
    @rows = extract_rows(matrix_string)
    @columns = extract_columns(rows)
  end

  def extract_rows(matrix_string)
    matrix_string.lines.map { |line| line.split.map(&:to_i) }
  end

  def extract_columns(rows)
    rows.transpose
  end
end
