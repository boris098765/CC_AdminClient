from ..api_response import ApiResponse


class RolesEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self,
            role_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/role/get",
            role_id = role_id,
            name = name
        )

    def get_all(self) -> ApiResponse:
        return self.client.request("/role/get/all")

    def create(self,
            name:str
    ) -> ApiResponse:
        return self.client.request("/role/create",
            name = name
        )

    def delete(self,
            role_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/role/delete",
            role_id = role_id,
            name = name
        )

    def edit(self,
            role_id:int,
            name:str
    ) -> ApiResponse:
        return self.client.request("/role/edit",
            role_id = role_id,
            name = name
        )

    def grant(self,
              user_id:int,
              role_id: int
    ) -> ApiResponse:
        return self.client.request("/role/grant",
            user_id = user_id,
            role_id = role_id
        )
