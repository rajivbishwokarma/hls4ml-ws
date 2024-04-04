# Quick Start - hls4ml

This is simply an introductory lesson. We simply import a pre-built Keras layer and synthesize it with Vivado backend to get to know the general hls4ml flow.

# Line by line analysis

## 1. Import the hls4ml

```
import hls4ml
```

## 2. Fetch an example model from the hub
```
config = hls4ml.utils.fetch_example_model('KERAS_3layer.json')
```

The `fetch_example_model()` function is defined as `fetch_example_model(model_name, backend='Vivado'):`
