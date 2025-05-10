import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "rkim@example.com",
    "password": "P@ssw0rd"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

# Получаем данные пользователя
headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
user_response_data = user_response.json()

print("User response:", user_response_data)
print("Status Code:", user_response.status_code)