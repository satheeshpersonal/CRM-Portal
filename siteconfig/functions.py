from rest_framework.response import Response
import re
from django.template.defaultfilters import slugify


def get_validation_error_message(model_instance):
    try:
        error_key = next(iter(model_instance.errors))
        error_code = model_instance.errors[error_key][0].title()
        return "(" + error_key.capitalize() + ")" + " " + error_code.replace('\"', '').replace('\\', '')
    except:
        return "Invalid input."
    
def method_not_allowed():
    return Response({"status" : "failure", "data": {}, "error": {"error_message":"Method not allowed ","error_code":"error"}, "extra_data" : {}},status=405)        


def filename_conversion(value):
    if "." in value:
        value, extension = value.rsplit(".", 1)
        return re.sub(r"[^a-zA-Z0-9-]", "", slugify(value))+"."+extension
    else:
        return re.sub(r"[^a-zA-Z0-9-]", "", slugify(value))