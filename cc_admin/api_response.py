from typing import Generic, TypeVar, Optional


T = TypeVar('T')

class ApiResponse(Generic[T]):
    def __init__(
        self,
        success: bool,
        message: Optional[str] = None,
        data: Optional[T] = None,
        error: Optional[T] = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error = error

    @classmethod
    def success(cls, data: T) -> 'ApiResponse[T]':
        return cls(success=True, data=data)

    @classmethod
    def error(cls, error: str) -> 'ApiResponse[T]':
        return cls(success=False, error=error)
