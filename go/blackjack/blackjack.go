package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	switch card {
	case "ace":
		return 11
	case "king", "queen", "jack", "ten":
		return 10
	case "nine":
		return 9
	case "eight":
		return 8
	case "seven":
		return 7
	case "six":
		return 6
	case "five":
		return 5
	case "four":
		return 4
	case "three":
		return 3
	case "two":
		return 2
	default:
		return 0
	}
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	playerCardSum := ParseCard(card1) + ParseCard(card2)
	dealerCardValue := ParseCard(dealerCard)

	const (
		stand = "S"
		hit   = "H"
		split = "P"
		win   = "W"
	)

	switch playerCardSum {
	case 22:
		return split
	case 21:
		if dealerCardValue < 10 {
			return win
		} else {
			return stand
		}
	case 17, 18, 19, 20:
		return stand
	case 12, 13, 14, 15, 16:
		if dealerCardValue >= 7 {
			return hit
		} else {
			return stand
		}
	default:
		return hit
	}
}
