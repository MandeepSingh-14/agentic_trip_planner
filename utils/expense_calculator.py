class Calculator:
    @staticmethod
    def multiply(a: int, b: int) -> int:
        """Multiplies two numbers and returns the result."""
        try:
            return a * b
        except ValueError:
            raise ValueError("Invalid input for multiplication. Please provide a number as a string and a float.")\
    
    @staticmethod
    def calculate_total(*x :float) -> float:
        """Calculates the total of a list of numbers."""
        try:
            return sum(x)
        except ValueError:
            raise ValueError("Invalid input for total calculation. Please provide a list of numbers.")
    
    @staticmethod
    def calculate_daily_budget(total_budget: float, total_days: int) -> float:
        """Calculates the daily budget for a trip."""
        try:
            if total_days <= 0:
                raise ValueError("Total days must be greater than zero.")
            return total_budget / total_days
        except ValueError as e:
            raise ValueError(f"Invalid input for daily budget calculation. {str(e)}")