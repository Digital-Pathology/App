
"""
    A wrapper on ModelManager that requires use of ManagedModel
"""

import os
from typing import Any

from model_manager import ModelManager as OriginalModelManager

from .managed_model import ManagedModel


class ModelManager(OriginalModelManager):

    """
        Requires saved models to be ManagedModels
    """

    DEFAULT_MODEL_DIR = os.path.join(
        os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.dirname(__file__)))),
        "models",
        ""
    )

    def __init__(self):
        super().__init__(ModelManager.DEFAULT_MODEL_DIR)

    def save_model(self,
                   model_name: str,
                   model: ManagedModel,  # no longer Any
                   model_info: dict = None,
                   overwrite_model: bool = False):
        if not isinstance(model, ManagedModel):
            raise TypeError(
                f"model must be of type ManagedModel but is {type(model)=}")
        return super().save_model(
            model_name,
            model,
            model_info,
            overwrite_model
        )


print(ModelManager.DEFAULT_MODEL_DIR)
