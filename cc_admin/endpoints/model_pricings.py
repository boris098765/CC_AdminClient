from ..api_response import ApiResponse


class ModelPricingsEndpoint:
    def __init__(self, client):
        self.client = client

    def get(self,
            model_pricing_id:int = None,
            name:str = None
    ) -> ApiResponse:
        return self.client.request("/model_pricing/get",
            model_pricing_id = model_pricing_id,
            name = name
        )

    def get_by_model(self,
            model_id:int
    ) -> ApiResponse:
        return self.client.request("/model_pricing/get/by_model",
            model_id = model_id
        )

    def get_by_model_and_capability(self,
            model_id:int,
            capability_id:int
    ) -> ApiResponse:
        return self.client.request("/model_pricing/get/by_model_and_capability",
            model_id = model_id,
            capability_id = capability_id
        )

    def create(self,
            model_id:int,
            capability_id:int,
            usage_type:str,
            price:float,
            price_per:int,
            currency:str,
            unit:str = None
    ) -> ApiResponse:
        return self.client.request("/model_pricing/create",
            model_id = model_id,
            capability_id = capability_id,
            usage_type = usage_type,
            price = price,
            price_per = price_per,
            unit = unit,
            currency = currency
        )

    def delete(self,
            model_pricing_id:int
    ) -> ApiResponse:
        return self.client.request("/model_pricing/delete",
           model_pricing_id = model_pricing_id
        )

    def delete_by_model(self,
            model_id:int
    ) -> ApiResponse:
        return self.client.request("/model_pricing/delete/by_model",
           model_id = model_id
        )

    def edit(self,
            model_id:int,
            capability_id:int,
            usage_type:str = None,
            price:float = None,
            price_per:int = None,
            unit:str = None,
            currency:str = None,
    ) -> ApiResponse:
        return self.client.request("/model_pricing/edit",
            model_id = model_id,
            capability_id = capability_id,
            usage_type = usage_type,
            price = price,
            price_per = price_per,
            unit = unit,
            currency = currency
        )
