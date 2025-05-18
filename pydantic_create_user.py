from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """
    Описание модели пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """
    Описание модели запроса для создания пользователя.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserResponseSchema(BaseModel):
    """
    Описание модели ответа на создание пользователя.
    """
    user: UserSchema
