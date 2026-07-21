Router → Waiter (takes orders, sends responses)
Service → Chef (actual business logic)
Models → Ingredients (raw data from database)
Schemas → Menu/Plate (what customer sees)
Database → Kitchen (where food is prepared)
Config → Recipe book (settings and configuration)

Request comes in
|
v
Router (routers/sessions.py)

- receives request
- validates input via Pydantic
- calls service
  |
  v
  Service (services/session.py)
- contains all business logic
- talks to database
- makes decisions
  |
  v
  Database (database.py + models/session.py)
- saves/retrieves data
  |
  v
  Router gets result back
- serializes via Pydantic schema
- returns response

pydantic reads your Settings class
|
v
sees DATABASE_URL: str (no default)
|
v
looks for "DATABASE_URL" in these places, in order:

1. actual environment variables on your system
2. your .env file (because you set env_file=".env")
   |
   v
   finds it in .env:
   DATABASE_URL=postgresql://postgres:password@localhost:5432/prepai
   |
   v
   validates it's a string ✓
   |
   v
   settings.DATABASE_URL is now available anywhere you import settings

How JWT Works
A JWT has three parts separated by dots:
header.payload.signature
Header — algorithm used:
json{"alg": "HS256", "typ": "JWT"}
Payload — data inside the token:
json{"sub": "john@example.com", "exp": 1709648000}
Signature — proof it wasn't tampered with:
HMAC_SHA256(header + payload, SECRET_KEY)
The signature is the key part. It's generated using your SECRET_KEY. If anyone changes even one character in the payload, the signature won't match anymore and you'll reject the token.
Important — the payload is just base64 encoded, not encrypted. Anyone can decode and read it. So never put passwords or sensitive data inside a JWT.

HS256???
