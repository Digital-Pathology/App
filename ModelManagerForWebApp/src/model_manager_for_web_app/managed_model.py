
"""
    ManagedModel requires diagnosis behavior from subclasses
"""

from abc import ABC, abstractmethod
from typing import Any, Generator

import numpy as np


class ManagedModel(ABC):

    """
        ManagedModel requires diagnosis behavior from subclasses
    """

    @abstractmethod
    def diagnose(self, region_stream: Generator[np.ndarray, Any, Any]) -> Any:
        """
            model takes in a stream of regions (numpy arrays) and produces diagnosis

            Example:
                # diagnosis is whichever category has the most 'votes'
                votes = {'positive':0, 'negative':0}
                for region in region_stream:
                    votes[self.process(region)] += 1
                return max(votes, key=votes.get) # key with max value
        """
        return None
