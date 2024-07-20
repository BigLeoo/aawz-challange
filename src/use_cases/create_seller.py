from schemas.seller import SellerCreateModelResponse, SellerCreateModelRequest
from repositories.seller_repository import SellerRepository
from use_cases.errors.user_already_exists_error import UserAlreadyExistError


class CreateSellerUseCaseRequest(SellerCreateModelRequest):
    pass


class CreateSellerUseCaseResponse(SellerCreateModelResponse):
    pass


class CreateSellerUseCase():
    def __init__(self, sellerRepository: SellerRepository):
        self.sellerRepository = sellerRepository

    async def execute(self, request: CreateSellerUseCaseRequest) -> CreateSellerUseCaseResponse:
        userExists = await self.sellerRepository.findByEmail(email=request.email)

        if userExists:
            raise UserAlreadyExistError()

        sellerCreated = await self.sellerRepository.create(seller=request)
        return sellerCreated
