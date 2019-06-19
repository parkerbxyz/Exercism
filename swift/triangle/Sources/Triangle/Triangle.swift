struct Triangle {
    let a, b, c: Double

    init(_ a: Double, _ b: Double, _ c: Double) {
        (self.a, self.b, self.c) = (a, b, c)
    }

    var kind: String {
        let perimeter = (a + b + c)

        guard min(a, b, c) > 0 && // all side lengths are positive
            max(a, b, c) <= (perimeter) - max(a, b, c) // degenerate inclusive
            else { return "ErrorKind" }

        switch (a == b, b == c, c == a ) {
        case (true, true, true):
            return "Equilateral" // all three sides are the same length
        case (false, false, false):
            return "Scalene" // all sides are of different lengths
        default:
            return "Isosceles" // two sides are the same length
        }
    }
}
