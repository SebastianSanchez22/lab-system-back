from pydantic import BaseModel, model_validator, field_validator, EmailStr

class UserSchema(BaseModel):
    full_name: str
    email: EmailStr
    username: str
    password: str
    role: str = 'user' 
    disabled: bool = False 

    @model_validator(mode='before')
    def validate_empty_fields(cls, values):
        for key, value in values.items():
            if not value and key != 'disabled':
                raise ValueError(f'{key} cannot be empty')
        return values
    
    @field_validator('role')
    def validate_role(cls, value):
        if value not in ['admin', 'user']:
            raise ValueError('Invalid role')
        return value