from ..api_response import ApiResponse


class ModelsEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self,
            model_cat_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/model/get",
            model_cat_id = model_cat_id,
            name = name
        )

    def get_own(self) -> ApiResponse:
        return self.client.request("/model/get/own")

    def get_users(self,
            user_id:int
    ) -> ApiResponse:
        return self.client.request("/model/get/by_user",
            user_id = user_id
        )

    def get_cat(self,
            cat_id:int
    ) -> ApiResponse:
        return self.client.request("/model/get/by_cat",
            cat_id = cat_id
        )

    def create(self,
            cat_id:int,
            name:str,
            api_name:str,
            user_id:int = None,
            base_model_id:int = None,
            description:str = None
    ) -> ApiResponse:
        return self.client.request("/model/create",
            user_id = user_id,
            base_model_id = base_model_id,
            cat_id = cat_id,
            name = name,
            api_name = api_name,
            description = description
        )

    def delete(self,
            model_id:int
    ) -> ApiResponse:
        return self.client.request("/model/delete",
           model_id = model_id
        )

    def edit(self,
            model_id:int,
            user_id:int = None,
            cat_id:int = None,
            name:str = None,
            api_name:str = None,
            description:str = None
    ) -> ApiResponse:
        return self.client.request("/model_cat/edit",
            model_id = model_id,
            user_id = user_id,
            cat_id = cat_id,
            name = name,
            api_name = api_name,
            description = description
       )
