import sys
import time

from bitcoin_mid import BitcoinMid

# 10秒おきにBitcoinの平均値を取得する
try:
    bit = BitcoinMid()
    
    while True:
        ret = bit.get_mid()
        if (ret):
            print(bit.message)
        else:
            print('Request Error. Status:{0}'.format(bit.status))
            sys.exit

        time.sleep(10)
except KeyboardInterrupt:
    sys.exit