import torch.optim as optim

from dqn_model import DQN
from dqn_learn import OptimizerSpec, dqn_learing
from utils.schedule import LinearSchedule

import simulator

BATCH_SIZE = 32
GAMMA = 0.99 # 시간 지날 수록 감마 곱해서 reward
REPLAY_BUFFER_SIZE = 1000000
LEARNING_STARTS = 10000
LEARNING_FREQ = 4 
FRAME_HISTORY_LEN = 4 #image 4겹쳐서
TARGER_UPDATE_FREQ = 10000
LEARNING_RATE = 0.00025 
ALPHA = 0.95 # 클수록 빠르게 되지만 크게 변동, 점점 작게 #처음은 크게, 점점 작게 alpha
EPS = 0.01 #입실론

def main(env):


    optimizer_spec = OptimizerSpec(
        constructor=optim.RMSprop,
        kwargs=dict(lr=LEARNING_RATE, alpha=ALPHA, eps=EPS),
    )

    exploration_schedule = LinearSchedule(1000000, 0.1)

    dqn_learing(
        env=env,
        q_func=DQN,
        optimizer_spec=optimizer_spec,
        exploration=exploration_schedule,
        replay_buffer_size=REPLAY_BUFFER_SIZE,
        batch_size=BATCH_SIZE,
        gamma=GAMMA,
        learning_starts=LEARNING_STARTS,
        learning_freq=LEARNING_FREQ,
        frame_history_len=FRAME_HISTORY_LEN,
        target_update_freq=TARGER_UPDATE_FREQ,
    )

if __name__ == '__main__':

    env = simulator.Task(debug_flag=False, test_flag=False, state_blink=True, state_inaccurate=True)
    main(env)


