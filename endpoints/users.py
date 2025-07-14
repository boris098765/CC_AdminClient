from ..api_response import ApiResponse


class UsersEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self,
            user_id:int = None,
            login:str = None,
            user_api_key:str = None,
    ) -> ApiResponse:
        return self.client.request("/user/get",
            user_id      = user_id,
            login        = login,
            user_api_key = user_api_key,
        )

    def get_count(self) -> ApiResponse:
        return self.client.request("/user/get/count")

    def get_list(self,
            limit:int = 20,
            offset:int = 0,
            desc:bool = True
    ) -> ApiResponse:
        return self.client.request("/user/get/list",
            limit  = limit,
            offset = offset,
            desc   = desc,
        )

    def create(self,
            login:str,
            name:str,
            role_id:int
    ) -> ApiResponse:
        return self.client.request("/user/create",
            login   = login,
            name    = name,
            role_id = role_id
        )

    def delete(self,
            user_id:int = None,
            login:str = None
    ) -> ApiResponse:
        return self.client.request("/user/delete",
            user_id = user_id,
            login   = login
        )

    def edit(self,
            user_id:int,
            login:str = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/user/edit",
            user_id = user_id,
            login   = login,
            name    = name
        )
