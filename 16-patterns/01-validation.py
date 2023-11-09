# Inversion Of Control

values = {
    "product_name": "VR Visor",
    "quantity": 1,
    "home_address": {"street": "Long St", "zip": "00666"},
    "shipping_address": {"street": "Short St", "zip": "00777", "co": "Inglorious Coderz"},
    "billing_address": {"street": "Wide Plaza", "zip": "00888", "vat": "1142042"}
}


def validate(values):
    errors = {}

    if 'product_name' not in values:
        errors['product_name'] = 'required'

    if 'quantity' not in values:
        errors['quantity'] = 'required'

    errors['home_address'] = validate_address(values['home_address'])
    errors['shipping_address'] = validate_shipping_address(
        values['shipping_address'])
    errors['billing_address'] = validate_billing_address(
        values['billing_address'])

    return errors


def validate_address(address):
    errors = {}

    if 'street' not in address:
        errors['street'] = 'required'

    return errors


def validate_zip_address(address):
    errors = validate_address(address)

    if 'zip' not in address:
        errors['zip'] = 'required'

    return errors


def validate_shipping_address(address):
    errors = validate_zip_address(address)

    if 'co' not in address:
        errors['co'] = 'required'

    return errors


def validate_billing_address(address):
    errors = validate_zip_address(address)

    if 'vat' not in address:
        errors['vat'] = 'required'

    return errors


print(validate({
    "home_address": {},
    "shipping_address": {},
    "billing_address": {}
}))
