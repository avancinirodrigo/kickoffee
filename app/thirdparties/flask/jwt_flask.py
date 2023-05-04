from flask_jwt_extended import create_access_token
from app.entities.jason_web_token import JsonWebToken


class JwtFlask(JsonWebToken):
    def create_token(self, identity: str, additional_claims: dict) -> str:
        return create_access_token(identity=identity, additional_claims=additional_claims)
