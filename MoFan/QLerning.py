
# The reinforcement learning algorithm Q-Learning

# 探索者挖宝藏例子

######## Pesudo code   #########
# initial Q(s,a) arbitrarily
# Repeat (for each episode)         # episode： agent根据某个策略执行一系列action到结束就是一个episode
#   initialize s
#   Repeat (for each step episode)
#     Choose a from s using policy derived from Q (eg epsilon-greedy)
#     Take action a, observe r, s'
#     Q(s,a) → Q(s,a) + α[r+γmaxQ(s',a')-Q(s,a)]
#     s → s'
#   until s is terminal

import numpy as np
import pandas as pd      # pandas 也是用于数据处理的库
import time              # time 用来控制探索者的速度

np.random.seed(2)        # 产生一组伪随机数列，每次运行时随机过程一样

# 创建一些global variables 

NSTATES = 6            # 最开始和宝藏的距离 the length of the 1 dimensional world
Actions = ['left', 'right']     # 探索者可以选的两个动作，左和右  available actions
Epsiode = 0.9           # epsilone-greedy 90%选择最优动作 10%选择随机的动作
Alpha = 0.1             # learning rate 学习效率
Lambda = 0.9            # discount factor 未来的衰减值  ---这个我是理解的，强化学习课反复讲过
Max_epsiode = 13        # 最大的回合数
Fresh_time = 0.3        # 走一步花的时间

def build_q_table(n_states, actions):
       table = pd.DataFrame(                        # 用pandas创建一个表格
             np.zeros((n_states, len(actions))),      # 初始化，0举证
             columns=actions,
       ) 
       print(table)
       return table

build_q_table(NSTATES, Actions)


def choose_action(state, q_table):             # 根据状态和qtable中的值选动作
      state_actions = q_table.iloc[state, :]   # iloc是pandas的用法，通过行号来取行数据
      if (np.random.uniform() > Epsiode) or (state_actions.all() == 0): # 如果大于episode，随机选择action动作 
            action_name = np.random.choice(Actions)
      else:                                    # 如果小于episode，在table中选择大的数
            action_name = state_actions.argmax()  # argmax是pandas中的算法，取较大数的索引值
      return action_name

# 接下来创建环境和环境的feedback
def get_env_feedback(S,A):
      if A == 'right':                     # 向右移动
            if S == NSTATES -2:
                  S_ = 'terminal'          # S_就是下一个状态，R是环境返回来的reward
                  R =1
            else:
                  S_ = s +1
                  R = 0
      else:
            R = 0
            if S == 0:
                  S_ = S
            else: 
                  S_ = S - 1
      return S_, R 


# 创建环境代码，一般都是Google内置的环境，也有自己建立的环境





