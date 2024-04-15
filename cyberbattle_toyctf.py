# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from ..samples.toyctf import toy_ctf
from . import cyberbattle_env
from gym import spaces
import numpy as np


class CyberBattleToyCtf(cyberbattle_env.CyberBattleEnv):
    """CyberBattle simulation based on a toy CTF exercise"""

    def __init__(self, **kwargs):
        super().__init__(
            initial_environment=toy_ctf.new_environment(),
            **kwargs)
        self.observation_space = spaces.flatten_space(self.observation_space)