import numpy as np
import random
import csv
import json
import time
import requests
from datetime import datetime, timedelta
from sensor import mod
from msvcrt import getch


def main():
    deviceID = '24039428242'
    URL = 'https://iot.cht.com.tw/iot/v1/device/' + deviceID + '/rawdata'
    headers = {
        "CK": "PKMHW774WRHCHEEY49"
    }
    # 設定是否上傳至 iot 大平台
    iot = False
    # 設定上傳延遲時間
    second = sleeptime(0, 0, 5)
    # 設定 usb 輸入埠
    PORT = "com5"

    day = getTime('day')
    switch = True

    while True:
        if day == getTime('day'):
            # 開啟輸出的 CSV 檔案
            with open('./csv/' + getTime('day') + '.csv', 'w', newline='') as csvfile:
                if switch:
                    print('儲存檔名為：', str(getTime('day') + '.csv'))
                    # 建立 CSV 檔寫入器
                    writer = csv.writer(csvfile)
                    # 寫入一列資料
                    writer.writerow(['date', 'Dissolved_oxygen', 'pH_value', 'oxidation-reduction_potential', 'salinity', 'temperature'])
                    # 獲取感測器之值
                    # 溶氧量
                    do = mod(PORT, [3, 4, 0, 2])
                    time.sleep(sleeptime(0, 0, 1))
                    # 酸鹼值
                    ph = mod(PORT, [1, 4, 0, 2])
                    time.sleep(sleeptime(0, 0, 1))
                    # 氧化還原電位差
                    opr = mod(PORT, [4, 4, 6, 2])
                    time.sleep(sleeptime(0, 0, 1))
                    # 鹽度
                    con = mod(PORT, [2, 4, 0, 2])
                    time.sleep(sleeptime(0, 0, 1))
                    # 寫入另外幾列資料
                    writer.writerow([getTime('time'), do, ph, opr, con])
                    # 將數值寫成 josn 檔案
                    data = json.dumps([{"id": 1, "value": [do]},
                                    {"id": 2, "value": [ph]},
                                    {"id": 3, "value": [opr]},
                                    {"id": 4, "value": [con]}])
                    # 將數值即時上傳至大平台
                    if iot:
                        requests.post(URL, data=data, headers=headers)
                    switch = False
                    print('執行完畢時間：', getTime())
                    time.sleep(second)
                else :
                    # 獲取感測器之值
                    # 溶氧量
                    do = mod(PORT, [3, 4, 0, 2])
                    time.sleep(sleeptime(0, 0, 1))
                    # 酸鹼值
                    ph = mod(PORT, [1, 4, 0, 2])
                    time.sleep(sleeptime(0, 0, 1))
                    # 氧化還原電位差
                    opr = mod(PORT, [4, 4, 6, 2])
                    time.sleep(sleeptime(0, 0, 1))
                    # 鹽度
                    con = mod(PORT, [2, 4, 0, 2])
                    time.sleep(sleeptime(0, 0, 1))
                    # 寫入另外幾列資料
                    writer.writerow([getTime('time'), do, ph, opr, con])
                    # 將數值寫成 josn 檔案
                    data = json.dumps([{"id": 1, "value": [do]},
                                    {"id": 2, "value": [ph]},
                                    {"id": 3, "value": [opr]},
                                    {"id": 4, "value": [con]}])
                    # 將數值即時上傳至大平台
                    if iot:
                        requests.post(URL, data=data, headers=headers)
                    switch = False
                    print('執行完畢時間：', getTime())
                    time.sleep(second)
        else:
            day = getTime('day')
            switch = True


# 設定每多久執行一次
def sleeptime(hour, min, sec):
    time = hour*3600 + min*60 + sec
    return time

# 獲取時間
def getTime(mode = ''):
    now_time = datetime.now()  
    # 列印需要的資訊,依次是年月日,時分秒,注意字母大小寫
    # new_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
    new_time = now_time.strftime('%Y-%m-%d %H:%M')
    if mode == 'day':
        new_time = new_time.split(' ')
        time = new_time[0]
    elif mode == 'time':
        new_time = new_time.split(' ')
        time = new_time[1]
    else:
        time = now_time
    return time


if __name__ == '__main__':
    main()
