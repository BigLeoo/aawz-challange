from pydantic import BaseModel
from schemas.seller import SellerBaseModelResponse, SellerUpdateModelRequest, SellerBaseModel
from repositories.seller_repository import SellerRepository
from use_cases.errors.resource_not_found_error import ResourceNotFoundError


class UpdateSellerUseCaseRequest():
    userId: int
    sellerUpdate: SellerUpdateModelRequest


class UpdateSellerUseCaseResponse(BaseModel):
    seller: SellerBaseModelResponse


class UpdateSellerUseCase():
    def __init__(self, sellerRepository: SellerRepository):
        self.sellerRepository = sellerRepository

    async def execute(self, request: UpdateSellerUseCaseRequest) -> UpdateSellerUseCaseResponse:
        print('entrou AUQISASDA')
        print("request dentro: ", request)
        print("id", request["userId"])

        sellerUpdated = await self.sellerRepository.updateSeller(userId=request["userId"], sellerUpdate=request["sellerUpdate"])
        print("sellerUpdated: ", sellerUpdated)

        if not sellerUpdated:
            raise ResourceNotFoundError()

        return sellerUpdated
