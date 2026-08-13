from pydantic import BaseModel, ConfigDict, Field


class SchoolClassCreate(BaseModel):
    name: str = Field(min_length=1, max_length=32)


class SchoolClassResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
