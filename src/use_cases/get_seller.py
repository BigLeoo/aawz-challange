from pydantic import BaseModel
from schemas.seller import SellerBaseModelResponse
from repositories.seller_repository import SellerRepository
from use_cases.errors.resource_not_found_error import ResourceNotFoundError


class GetSellerUseCaseRequest():
    id: int


class GetSellerUseCaseResponse(BaseModel):
    seller: SellerBaseModelResponse


class GetSellerUseCase():
    def __init__(self, sellerRepository: SellerRepository):
        self.sellerRepository = sellerRepository

    async def execute(self, request: GetSellerUseCaseRequest) -> GetSellerUseCaseResponse:
        seller = await self.sellerRepository.getOneSeller(id=request)

        if not seller:
            raise ResourceNotFoundError()

        return seller
