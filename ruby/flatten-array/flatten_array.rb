# Accepts an arbitrarily-deep nested list-like structure and
# returns a flattened structure without any nil/null values.
class FlattenArray
  def self.flatten(array)
    array.flatten.compact
  end
end
