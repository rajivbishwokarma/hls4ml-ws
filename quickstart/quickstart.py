import hls4ml

config = hls4ml.utils.fetch_example_model('KERAS_3layer.json')
print(config)

hls_model = hls4ml.converters.keras_to_hls(config)

hls4ml.utils.fetch_example_list()

# Using vivado to synthesize the model
hls_model.build()

# print the report
hls4ml.report.read_vivado_report('hls-report')
