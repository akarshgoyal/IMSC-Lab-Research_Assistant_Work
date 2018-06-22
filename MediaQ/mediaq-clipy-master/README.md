# Requirements.
Python 2.7 and later.

# Installation
You can install the bindings via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```
Or you can install from Github via pip:

```sh
pip install git+https://github.com/ubriela/mediaq-clipy.git
```

# Tutorial
To use the bindings, import the pacakge:

```python
import SwaggerMediaq as sm
```

Create geoq client api
```python
url = "http://local.eclipse.org/MediaQ_MVC_V3/api"
geoq = sm.GeoqApi(sm.ApiClient(url))
```

Returns a set of video locations in GEOJSON format (small sample data)
```python
print geoq.sample_videos()
# http://mediaq.usc.edu/MediaQ_MVC_V3/api/geoq/sample_videos
```
Returns a set of video frames (of a particular video) in GEOJSON format (small sample data)
```python
print geoq.sample_fovs()
# http://mediaq.usc.edu/MediaQ_MVC_V3/api/geoq/sample_fovs
```

Create geoq client with API key, replace KEY_VALUE by actual one
```python
geoq = sm.GeoqApi(sm.ApiClient(url, "X-API-KEY", "KEY_VALUE"))
```

Returns a set of video locations
```python
print geoq.rectangle_query(swlat=34.019972,swlng=-118.291588,nelat=34.021111,nelng=-118.287125)
# http://mediaq.usc.edu/MediaQ_MVC_V3/api/geoq/rectangle_query?swlat=34.019972&swlng=-118.291588&nelat=34.021111&nelng=-118.287125&X-API-KEY=REAL_KEY
```

Returns a set of video locations that are captured within a time interval (startdate -> enddate)
```python
geoq.rectangle_query(swlat=34.019972,swlng=-118.291588,nelat=34.021111,nelng=-118.287125,startdate="2015-01-01 00:00:00",enddate="2016-01-01 00:00:00")
# http://mediaq.usc.edu/MediaQ_MVC_V3/api/geoq/rectangle_query?startdate=2015-01-01 00:00:00&enddate=2016-01-01 00:00:00&swlat=34.019972&swlng=-118.291588&nelat=34.021111&nelng=-118.287125&X-API-KEY=REAL_KEY
```

Returns a set of video frames
```python
print geoq.video_metadata("d0a0163e5d852e70f87bdc8718166e42989306a5")
# http://mediaq.usc.edu/MediaQ_MVC_V3/api/geoq/video_metadata?vid=d0a0163e5d852e70f87bdc8718166e42989306a5&X-API-KEY=REAL_KEY
```

# Test
You can download test file here ./test/geoq_test.py
