## Hades Bot

binance/okx based, currently it can only support real time Tick/Bar/Order/Position live update and monitor. In `bot/strategies/sample` , created a simple strategy, doing nothing but send notification 
![alt text](./doc/screenshot.png "Screen Shot")
## How to start

### 1. Setup Environment

```shell
python -m venv runtime
runtime\Scripts\activate
pip install -r requirements.txt
# if requirements.txt not work
pip3 install python-okx websockets requests binance-futures-connector
```

### 2. Change Configuration

copy `example.conf` and rename to `app.conf` , change parameter

```ini
[binance]
apiKey           = apiKey
secretKey        = secretKey

[okx]
apiKey           = apiKey
secretKey        = secretKey
passphrase       = passphrase
ws_private       = wss://wsaws.okx.com:8443/ws/v5/private
ws_public        = wss://wsaws.okx.com:8443/ws/v5/public
ws_business      = wss://wsaws.okx.com:8443/ws/v5/business
domain           = https://aws.okx.com
useServerTime    = False

[notification]
token            = token
prefix           = prefix
period           = 8-23
```
