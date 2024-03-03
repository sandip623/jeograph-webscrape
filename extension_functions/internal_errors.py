class LengthMismatchError(Exception):
    """Exception raised when lengths do not match"""
    def __init__(self, expected_length, actual_length):
        self.expected_length = expected_length
        self.actual_length = actual_length
        message = f"Expected length: {expected_length}. Actual length: {actual_length}."
        super().__init__(message)
