import os
import pandas as pd
import json
import numpy as np
from pandas import Series, DataFrame

os.chdir(os.path.dirname(__file__))

class load_data(object):
    """

    fullVisitorId- A unique identifier for each user of the Google Merchandise Store.
    channelGrouping - The channel via which the user came to the Store.
    date - The date on which the user visited the Store.
    device - The specifications for the device used to access the Store.
    geoNetwork - This section contains information about the geography of the user.
    socialEngagementType - Engagement type, either "Socially Engaged" or "Not Socially Engaged".
    totals - This section contains aggregate values across the session.
    trafficSource - This section contains information about the Traffic Source from which the session originated.
    visitId - An identifier for this session. This is part of the value usually stored as the _utmb cookie. This is only unique to the user. For a completely unique ID, you should use a combination of fullVisitorId and visitId.
    visitNumber - The session number for this user. If this is the first session, then this is set to 1.
    visitStartTime - The timestamp (expressed as POSIX time).
    hits - This row and nested fields are populated for any and all types of hits. Provides a record of all page visits.
    customDimensions - This section contains any user-level or session-level custom dimensions that are set for a session. This is a repeated field and has an entry for each dimension that is set.
    totals - This set of columns mostly includes high-level aggregate data.

    """

    def __init__(self, target, rebuild=True):

        #self.datafile = pd.read_csv(target + '_v2.csv')
        self.path = './json'
        self.rebuild = rebuild

        if os.path.exists(self.path) == False:
            os.mkdir(self.path)

        device = self._to_json(col_name='device')
        print(device['0'])


    def _to_json(self, col_name):

        save_path = os.path.join(self.path, col_name + '.json')

        if os.path.exists(save_path) and self.rebuild==False:
            with open(save_path, mode='r', encoding='utf-8') as f:
                json_txt = f.read()
                json_txt = str(json_txt).replace("'", '"').replace('True', 'true').replace('False', 'false')
                return json.loads(json_txt)

        df = self.datafile[col_name]
        df.to_json(save_path)

        with open(save_path, mode='r', encoding='utf-8') as f:
            json_txt = f.read()
            json_txt = str(json_txt).replace("'", '"').replace('True', 'true').replace('False', 'false')

        return json.loads(json_txt)

    def _to_csv(self):
        pass



load_data(target='train', rebuild=False)