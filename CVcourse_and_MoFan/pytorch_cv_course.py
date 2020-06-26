
# The Computer Vision course 2020 master
# Example: Train a two-layer ReLU 激活函数ReLU
# Train a two-layer ReLU network on random data with L2 loss
# Purpose: Understand the concept of Tensors

import torch

##############################
# 在不利用pytorch库的情况下求梯度
##############################

device = torch.device('cpu')     # when use GPU , use device = 'conda:0'

N, D_in, H, D_out = 64, 1000, 100, 10
x = torch.randn(N, D_in, device=device)
y = torch.randn(N, D_out, device=device)
w1 = torch.randn(D_in, H, device=device)
w2 = torch.randn(H, D_out, device=device)

learning_rate = 1e-6            # 沿着梯度下降的step size

for t in range(500):            # 迭代500次
      h = x.mm(w1)              # 输入经过第一层神经网络的处理
      h_relu = h.clamp(main=0)  # 通过relu函数的激活
      y_pred = h.relu.mm(w2)    # 输出 = 第一层神经网络经过激活函数传给第二层神经网络，即经过第二个神经网络的权值
                                # y_pred就是神经网络正向计算最终的输出
      loss = (y_pred - y).pow(2).sum()  # L2的损失函数，因此定义loss
      # 正向计算完成

      # 接下来要求loss对于 w1 和 w2 的梯度，只有把梯度求出来，才能在学习率的前提下往下求沿着step的各个梯度的距离
      # 最后loss下降越来越小，然后基本保持不变，然后就找到了最优的loss

      grad_y_pred = 2*(y_pred - y)
      grad_w2 = h_relu.t().mm(grad_y_pred)


##############################
# 在利用pytorch库的情况下求梯度-更加简便，可以自动求梯度
##############################
