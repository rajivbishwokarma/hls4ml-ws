import hls4ml

config = hls4ml.utils.fetch_example_model('KERAS_3layer.json')
print(config)

hls_model = hls4ml.converters.keras_to_hls(config)
