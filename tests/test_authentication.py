from http import HTTPStatus

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
# Импортируем функцию для проверки ответа логина
from tools.assertions.authentication import assert_login_response


def test_login():
    # Инициализаруем клиенты
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()
    # Создаем пользователя
    request = CreateUserRequestSchema()
    public_users_client.create_user_api(request)
    # Логинимся под созданным пользователем
    login_request = LoginRequestSchema(email=request.email, password=request.password)
    login_response = authentication_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    # Проверяем ассерт статус кода и правильность полей в ответе.
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
    # Валидируем json схему ответа
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())