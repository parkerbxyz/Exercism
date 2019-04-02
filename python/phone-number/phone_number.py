N = '23456789'
X = '1234567890'
COUNTRY_CODE = '1'


class Phone:
    def __init__(self, phone_number: str):
        self.number = self.transform(phone_number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.line_number = self.number[6:]

    @staticmethod
    def transform(number: str) -> str:
        """Transform a NANP phone number into the format NXXNXXXXXX"""
        digits = ''.join(c for c in number if c.isdigit())
        if len(digits) < 10:
            raise ValueError("Number must have at least 10 digits.")
        if len(digits) > 11:
            raise ValueError("Number should not have more than 11 digits.")
        if len(digits) == 11:
            if digits[0] == COUNTRY_CODE:
                digits = digits[1:]  # Removes leading country code
            else:
                raise ValueError(f"{digits[0]} is not a valid country code.")
        if not digits[0] in N:
            raise ValueError(f"Area code can't start with {digits[0]}")
        if not digits[3] in N:
            raise ValueError(f"Exchange code can't start with {digits[3]}")
        return digits

    def pretty(self) -> str:
        """Prettify a phone number into the format (NXX) NXX-XXXX"""
        return f"({self.area_code}) {self.exchange_code}-{self.line_number}"
