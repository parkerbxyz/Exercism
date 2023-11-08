// Package weather provides weather forecasts for various cities in Goblinocus.
package weather

// CurrentCondition is the current weather condition.
var CurrentCondition string

// CurrentLocation is the current city.
var CurrentLocation string

// Forecast returns a string describing the current weather conditions for the given city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
