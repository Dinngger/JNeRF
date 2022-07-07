###
 # ---------------------------------------------------------------------------------------------------------------------
 # Copyright (c) 1986 - 2022, AMA team, Institute of AI and Robotics, Xi'an Jiaotong University. Proprietary and
 # Confidential All Rights Reserved.
 # ---------------------------------------------------------------------------------------------------------------------
 # NOTICE: All information contained herein is, and remains the property of AMA team, Institute of AI and Robotics,
 # Xi'an Jiaotong University. The intellectual and technical concepts contained herein are proprietary to AMA team, and
 # may be covered by P.R.C. and Foreign Patents, patents in process, and are protected by trade secret or copyright law.
 # 
 # This work may not be copied, modified, re-published, uploaded, executed, or distributed in any way, in any time, in
 # any medium, whether in whole or in part, without prior written permission from AMA team, Institute of AI and
 # Robotics, Xi'an Jiaotong University.
 # 
 # The copyright notice above does not evidence any actual or intended publication or disclosure of this source code,
 # which includes information that is confidential and/or proprietary, and is a trade secret, of AMA team.
 # ---------------------------------------------------------------------------------------------------------------------
 # @FilePath: /init.sh
 # @Author: Dinger
 # @Author's email: dinger@stu.xjtu.edu.cn
### 
export PYTHONPATH=$PYTHONPATH:./python
unset LD_LIBRARY_PATH
python tools/run_net.py --config-file ./projects/ngp/configs/ngp_comp.py --task gui
