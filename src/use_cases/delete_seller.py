from pydantic import BaseModel
from schemas.seller import SellerBaseModelResponse
from repositories.seller_repository import SellerRepository
from use_cases.errors.resource_not_found_error import ResourceNotFoundError


class DeleteSellerUseCaseRequest():
    id: int


class DeleteSellerUseCaseResponse(BaseModel):
    seller: SellerBaseModelResponse


class DeleteSellerUseCase():
    def __init__(self, sellerRepository: SellerRepository):
        self.sellerRepository = sellerRepository

    async def execute(self, request: DeleteSellerUseCaseRequest) -> DeleteSellerUseCaseResponse:
        seller = await self.sellerRepository.deleteSeller(id=request)

        if not seller:
            raise ResourceNotFoundError()

        return seller
