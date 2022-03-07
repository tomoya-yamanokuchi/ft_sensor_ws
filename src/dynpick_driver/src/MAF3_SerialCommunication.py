import time
import numpy as np
import serial
from serial import Serial
import rospy


class MAF3_SerialCommunication:
    def __init__(self):
        self.R                   = "R"      # 単データリクエストコマンド
        self.P                   = "P"      # 主軸感度リクエストコマンド
        self.n_data_R            = 27       # 単データリクエストの際に返ってくるデータのバイト数
        self.n_data_force_torque = 24       # 単データリクエストの際に返ってくるデータのうちForce/Torqueだけのデータのバイト数
        self.n_data_P            = 26       # 主軸感度リクエストの際に返ってくるデータのバイト数
        self.n_axis              = 6        # 軸の数 (Fx, Fy, Fz, Mx, My, Mz) = 6個
        self.unit_P_response     = 0.001    # 主軸感度リクエストで返って来るデータの単位が[0.001digit/N] or [0.001digit/Nm]
        self.raw_data_at_free    = 8192     # 零点出力（無負荷時の出力値）


    def open(self):
        self.ser = serial.Serial(
            port     = '/dev/ttyUSB0',
            baudrate = 921600,
            timeout  = None,
            bytesize = serial.EIGHTBITS,
            parity   = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE
        )
        self.sensitivities = self.read_sensitivity()
        self.print_sensitivities(self.sensitivities)


    def close(self):
        self.ser.close()


    def _read_sensitivity(self):
        self.ser.write(self.P.encode())
        sensitivities = [0.0]*self.n_axis
        for i in range(6):
            sensitivities[i] = int.from_bytes(self.ser.read(4), byteorder='little') * self.unit_P_response
        self.ser.read(2) # 行末に2バイトのチェックサムがあるので最後まで読み込む
        return sensitivities


    def _change_moment_unit_of_sensitivities(self, sensitivities):
        # モーメントの単位を[digit/Nm]から[digit/Ncm]に変換
        moment_index = [-3, -2, -1]
        for index in moment_index:
           sensitivities[index] = sensitivities[index] * 0.01
        return sensitivities


    def read_sensitivity(self):
        return self._change_moment_unit_of_sensitivities(self._read_sensitivity())


    def _read_raw_data(self):
        self.ser.write(self.R.encode())
        data     = self.ser.readline()
        data_str = data.decode()
        assert len(data_str) == self.n_data_R
        force_torque    = [0.0]*self.n_axis
        force_torque[0] = int(data_str[1:5], 16)
        force_torque[1] = int(data_str[5:9], 16)
        force_torque[2] = int(data_str[9:13], 16)
        force_torque[3] = int(data_str[13:17], 16)
        force_torque[4] = int(data_str[17:21], 16)
        force_torque[5] = int(data_str[21:25], 16)
        return force_torque


    def convert_raw_data_to_weight(self, raw_data: list):
        assert len(raw_data) == self.n_axis
        # 並進力    : 検出荷重[N]   = ( 検出値 [LSB] - 零点出力値 [LSB] ) ÷ 主軸感度 [LSB/N]
        # モーメント: 検出荷重[Ncm] = ( 検出値 [LSB] - 零点出力値 [LSB] ) ÷ 主軸感度 [LSB/Ncm]
        return [(raw_data[i] - self.raw_data_at_free) / self.sensitivities[i] for i in range(self.n_axis)]


    def read_weight(self):
        return self.convert_raw_data_to_weight(self._read_raw_data())


    def print_sensitivities(self, sensitivities):
        axis_name_list = ["Fx", "Fy", "Fz", "Mx", "My", "Mz"]
        print("========================")
        print(" sensitivities: ")
        for i in range(self.n_axis):
            print("     {} : {:.3f}    ".format(axis_name_list[i], sensitivities[i]))
        print("========================")


    def print_weight(self, weight: list):
        assert len(weight) == self.n_axis
        print("{:.2f}[N], {:.2f}[N], {:.2f}[N], {:.2f}[N/cm], {:.2f}[N/cm], {:.2f}[N/cm]".format(
               weight[0], weight[1], weight[2], weight[3],    weight[4],    weight[5]))


    def print_raw_data(self, raw_data: list):
        info = ["{},".format(raw_data[i]) for i in range(len(raw_data))]
        print(" ".join(info)[:-1])


if __name__ == "__main__":
    ft_ser = MAF3_SerialCommunication()

    ft_ser.open()
    for i in range(1000):
        data = ft_ser.read_weight()
        ft_ser.print_weight(data)
    ft_ser.close()
