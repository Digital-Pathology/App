# ModelManagerForWebApp

This package is an extension of [the ModelManager repo](https://github.com/Digital-Pathology/ModelManager) with added behavior expected by the WebApp of the models it uses. The only requirement is that models saved with this model manager be ManagedModels, which requires that they have a diagnose method. The diagnose method simply takes in a stream of regions and returns a diagnosis.

## An Example of End-to-End Use

Before you begin, be sure to install this package using pip. The path should be to the folder ModelManagerForWebApp

```
pip install -e /path/to/this/package/
```

### Model  Saving

```python
# Imports

from typing import Generator

import numpy as np
import torch

from model_manager_for_web_app import ModelManager, ManagedModel


# Model Training

class MyModel(torch.nn.Module):
    # your model
    pass

my_model = MyModel()
my_model.train()


# Model Saving

class MyManagedModel(ManagedModel):
    # a wrapper on a pytorch model
    def __init__(self, wrapped_model: torch.nn.Module):
        self.model = wrapped_model
    # override the diagnose method
    def diagnose(self, region_stream: Generator[np.ndarray]) -> Any:
        # simple implementation: whichever diagnosis gets the most votes wins
        votes = {"positive":0, "negative":0}
        for region in region_stream:
            votes[self.model.process(region)] += 1
        return max(votes, key=votes.get) # key with max value

my_managed_model = MyManagedModel(my_model)

model_manager = ModelManager()
model_manager.save_model(
    model_name = "my_managed_model",
    model = my_managed_model,
    model_info = {
        "description": "This is obviously a test"
    },
    overwrite_model = True # update model
)

```

## Questions?

Please direct any and all questions to Adin at adinbsolomon@gmail.com.