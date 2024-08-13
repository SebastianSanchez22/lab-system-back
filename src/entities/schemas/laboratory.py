from pydantic import BaseModel, model_validator

class LaboratorySchema(BaseModel):
    name: str
    schedule: str
    capacity: str

    @model_validator(mode='before')
    def validate_empty_fields(cls, values):
        for key, value in values.items():
            if not value:
                raise ValueError(f'{key} cannot be empty')
        return values