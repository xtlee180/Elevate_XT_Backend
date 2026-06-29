from pydantic import BaseModel

# Describe what data your API expects, schemas = API structure (blueprint for how data enters or leaves the API)
# Defines how data enters and leaves the API
class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True
