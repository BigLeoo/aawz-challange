from repositories.seller_repository import SellerRepository
from schemas.seller import SellerBaseModelResponse, SellerUpdateModelRequest
from typing import List


class InMemorySellerRepository(SellerRepository):
    sellersDB: List[SellerBaseModelResponse] = []

    @classmethod
    async def create(cls, seller):

        newId = len(cls.sellersDB) + 1

        sellerCreated = SellerBaseModelResponse(id=newId,
                                                name=seller.name,
                                                cpf=seller.cpf,
                                                birthdate=seller.birthdate,
                                                email=seller.email,
                                                state=seller.state)

        cls.sellersDB.append(sellerCreated)

        return sellerCreated

    @classmethod
    async def findByEmail(cls, email):
        for seller in cls.sellersDB:
            if seller.email == email:
                return seller
        return None

    @classmethod
    async def fetchAllSellers(cls):
        return cls.sellersDB

    @classmethod
    async def getOneSeller(cls, id):
        for seller in cls.sellersDB:
            if seller.id == id:
                return seller
        return None

    @classmethod
    async def deleteSeller(cls, id):
        for seller in cls.sellersDB:
            if seller.id == id:
                cls.sellersDB.remove(seller)

                return seller
        return None

    @classmethod
    async def updateSeller(cls, userId: int, sellerUpdate: SellerUpdateModelRequest):
        for seller in cls.sellersDB:
            if seller.id == userId:
                if sellerUpdate["name"] is not None:
                    seller.name = sellerUpdate["name"]
                if sellerUpdate["cpf"] is not None:
                    seller.cpf = sellerUpdate["cpf"]
                if sellerUpdate["birthdate"] is not None:
                    seller.birthdate = sellerUpdate["birthdate"]
                if sellerUpdate["email"] is not None:
                    seller.email = sellerUpdate["email"]
                if sellerUpdate["state"] is not None:
                    seller.state = sellerUpdate["state"]

                return seller

        return None
