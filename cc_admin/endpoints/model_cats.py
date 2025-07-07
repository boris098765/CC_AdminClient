from ..api_response import ApiResponse


class ModelCatsEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self,
            model_cat_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/model_cat/get",
            model_cat_id = model_cat_id,
            name = name
        )

    def get_all(self) -> ApiResponse:
        return self.client.request("/model_cat/get/all")

    def create(self,
            name:str,
            order:int
    ) -> ApiResponse:
        return self.client.request("/model_cat/create",
            name = name,
            order = order
        )

    def delete(self,
            model_cat_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/model_cat/delete",
           model_cat_id = model_cat_id,
           name = name
        )

    def edit(self,
            model_cat_id:int,
            name:str = None,
            order:int = None
    ) -> ApiResponse:
        return self.client.request("/model_cat/edit",
            model_cat_id = model_cat_id,
            name = name,
            order = order
       )
