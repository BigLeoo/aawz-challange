from fastapi import APIRouter, HTTPException, Depends
from schemas.seller import SellerFecthModel, SellerCreateModelRequest, SellerCreateModelResponse, SellerGetModel, SellerDeleteModel, SellerUpdateModelRequest, SellerUpdateModel
from use_cases.create_seller import CreateSellerUseCase
from use_cases.fetch_sellers import FetchSellerUseCase
from use_cases.get_seller import GetSellerUseCase
from use_cases.delete_seller import DeleteSellerUseCase
from use_cases.update_seller import UpdateSellerUseCase
from repositories.in_memory.seller_repository_in_memory import InMemorySellerRepository
from repositories.sql_alchemy.selle_repository_sql_alchemy import SqlAlchemySellerRepository
from sqlalchemy.orm import Session
from dependecies import get_db


router = APIRouter(prefix="/sellers", tags=["Sellers"])

# sellerRepository = InMemorySellerRepository()


# ------------------ Create Seller --------
@router.post("/", response_model=SellerCreateModelResponse, status_code=201)
async def create(seller: SellerCreateModelRequest, db: Session = Depends(get_db)):
    sellerRepository = SqlAlchemySellerRepository(db)

    createSellerUseCase = CreateSellerUseCase(sellerRepository)

    try:
        sellerCreated = await createSellerUseCase.execute(
            request=seller)

        return {"sellerCreated": sellerCreated}
    except Exception as error:
        if error.__class__.__name__ == "UserAlreadyExistError":
            raise HTTPException(status_code=400, detail=str(error))

# ------------------ Fetch Sellers --------


@router.get("/", response_model=SellerFecthModel, status_code=200)
async def fetch(db: Session = Depends(get_db)):
    sellerRepository = SqlAlchemySellerRepository(db)

    fetchSellersUseCase = FetchSellerUseCase(sellerRepository)

    sellers = await fetchSellersUseCase.execute()

    return {"sellers": sellers}

# ------------------ Get one Seller --------


@router.get("/{userId}", response_model=SellerGetModel, status_code=200)
async def get(userId: int, db: Session = Depends(get_db)):
    sellerRepository = SqlAlchemySellerRepository(db)

    getSellerUseCase = GetSellerUseCase(sellerRepository)

    try:

        seller = await getSellerUseCase.execute(userId)

        return {"seller": seller}
    except Exception as error:
        if error.__class__.__name__ == "ResourceNotFoundError":
            raise HTTPException(status_code=404, detail=str(error))


# ------------------ Delete Seller --------


@router.delete("/{userId}", response_model=SellerDeleteModel, status_code=200)
async def delete(userId: int, db: Session = Depends(get_db)):
    sellerRepository = SqlAlchemySellerRepository(db)

    deleteSellerUseCase = DeleteSellerUseCase(sellerRepository)

    try:

        sellerDeleted = await deleteSellerUseCase.execute(userId)

        return {"sellerDeleted": sellerDeleted}
    except Exception as error:
        if error.__class__.__name__ == "ResourceNotFoundError":
            raise HTTPException(status_code=404, detail=str(error))

# ------------------ Update Seller --------


@router.put("/{userId}", response_model=SellerUpdateModel, status_code=200)
async def update(userId: int, sellerUpdate: SellerUpdateModelRequest, db: Session = Depends(get_db)):
    sellerRepository = SqlAlchemySellerRepository(db)

    updateSellerUseCase = UpdateSellerUseCase(sellerRepository)

    try:

        request = {"userId": userId, "sellerUpdate": sellerUpdate.dict()}

        sellerUpdated = await updateSellerUseCase.execute(request=request)

        return {"sellerUpdated": sellerUpdated}
    except Exception as error:
        if error.__class__.__name__ == "ResourceNotFoundError":
            raise HTTPException(status_code=404, detail=str(error))
        else:
            raise HTTPException(status_code=500, detail=str(error))
