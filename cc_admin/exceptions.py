class CCAPIError(Exception):
    def __init__(self, status_code: int, error: str):
        self.status_code = status_code
        self.error = error

class CleverChatterError(Exception):
    """Base exception for Clever Chatter API errors"""
    pass

class APIKeyError(CleverChatterError):
    """Raised when API key is missing or invalid"""
    pass

class APIRequestError(CleverChatterError):
    """Raised when API request fails"""
    pass

class APISuccessError(CleverChatterError):
    """Raised when API response success=False"""
    pass