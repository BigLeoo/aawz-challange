from abc import ABC, abstractmethod
from schemas.seller import SellerCreateModelRequest, SellerBaseModelResponse, SellerCreateModelResponse, SellerUpdateModelRequest
from pydantic import EmailStr


class SellerRepository(ABC):
    @abstractmethod
    async def create(self, seller: SellerCreateModelRequest) -> SellerCreateModelResponse:
        pass

    @abstractmethod
    async def findByEmail(self, email: EmailStr) -> SellerBaseModelResponse:
        pass

    @abstractmethod
    async def fetchAllSellers(self) -> list[SellerBaseModelResponse]:
        pass

    @abstractmethod
    async def getOneSeller(self, id: int) -> SellerBaseModelResponse:
        pass

    @abstractmethod
    async def deleteSeller(self, id: int) -> SellerBaseModelResponse:
        pass

    @abstractmethod
    async def updateSeller(self, userId: int, sellerUpdate: SellerUpdateModelRequest) -> SellerBaseModelResponse:
        pass
