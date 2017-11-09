# squash-apps
A place to develop new visualizations or dashboards that you would like to deploy to SQuaSH


1. Clone this repo

```
git clone https://github.com/lsst-sqre/squash-apps.git
```

2. Create a virtualenv

```
cd squash-apps

virtualenv squash-apps -p python3
source squash-apps/bin/activate
pip install -r requirements.txt
```

3. Using the virtualenv in the Jupyter notebook


```
python -m ipykernel install --user --name=squash-apps
jupyter notebook
```

(You should now be able to see your kernel in the Jupyter notebook menu: `Kernel -> Change kernel` and be able so switch to it.)

Check the content of the `notebooks` folder where the visualizations are created and then the `apps` folder for an standalone version that can be deployed with `bokeh serve`, for example

```
source squash-apps/bin/activate
bokeh serve --show apps/metrics.py
```
