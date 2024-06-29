from django.core.validators import RegexValidator

alphanumeric = RegexValidator(
    r"^[a-zA-Z0-9]*$",
    "Only alphanumeric characters are allowed.",
)