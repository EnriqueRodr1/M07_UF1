from pydantic import BaseModel

class ThemeOption(BaseModel):
    option: str

    class Config:
        from_attributes = True

class WordOption(BaseModel):
    option: str

    class Config:
        from_attributes = True
