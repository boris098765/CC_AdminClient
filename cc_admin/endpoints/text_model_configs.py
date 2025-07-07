from ..api_response import ApiResponse


class TextModelConfigEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self,
            text_model_config_id:int
    ) -> ApiResponse:
        return self.client.request("/text_model_config/get",
            text_model_config_id = text_model_config_id
        )

    def get_by_model(self,
            model_id:int
    ) -> ApiResponse:
        return self.client.request("/text_model_config/get/by_model",
            model_id = model_id
        )

    def create(self,
            model_id:int,
            input_context_length:int,
            output_context_length:int
    ) -> ApiResponse:
        return self.client.request("/text_model_config/create",
            model_id = model_id,
            input_context_length = input_context_length,
            output_context_length = output_context_length
        )

    def delete(self,
            text_model_config_id:int = None
    ) -> ApiResponse:
        return self.client.request("/text_model_config/delete",
           text_model_config_id = text_model_config_id
        )

    def delete_by_model(self,
            model_id:int = None
    ) -> ApiResponse:
        return self.client.request("/text_model_config/delete/by_model",
           model_id = model_id
        )

    def edit(self,
            text_model_config_id:int,
            model_id:int,
            input_context_length:int = None,
            output_context_length:int = None
    ) -> ApiResponse:
        return self.client.request("/text_model_config/edit",
            text_model_config_id = text_model_config_id,
            model_id = model_id,
            input_context_length = input_context_length,
            output_context_length = output_context_length
       )
