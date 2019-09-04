import Foundation

struct Gigasecond {
    let description: String
    let gigasecond: TimeInterval = 1_000_000_000 // pow(10, 9)

    init?(from givenDate: String) {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss"
        dateFormatter.timeZone = TimeZone(abbreviation: "UTC")

        let formattedDate = dateFormatter.date(from: givenDate)
        description = dateFormatter.string(from: formattedDate!.addingTimeInterval(gigasecond))
    }
}
