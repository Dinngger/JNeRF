'''
---------------------------------------------------------------------------------------------------------------------
Copyright (c) 1986 - 2022, AMA team, Institute of AI and Robotics, Xi'an Jiaotong University. Proprietary and
Confidential All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------
NOTICE: All information contained herein is, and remains the property of AMA team, Institute of AI and Robotics,
Xi'an Jiaotong University. The intellectual and technical concepts contained herein are proprietary to AMA team, and
may be covered by P.R.C. and Foreign Patents, patents in process, and are protected by trade secret or copyright law.

This work may not be copied, modified, re-published, uploaded, executed, or distributed in any way, in any time, in
any medium, whether in whole or in part, without prior written permission from AMA team, Institute of AI and
Robotics, Xi'an Jiaotong University.

The copyright notice above does not evidence any actual or intended publication or disclosure of this source code,
which includes information that is confidential and/or proprietary, and is a trade secret, of AMA team.
---------------------------------------------------------------------------------------------------------------------
FilePath: /python/jnerf/models/position_encoders/shg_encoder/shg_encoder.py
Author: Dinger
Author's email: dinger@stu.xjtu.edu.cn
'''
import os
import jittor as jt
from jittor import Module
from jittor.init import constant
import numpy as np
from jnerf.ops.code_ops.global_vars import global_headers,proj_options
from jnerf.utils.config import get_cfg
from jnerf.utils.registry import ENCODERS

@ENCODERS.register_module()
class SHGEncoder(Module):
    def __init__(self) :
        self.cfg = get_cfg()
        self.using_fp16 = self.cfg.fp16
        self.m_n_padded_output_dims=16
        self.m_sh_degree=4
        self.m_n_to_pad=0
        self.out_dim=self.m_n_padded_output_dims
        
    def execute(self, coords):
        x, y, z = coords[..., 0], coords[..., 1], coords[..., 2]

        xy = x * y
        xz = x * z
        yz = y * z
        x2 = x * x
        y2 = y * y
        z2 = z * z

        out = [None] * 16
        out[0] = constant(x.shape, value=0.28209479177387814)
        out[1] = -0.48860251190291987 * y
        out[2] = 0.48860251190291987 * z
        out[3] = -0.48860251190291987 * x
        out[4] = 1.0925484305920792 * xy
        out[5] = -1.0925484305920792 * yz
        out[6] = 0.94617469575755997 * z2 - 0.31539156525251999
        out[7] = -1.0925484305920792 * xz
        out[8] = 0.54627421529603959 * x2 - 0.54627421529603959 * y2
        out[9] = 0.59004358992664352 * y * (-3.0 * x2 + y2)
        out[10] = 2.8906114426405538 * xy * z
        out[11] = 0.45704579946446572 * y * (1.0 - 5.0 * z2)
        out[12] = 0.3731763325901154 * z * (5.0 * z2 - 3.0)
        out[13] = 0.45704579946446572 * x * (1.0 - 5.0 * z2)
        out[14] = 1.4453057213202769 * z * (x2 - y2)
        out[15] = 0.59004358992664352 * x * (-x2 + 3.0 * y2)

        res = jt.stack(out, dim=len(x.shape))
        if self.using_fp16:
            res=res.float16()
        return res
