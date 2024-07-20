from pydantic import BaseModel
from schemas.seller import SellerBaseModelResponse
from repositories.seller_repository import SellerRepository


class FetchSellerUseCaseRequest():
    pass


class FetchSellerUseCaseResponse(BaseModel):
    sellers: list[SellerBaseModelResponse]

# InMemorySellerRepository


class FetchSellerUseCase():
    def __init__(self, sellerRepository: SellerRepository):
        self.sellerRepository = sellerRepository

    async def execute(self) -> FetchSellerUseCaseResponse:
        sellers = await self.sellerRepository.fetchAllSellers()
        return sellers
