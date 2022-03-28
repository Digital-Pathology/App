
import os

DEFAULT_MODELS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "models"
)

print(DEFAULT_MODELS_DIR)
