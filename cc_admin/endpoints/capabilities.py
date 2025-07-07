from ..api_response import ApiResponse


class CapabilitiesEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self,
            capability_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/capability/get",
            capability_id = capability_id,
            name = name
        )

    def get_all(self) -> ApiResponse:
        return self.client.request("/capability/get/all")

    def create(self,
            name:str
    ) -> ApiResponse:
        return self.client.request("/capability/create",
            name = name
        )

    def delete(self,
            capability_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/capability/delete",
           capability_id = capability_id,
           name = name
        )

    def edit(self,
            capability_id:int,
            name: str
    ) -> ApiResponse:
        return self.client.request("/capability/edit",
           capability_id = capability_id,
           name = name
       )

    def add_to_model(self,
            model_id:int,
            capability_id:int,
            api_mode_id:int
    ) -> ApiResponse:
        return self.client.request("/capability/add_to_model",
           model_id = model_id,
           capability_id = capability_id,
           api_mode_id = api_mode_id
        )

    def delete_from_model(self,
            model_id:int,
            capability_id:int
    ) -> ApiResponse:
        return self.client.request("/capability/delete_from_model",
           model_id = model_id,
           capability_id = capability_id
        )
