import re
from rest_framework.validators import ValidationError

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    try:
        if re.fullmatch(regex, email):
            return True
        else:
            raise ValidationError({"detail":"Invalid email address"})
    except:
        raise ValidationError({"detail":"Invalid email address"})