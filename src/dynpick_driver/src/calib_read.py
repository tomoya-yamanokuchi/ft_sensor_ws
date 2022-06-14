import numpy as np
import sys; import pathlib

p         = pathlib.Path(__file__)
save_path = "/".join(str(p.parent).split("/")[:-1]) + "/calibration_data"

idx = 0
bias_mean = np.load(save_path + "/bias_mean_idx{}.npy".format(idx))
bias_std  = np.load(save_path +  "/bias_std_idx{}.npy".format(idx))


print("bias_mean: [{: .5f}, {: .5f}, {: .5f}]".format(*bias_mean))
print("bias_std : [{: .5f}, {: .5f}, {: .5f}]".format(*bias_std))
