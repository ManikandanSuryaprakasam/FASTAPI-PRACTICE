
"""Password hashing utilities using passlib.

Provides:
- pwd_context: a CryptContext configured to use bcrypt.
- Hash class with two convenience methods:
    - bcrypt(password: str) -> str : produce a bcrypt hash for the given password.
    - verify(hashed_password: str, plain_password: str) -> bool : verify a plain password against a bcrypt hash.

Notes:
- Bcrypt has a 72‑byte input limit; callers should ensure passwords are not longer than 72 bytes
  (or the implementation should truncate safely) to avoid runtime errors.
- For production you may prefer Argon2 (no 72‑byte limit) or enforce max password length in your
  Pydantic schemas.
"""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_context.hash(password)

    def verify(hashed_password, plain_password):
        return pwd_context.verify(plain_password, hashed_password)