struct Raindrops {
    let drops: Int
    
    init(_ drops: Int) {
        self.drops = drops
    }
    
    var sounds: String {
        var raindropSpeak = String()
        
        if drops % 3 == 0 { raindropSpeak += "Pling" }
        if drops % 5 == 0 { raindropSpeak += "Plang" }
        if drops % 7 == 0 { raindropSpeak += "Plong" }
        
        if raindropSpeak.isEmpty { raindropSpeak = String(drops)}
        
        return raindropSpeak
    }
}
