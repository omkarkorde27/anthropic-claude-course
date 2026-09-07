def greeting():
    return "Hello, there."


def calculate_pi():
    """
    Calculate pi to the 5th decimal place using the Machin formula.
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Returns:
        float: Pi calculated to at least 5 decimal places (3.14159)
    """
    def arctan(x, num_terms=100):
        """
        Calculate arctan(x) using Taylor series expansion.
        arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...
        """
        result = 0.0
        x_squared = x * x
        numerator = x
        
        for n in range(num_terms):
            denominator = 2 * n + 1
            if n % 2 == 0:
                result += numerator / denominator
            else:
                result -= numerator / denominator
            numerator *= x_squared
        
        return result
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = 4 * (4 * arctan(1/5) - arctan(1/239))
    
    return round(pi, 5)