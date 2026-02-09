from jose import jwt

payload = {
    "sub": "11111111-1111-1111-1111-111111111111",
    "clinic_id": "22222222-2222-2222-2222-222222222222",
    "role": "admin"
}

print(jwt.encode(payload, "super-secret-key", algorithm="HS256"))
