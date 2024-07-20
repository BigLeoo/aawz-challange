from fastapi import APIRouter, HTTPException
from schemas.seller import SellerFecthModel, SellerCreateModelRequest, SellerCreateModelResponse, SellerGetModel, SellerDeleteModel, SellerUpdateModelRequest, SellerUpdateModel
from use_cases.create_seller import CreateSellerUseCase
from use_cases.fetch_sellers import FetchSellerUseCase
from use_cases.get_seller import GetSellerUseCase
from use_cases.delete_seller import DeleteSellerUseCase
from use_cases.update_seller import UpdateSellerUseCase, UpdateSellerUseCaseRequest
from repositories.in_memory.seller_repository_in_memory import InMemorySellerRepository

router = APIRouter(prefix="/sellers", tags=["Sellers"])

sellerRepository = InMemorySellerRepository()

# ------------------ Create Seller --------
createSellerUseCase = CreateSellerUseCase(sellerRepository)


@router.post("/", response_model=SellerCreateModelResponse, status_code=201)
async def create(seller: SellerCreateModelRequest):
    try:
        sellerCreated = await createSellerUseCase.execute(
            request=seller)

        return {"sellerCreated": sellerCreated}
    except Exception as error:
        if error.__class__.__name__ == "UserAlreadyExistError":
            raise HTTPException(status_code=400, detail=str(error))

# ------------------ Fetch Sellers --------
fetchSellersUseCase = FetchSellerUseCase(sellerRepository)


@router.get("/", response_model=SellerFecthModel, status_code=200)
async def fetch():

    sellers = await fetchSellersUseCase.execute()

    return {"sellers": sellers}

# ------------------ Get one Seller --------
getSellerUseCase = GetSellerUseCase(sellerRepository)


@router.get("/{userId}", response_model=SellerGetModel, status_code=200)
async def get(userId: int):
    try:

        seller = await getSellerUseCase.execute(userId)

        return {"seller": seller}
    except Exception as error:
        if error.__class__.__name__ == "ResourceNotFoundError":
            raise HTTPException(status_code=404, detail=str(error))


# ------------------ Delete Seller --------
deleteSellerUseCase = DeleteSellerUseCase(sellerRepository)


@router.delete("/{userId}", response_model=SellerDeleteModel, status_code=200)
async def delete(userId: int):
    try:

        sellerDeleted = await deleteSellerUseCase.execute(userId)

        return {"sellerDeleted": sellerDeleted}
    except Exception as error:
        if error.__class__.__name__ == "ResourceNotFoundError":
            raise HTTPException(status_code=404, detail=str(error))

# ------------------ Update Seller --------
updateSellerUseCase = UpdateSellerUseCase(sellerRepository)


@router.put("/{userId}", response_model=SellerUpdateModel, status_code=200)
async def update(userId: int, sellerUpdate: SellerUpdateModelRequest):
    try:

        request = {"userId": userId, "sellerUpdate": sellerUpdate.dict()}

        sellerUpdated = await updateSellerUseCase.execute(request=request)

        return {"sellerUpdated": sellerUpdated}
    except Exception as error:
        if error.__class__.__name__ == "ResourceNotFoundError":
            raise HTTPException(status_code=404, detail=str(error))
        else:
            raise HTTPException(status_code=500, detail=str(error))
