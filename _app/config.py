
import os

DIAGNOSTIC_MODEL = "testyboi"

UPLOADS_DIR = os.path.abspath("./uploads")

if not os.path.exists(UPLOADS_DIR):
    os.mkdir(UPLOADS_DIR)
