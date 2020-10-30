import requests
import json
import time
import random
from sensor import mod
def main():
    deviceID = '24039428242'
    URL = 'https://iot.cht.com.tw/iot/v1/device/' + deviceID + '/rawdata'
    headers = {
        "CK": "PKMHW774WRHCHEEY49"
    }
    second = sleeptime(0, 10, 0)
    PORT="com4"
    # 溶氧量
    do = mod(PORT, [3, 4, 0, 2])
    do = do.split()
    # 酸鹼值
    ph = mod(PORT, [1, 4, 0, 2])
    ph = ph.split()
    # 氧化還原電位差
    opr = mod(PORT, [4, 4, 6, 2])
    opr = opr.split()
    # 鹽度
    con = mod(PORT, [2, 4, 0, 2])
    con = con.split()
    while():
        data = json.dumps([{"id": 1, "value": [do[0]]},
                        {"id": 2, "value": [ph[0]]},
                        {"id": 3, "value": [opr[0]]},
                        {"id": 4, "value": [con[0]]}])
        requests.post(URL, data=data, headers=headers)
        time.sleep(second)
    if 0xFF == ord('q'):
        break

# 設定每多久執行一次
def sleeptime(hour, min, sec):
    time = hour*3600 + min*60 + sec
    return time

if __name__ == '__main__':
    main()
