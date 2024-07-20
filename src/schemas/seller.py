from pydantic import BaseModel, EmailStr, field_validator, Field
from datetime import date
from errors.invalid_cpf import InvalidCpf
from typing import Optional


class SellerBaseModel(BaseModel):
    name: str
    cpf: str
    birthdate: date
    email: EmailStr
    state: str

    @field_validator("cpf")
    @classmethod
    def cpf_validator(cls, cpf):
        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            raise InvalidCpf()

        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            raise InvalidCpf()

        # Calcula o primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10

        # Calcula o segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10

        # Verifica se os dígitos verificadores são iguais aos do CPF
        if cpf[-2:] != f"{digito1}{digito2}":
            raise InvalidCpf()

        return cpf


class SellerBaseModelResponse(SellerBaseModel):
    id: int


class SellerFecthModel(BaseModel):
    sellers: list[SellerBaseModelResponse]


class SellerGetModel(BaseModel):
    seller: SellerBaseModelResponse


class SellerUpdateModel(BaseModel):
    sellerUpdated: SellerBaseModelResponse


class SellerDeleteModel(BaseModel):
    sellerDeleted: SellerBaseModelResponse


class SellerUpdateModelRequest(BaseModel):
    name: Optional[str] = Field(default=None)
    cpf: Optional[str] = Field(default=None)
    birthdate: Optional[date] = Field(default=None)
    email: Optional[EmailStr] = Field(default=None)
    state: Optional[str] = Field(default=None)


class SellerCreateModelRequest(SellerBaseModel):
    pass


class SellerCreateModelResponse(BaseModel):
    sellerCreated: SellerBaseModelResponse
