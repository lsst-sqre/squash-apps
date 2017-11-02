import requests
import pandas as pd
import holoviews as hv

# Instead of using hv.extension, grab a bokeh renderer

renderer = hv.renderer('bokeh')

data = requests.get("https://squash-api.lsst.codes/measurements").json()

meas_df = pd.DataFrame.from_dict(data)

meas_df['date'] = pd.to_datetime(meas_df.date, format='%Y-%m-%dT%H:%M:%SZ')

meas = hv.Dataset(meas_df, kdims=['date', 'metric_id', 'ci_dataset'],
                  vdims=['value'])

meas = meas.redim.label(date='Time (UTC)', metric_id='Metric name',
                        ci_dataset='Dataset', value='Metric measurement')

scatter = meas.to(hv.Scatter, 'date', 'value',
                  groupby=['metric_id', 'ci_dataset'])\

# plotting options

opts = {'plot': dict(tools=['hover'], width=700, height=200, xaxis=None, toolbar="above")}
scatter = scatter({'Scatter': opts})

# create a bokeh document from the holoviews object

doc = renderer.server_doc(scatter)
doc.title = "Metrics App"

