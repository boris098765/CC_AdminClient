from ..api_response import ApiResponse


class ApiModesEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self,
            api_mode_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/api_mode/get",
            api_mode_id = api_mode_id,
            name = name
        )

    def get_all(self) -> ApiResponse:
        return self.client.request("/api_mode/get/all")

    def create(self,
            name:str
    ) -> ApiResponse:
        return self.client.request("/api_mode/create",
            name = name
        )

    def delete(self,
            api_mode_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/api_mode/delete",
           api_mode_id = api_mode_id,
           name = name
        )

    def edit(self,
            api_mode_id:int,
            name: str
    ) -> ApiResponse:
        return self.client.request("/api_mode/edit",
           api_mode_id = api_mode_id,
           name = name
       )
