import time
import numpy as np
from MAF3_SerialCommunication import MAF3_SerialCommunication



class MAF3_SerialCommunicationList:
    def __init__(self, port_name_list):
        self.n_port = len(port_name_list)
        self.ser    = [MAF3_SerialCommunication(port_name) for port_name in port_name_list]


    def open(self):
        [self.ser[i].open() for i in range(self.n_port)]


    def close(self):
        [self.ser[i].close() for i in range(self.n_port)]


    def read_weight(self):
        return np.hstack([self.ser[i].read_weight() for i in range(self.n_port)])

    def _read_all_weight(self):
        return [self.ser[i]._read_all_weight() for i in range(self.n_port)]

    def print_sensitivities(self, sensitivities_list):
        [self.ser[0].print_sensitivities(sensitivities) for sensitivities in sensitivities_list]


    def print_weight(self, weight_list: list):
        weight_string_list = ["{: .2f}[N], {: .2f}[N/cm], {: .2f}[N/cm]".format(weight_list[i][2], weight_list[i][3], weight_list[i][4]) for i in range(self.n_port)]
        print(" | ".join(weight_string_list))

