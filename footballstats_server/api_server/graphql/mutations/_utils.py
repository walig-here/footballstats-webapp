from django.forms import ModelForm


def convert_form_to_mutation_errors_response(form: ModelForm) -> list:
    form.is_valid()
    return [
        {
            "field": _snake_to_camel_case(field), 
            "messages": [
                data["message"] for data in payload
            ]
        }
        for field, payload in form.errors.get_json_data().items()
    ]


def _snake_to_camel_case(snake_str: str):
    """
    Converts snake case to camel case.
    """
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])