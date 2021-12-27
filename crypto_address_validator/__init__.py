from crypto_address_validator.validators import default_validator


validators = {
    'btc': default_validator,
}


def validate(symbol: str, address: str) -> bool:
    """Validates the address of the passed symbol.

    Args:
        symbol (str): Currency symbol, e.g. 'btc'.
        address (str): Currency address to validate.

    Returns:
        bool: Result of address validation.
    """
    try:
        validator = validators[symbol]
    except (TypeError, KeyError):
        print(f'"{symbol}" currency is not supported.')
        return False

    if not isinstance(address, str):
        return False

    # passes the address to the appropriate validator
    return validator.is_valid_address(address)
