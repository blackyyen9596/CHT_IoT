# -*- coding: utf_8 -*-


import serial
#import modbus_tk
#import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time

def main():   
    PORT="com4"
    print('PH值')
    mod(PORT, [1, 4, 0, 2])
    time.sleep(1)
    print('鹽度CON')
    mod(PORT, [2, 4, 0, 2])
    time.sleep(1)
    print('DO溶氧量')
    mod(PORT, [3, 4, 0, 2])
    time.sleep(1)
    print('ORP電極')
    mod(PORT, [4, 4, 6, 2])

def mod(PORT, order=[]):
    unit_dic = {'0a':'PH','0b':'度C','0e':'mg/L','08':'mS','':'mV'}
    red = []
    # 設定重端串口
    master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,
                                                baudrate=9600,
                                                bytesize=8, 
                                                parity='N', 
                                                stopbits=1))
    master.set_timeout(5.0)
    master.set_verbose(True)

    # 读保持寄存器
    red = master.execute(order[0], order[1], order[2], order[3])  # 这里可以修改需要读取的功能码       
    infor = hex(red[1])

    #decimal=小數點位數
    decimal = int(infor[2:3])
    #unit=單位代碼
    unit = infor[3:5]
    #處理感測器的數值
    data = int(red[0])
    data = data/(pow(10,decimal))
    unit = unit_dic[unit]
    return data


if __name__ == "__main__":    
    main()
