from ..api_response import ApiResponse


class PermissionsEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self,
            permission_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/permission/get",
            permission_id = permission_id,
            name = name,
        )

    def get_all(self) -> ApiResponse:
        return self.client.request("/permission/get/all")

    def create(self,
            name:str
    ) -> ApiResponse:
        return self.client.request("/permission/create",
            name = name
        )

    def delete(self,
            permission_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/permission/delete",
            permission_id = permission_id,
            name = name
        )

    def edit(self,
            permission_id:int,
            name:str
    ) -> ApiResponse:
        return self.client.request("/permission/edit",
            permission_id = permission_id,
            name = name
        )

    def check(self,
            user_id:int,
            permission:str
    ) -> ApiResponse:
        return self.client.request("/permission/check",
            user_id = user_id,
            permission = permission
        )

    def grant(self,
            role_id:int,
            permission_id:str
    ) -> ApiResponse:
        return self.client.request("/permission/grant",
            role_id = role_id,
            permission_id = permission_id
        )

    def revoke(self,
            role_id:int,
            permission_id:str
    ) -> ApiResponse:
        return self.client.request("/permission/revoke",
            role_id = role_id,
            permission_id = permission_id
        )
