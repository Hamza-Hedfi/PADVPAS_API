import numpy as np
from numpy.linalg import norm


class Model:
    def __init__(self, *args):
        self._models = []
        self._models.extend(args)

        # Initialize the set S
        self._s = [[0 for j in range(len(args))] for i in range(len(args))]

        # Calculate the set S {}
        for index1, model1 in enumerate(self._models):
            for index2, model2 in enumerate(self._models):
                # Calculate cos(alpha)
                cos_alpha = (model1 @ model2) / (norm(model1) * norm(model2))

                # cos_alpha = np.round(cos_alpha, 10)

                if cos_alpha > 1:
                    cos_alpha = 1
                elif cos_alpha < -1:
                    cos_alpha = -1

                self._s[index1][index2] = np.arccos(cos_alpha)

        # Get avg, max and std to calculate beta
        x = set(np.ndarray.flatten(np.array(self._s)))
        x.discard(0)
        x = np.array(list(x))
        self._max_s = np.max(x)
        self._avg_s = np.average(x)
        self._std_s = np.std(x)
        self.beta = self._max_s + np.absolute(self._avg_s - self._std_s)

        self.global_ref_model = np.average(np.array(self._models), axis=0)
