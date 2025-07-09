import requests

from .endpoints import (
    users,
    roles,
    permissions,
    api_modes,
    model_cats,
    models,
    capabilities,
    text_model_configs,
    model_pricings
)
from .api_response import ApiResponse


class CCAPIClient:
    def __init__(self,
        base_url:str,
        token:str
    ):
        self.base_url = base_url
        self.token = token

        self.users              = users.UsersEndpoint(self)
        self.roles              = roles.RolesEndpoint(self)
        self.permissions        = permissions.PermissionsEndpoint(self)
        self.api_modes          = api_modes.ApiModesEndpoint(self)
        self.model_cats         = model_cats.ModelCatsEndpoint(self)
        self.models             = models.ModelsEndpoint(self)
        self.capabilities       = capabilities.CapabilitiesEndpoint(self)
        self.text_model_configs = text_model_configs.TextModelConfigEndpoint(self)
        self.model_pricings     = model_pricings.ModelPricingsEndpoint(self)

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
