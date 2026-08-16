def test_register_success(client):
    response = client.post("/auth/register", json={
        "email":"test@example.com",
        "username":"testuser",
        "password":"password123"
    })
    assert response.status_code==201
    assert response.json()["email"] == "test@example.com"
    assert "password" not in response.json()

def test_register_duplicate_email(client):
    client.post("/auth/register", json={
        "email": "test@example.com",
        "username": "testuser",
        "password": "password123"
    })

    response = client.post("/auth/register", json={
        "email":"test@example.com",
        "username":"testuser",
        "password":"password123"
    })

    assert response.status_code == 409

def test_login_success(client):
    response = client.post("/auth/register", json={
            "email":"test@example.com",
            "username":"testuser",
            "password":"password123"
        })

    login = client.post("/auth/login", data={
    "username": "test@example.com",
    "password": "password123"
})

    assert login.status_code == 200
    assert "access_token" in login.json()

def test_login_wrong_password(client):
    client.post("/auth/register", json={
                "email":"test@example.com",
                "username":"testuser",
                "password":"password123"
            })
    login = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "wrongpassword"
    })

    assert login.status_code == 401

def test_get_me(client):
    client.post("/auth/register", json={
                    "email":"test@example.com",
                    "username":"testuser",
                    "password":"password123"
                })
    login = client.post("/auth/login", data={
            "username": "test@example.com",
            "password": "password123"
        })
    
    token = login.json()["access_token"]
    response = client.get("/users/me", headers={
        "Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"


