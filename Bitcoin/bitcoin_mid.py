import json
import certifi
import urllib3


class BitcoinMid:
    status = True
    message = ''

    def get_mid(self):
        # HTTPS Settings
        http = urllib3.PoolManager(
                cert_reqs='CERT_REQUIRED',
                ca_certs=certifi.where())
        request = http.request('GET', 'https://api.bitflyer.jp/v1/board?product_code=BTC_JPY')

        self.status = request.status

        # HTTP Status check
        if request.status == 200:
            res_json = json.loads(request.data)
            self.message = res_json['mid_price']

            return True
        else:
            return False

