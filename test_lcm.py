import lcm
from lcm_glove.glove import glove
from rich import print
import numpy as np


def manus_process(channel, data):
    msg = glove.decode(data)
    print(f"Action: {np.array(msg.action)}")


lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=255")
subscription = lc.subscribe("glove", manus_process)


while True:
    lc.handle()
