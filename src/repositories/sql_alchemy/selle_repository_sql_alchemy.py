from repositories.seller_repository import SellerRepository
from schemas.seller import SellerBaseModelResponse, SellerUpdateModelRequest
from typing import List
from sqlalchemy.orm import Session
from models.seller import Seller


class SqlAlchemySellerRepository(SellerRepository):
    def __init__(self, db: Session):
        self.db = db

    @classmethod
    async def create(self, seller):
        print("seller repo: ", seller)
        sellerCreated = Seller(**seller.dict())
        self.db.add(sellerCreated)
        self.db.commit()
        self.db.refresh(sellerCreated)
        return sellerCreated

    @classmethod
    async def findByEmail(self, email):
        print("email repo: ", email)
        seller = await self.db.query(Seller).filter(Seller.email == email).first()
        print("seller finded email: ", seller)
        return seller

    @classmethod
    async def fetchAllSellers(cls):
        pass

    @classmethod
    async def getOneSeller(cls, id):
        pass

    @classmethod
    async def deleteSeller(cls, id):
        pass

    @classmethod
    async def updateSeller(cls, userId: int, sellerUpdate: SellerUpdateModelRequest):
        pass
