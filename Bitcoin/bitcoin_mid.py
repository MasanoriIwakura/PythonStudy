import sys
import time
import json
import certifi
import urllib3


def bitcoin_thread():
    # HTTPS Settings
    http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where())
    request = http.request('GET', 'https://api.bitflyer.jp/v1/board?product_code=BTC_JPY')

    # HTTP Status check
    if request.status == 200:
        res_json = json.loads(request.data)
        print(res_json['mid_price'])
    else:
        print('Request Error!!! Status:{0}'.format(request.status))
        sys.exit

    time.sleep(60)

try:
    while True:
        bitcoin_thread()
except KeyboardInterrupt:
    sys.exit
