# class_static_methods_demo.py

class Calculator:
    # Class attribute shared by all instances and accessible via the class itself
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to return the sum of two numbers.
        Does not depend on class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to return the product of two numbers.
        Uses the class itself (cls) to access class-level attributes.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
