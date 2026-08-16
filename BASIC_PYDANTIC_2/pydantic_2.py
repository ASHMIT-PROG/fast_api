# Pydantic provides type validation and data validation
from pydantic import (
    BaseModel,
    EmailStr,
    AnyUrl,
    Field,
    field_validator,
    model_validator,
    computed_field
)

from typing import List, Optional, Annotated


# =========================================================
# NESTED MODEL
# =========================================================

# This model represents contact information of a patient
class ContactDetails(BaseModel):

    # Phone number is required
    phone: str

    # Emergency contact is optional
    emergency: Optional[str] = None


# =========================================================
# PATIENT MODEL
# =========================================================

class Patient(BaseModel):

    # Name should be a string and maximum 50 characters
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the patient",
            description="Give the name of the patient under 50 characters",
            examples=["Nitish", "Amit"]
        )
    ]

    # AnyUrl validates URL format
    linkedin_url: AnyUrl

    # Age should be an integer
    age: int

    # EmailStr validates email format
    email: EmailStr

    # Weight must be greater than 0
    # strict=True prevents type conversion
    weight: Annotated[
        float,
        Field(gt=0, strict=True)
    ]

    # Height in meters
    height: Annotated[
        float,
        Field(gt=0, strict=True)
    ]

    # Married can be True, False, or None
    married: Annotated[
        Optional[bool],
        Field(
            default=None,
            description="Is the patient married or not"
        )
    ]

    # Optional list of strings
    # Maximum 5 allergies allowed
    allergies: Annotated[
        Optional[List[str]],
        Field(
            default=None,
            max_length=5
        )
    ]

    # =====================================================
    # NESTED MODEL
    # =====================================================

    # ContactDetails model is nested inside Patient
    contact_details: ContactDetails


    # =====================================================
    # FIELD VALIDATOR
    # =====================================================

    # Custom validator for email
    @field_validator("email")
    @classmethod
    def email_validator(cls, value):

        # Only these domains are allowed
        valid_domains = ["hdfc.com", "icici.com"]

        # Extract domain
        # abc@hdfc.com -> hdfc.com
        domain_name = str(value).split("@")[-1]

        # Check domain
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")

        return value


    # Validate age after normal type validation
    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls, value):

        # Age must be between 1 and 99
        if 0 < value < 100:
            return value

        raise ValueError("Age should be between 0 to 100")


    # =====================================================
    # MODEL VALIDATOR
    # =====================================================

    # Runs after all fields have been validated
    @model_validator(mode="after")
    def validate_emergency_contact(self):

        # If patient is older than 60,
        # emergency contact must exist
        if self.age > 60 and self.contact_details.emergency is None:
            raise ValueError(
                "Patients older than 60 must have an emergency contact number"
            )

        return self


    # =====================================================
    # COMPUTED FIELD
    # =====================================================

    @computed_field
    @property
    def calculate_bmi(self) -> float:

        # BMI = weight / height^2
        bmi = round(
            self.weight / (self.height ** 2),
            2
        )

        return bmi


# =========================================================
# FUNCTION
# =========================================================

def insert_patient_record(patient: Patient):

    print("----- Patient Record -----")

    print(f"Name: {patient.name}")
    print(f"Email: {patient.email}")
    print(f"LinkedIn URL: {patient.linkedin_url}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Height: {patient.height}")
    print(f"BMI: {patient.calculate_bmi}")
    print(f"Married: {patient.married}")
    print(f"Allergies: {patient.allergies}")

    # Accessing nested model
    print(f"Phone: {patient.contact_details.phone}")
    print(f"Emergency: {patient.contact_details.emergency}")

    print("Patient inserted successfully")


# =========================================================
# PATIENT DATA
# =========================================================

patient_info = {

    "email": "abc@hdfc.com",

    "linkedin_url": "http://linkedin.com/2121",

    "name": "Ashmit",

    "age": 65,

    "weight": 70.2,

    "height": 1.67,

    "married": True,

    "allergies": [
        "pollen",
        "dust"
    ],

    # Nested model data
    "contact_details": {

        "phone": "1313413134",

        "emergency": "9999999999"
    }
}


# =========================================================
# CREATE PATIENT OBJECT
# =========================================================

patient_1 = Patient(**patient_info)


# =========================================================
# SERIALIZATION
# =========================================================

# Convert Pydantic model into Python dictionary
patient_dict = patient_1.model_dump()

print("\n----- SERIALIZED DICTIONARY -----")
print(patient_dict)


# Convert Pydantic model into JSON string
patient_json = patient_1.model_dump_json()

print("\n----- SERIALIZED JSON -----")
print(patient_json)


# =========================================================
# INSERT PATIENT
# =========================================================

insert_patient_record(patient_1)