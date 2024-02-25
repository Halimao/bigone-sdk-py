# BigOne-SDK-Py

An unofficial Python binding of the [V3 API](https://open.bigone.com/docs/api.html).

## Install

```bash
pip install bigone-sdk-py
```

## Usage

### How to set http proxy
bigone-sdk-py uses `requests`, so you can just simply set the http proxy through the `HTTP_PROXY` and `HTTPS_PROXY` environments:

```shell
export HTTP_PROXY=http://127.0.0.1:40880
export HTTPS_PROXY=http://127.0.0.1:40880
```

### get BTC-USDT ticker info
```python
from bigone.client import BigOneClient

api = ""
secret = ""
cli = BigOneClient(api, secret)
print(cli.get_ticker("BTC-USDT"))
```