#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NewsfeedLocationInfo(object):

    def __init__(self):
        self._ad_code = None
        self._lat = None
        self._lon = None

    @property
    def ad_code(self):
        return self._ad_code

    @ad_code.setter
    def ad_code(self, value):
        self._ad_code = value
    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value
    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, value):
        self._lon = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_code:
            if hasattr(self.ad_code, 'to_alipay_dict'):
                params['ad_code'] = self.ad_code.to_alipay_dict()
            else:
                params['ad_code'] = self.ad_code
        if self.lat:
            if hasattr(self.lat, 'to_alipay_dict'):
                params['lat'] = self.lat.to_alipay_dict()
            else:
                params['lat'] = self.lat
        if self.lon:
            if hasattr(self.lon, 'to_alipay_dict'):
                params['lon'] = self.lon.to_alipay_dict()
            else:
                params['lon'] = self.lon
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NewsfeedLocationInfo()
        if 'ad_code' in d:
            o.ad_code = d['ad_code']
        if 'lat' in d:
            o.lat = d['lat']
        if 'lon' in d:
            o.lon = d['lon']
        return o


