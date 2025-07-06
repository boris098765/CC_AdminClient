import requests

from .endpoints import (
    users,
    roles,
)
from .api_response import ApiResponse


class CCAPIClient:
    def __init__(self,
        base_url:str,
        token:str
    ):
        self.base_url = base_url
        self.token = token

        self.users = users.UsersEndpoint(self)
        self.roles = roles.RolesEndpoint(self)

    def request(self, path, **kwargs) -> ApiResponse:
        url = f"{self.base_url}/{path.lstrip('/')}"
        params = kwargs
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.post(
            url,
            json=params,
            headers=headers
        )
        code, data = response.status_code, response.json()

        if code == 200:
            return ApiResponse.success(data['data'])
        return ApiResponse.error(data['error'])
