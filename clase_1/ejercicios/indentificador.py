import numpy as np


class Identificador:
    def __init__(self, user_ids):
        super().__init__()
        idxs = np.arange(len(user_ids))
        self.idx2id = dict(zip(idxs, user_ids))
        self.id2idx = dict(zip(user_ids, idxs))
