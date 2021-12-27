# Cryptro address validator
Simple validation tool for Bitcoin and other altcoin addresses.

## Supported currencies
| Currency      | Symbol | Mainnet | Testnet    |
|:------------- | ------ | ------- | ---------- |
| Bitcoin       | BTC    | +       | +          |
| Cosmos        | ATOM   | +       | -          |
| Binance Coin  | BNB    | +       | +          |
| Aion          | AION   | +       | +          |
| EOS           | EOS    | +       | +          |
| IOST          | IOST   | +       | +          |
| IOTA          | MIOTA  | +       | Devnet     |

## Installation
```
pip install crypto_address_validator
```

## Usage
```python
from crypto_address_validator import validate

validate('btc', 'bc1q7w9p2unf3hngtzmq3sq47cjdd0xd9sw7us5h6p')
```

## License
The Unlicense. See the LICENSE file for details.
