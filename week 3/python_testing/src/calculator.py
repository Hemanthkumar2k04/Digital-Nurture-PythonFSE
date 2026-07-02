class Calculator:
    def __init__(self):
        self._memory = 0

    def add(self, a: float, b: float) -> float:
        return a + b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def get_memory(self) -> float:
        return self._memory

    def add_to_memory(self, value: float):
        self._memory += value

    def clear_memory(self):
        self._memory = 0
