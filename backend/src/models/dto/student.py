from pydantic import BaseModel, ConfigDict, Field


class StudentCreate(BaseModel):
    first_name: str = Field(min_length=1, max_length=64)
    last_name: str = Field(min_length=1, max_length=64)
    middle_name: str | None = Field(default=None, max_length=64)
    class_id: int = Field(gt=0)


class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_name: str
    last_name: str
    middle_name: str | None
    class_id: int
    qr_token: str
