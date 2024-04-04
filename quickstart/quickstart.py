import hls4ml

model = 'KERAS_3layer.json'

config = hls4ml.utils.fetch_example_model(model, backend='Vitis')
print(config)

hls_model = hls4ml.converters.keras_to_hls(config)

hls4ml.utils.fetch_example_list()

# Using vivado to synthesize the model
hls_model.build()

# print the report
hls4ml.report.read_vivado_report('my-hls-test')
