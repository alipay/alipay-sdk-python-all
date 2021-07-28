#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SiteItem(object):

    def __init__(self):
        self._lat_1 = None
        self._lat_2 = None
        self._lat_3 = None
        self._lat_4 = None
        self._lon_1 = None
        self._lon_2 = None
        self._lon_3 = None
        self._lon_4 = None
        self._name = None
        self._s_lat = None
        self._s_lon = None
        self._score = None
        self._site_id = None

    @property
    def lat_1(self):
        return self._lat_1

    @lat_1.setter
    def lat_1(self, value):
        self._lat_1 = value
    @property
    def lat_2(self):
        return self._lat_2

    @lat_2.setter
    def lat_2(self, value):
        self._lat_2 = value
    @property
    def lat_3(self):
        return self._lat_3

    @lat_3.setter
    def lat_3(self, value):
        self._lat_3 = value
    @property
    def lat_4(self):
        return self._lat_4

    @lat_4.setter
    def lat_4(self, value):
        self._lat_4 = value
    @property
    def lon_1(self):
        return self._lon_1

    @lon_1.setter
    def lon_1(self, value):
        self._lon_1 = value
    @property
    def lon_2(self):
        return self._lon_2

    @lon_2.setter
    def lon_2(self, value):
        self._lon_2 = value
    @property
    def lon_3(self):
        return self._lon_3

    @lon_3.setter
    def lon_3(self, value):
        self._lon_3 = value
    @property
    def lon_4(self):
        return self._lon_4

    @lon_4.setter
    def lon_4(self, value):
        self._lon_4 = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def s_lat(self):
        return self._s_lat

    @s_lat.setter
    def s_lat(self, value):
        self._s_lat = value
    @property
    def s_lon(self):
        return self._s_lon

    @s_lon.setter
    def s_lon(self, value):
        self._s_lon = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def site_id(self):
        return self._site_id

    @site_id.setter
    def site_id(self, value):
        self._site_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.lat_1:
            if hasattr(self.lat_1, 'to_alipay_dict'):
                params['lat_1'] = self.lat_1.to_alipay_dict()
            else:
                params['lat_1'] = self.lat_1
        if self.lat_2:
            if hasattr(self.lat_2, 'to_alipay_dict'):
                params['lat_2'] = self.lat_2.to_alipay_dict()
            else:
                params['lat_2'] = self.lat_2
        if self.lat_3:
            if hasattr(self.lat_3, 'to_alipay_dict'):
                params['lat_3'] = self.lat_3.to_alipay_dict()
            else:
                params['lat_3'] = self.lat_3
        if self.lat_4:
            if hasattr(self.lat_4, 'to_alipay_dict'):
                params['lat_4'] = self.lat_4.to_alipay_dict()
            else:
                params['lat_4'] = self.lat_4
        if self.lon_1:
            if hasattr(self.lon_1, 'to_alipay_dict'):
                params['lon_1'] = self.lon_1.to_alipay_dict()
            else:
                params['lon_1'] = self.lon_1
        if self.lon_2:
            if hasattr(self.lon_2, 'to_alipay_dict'):
                params['lon_2'] = self.lon_2.to_alipay_dict()
            else:
                params['lon_2'] = self.lon_2
        if self.lon_3:
            if hasattr(self.lon_3, 'to_alipay_dict'):
                params['lon_3'] = self.lon_3.to_alipay_dict()
            else:
                params['lon_3'] = self.lon_3
        if self.lon_4:
            if hasattr(self.lon_4, 'to_alipay_dict'):
                params['lon_4'] = self.lon_4.to_alipay_dict()
            else:
                params['lon_4'] = self.lon_4
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.s_lat:
            if hasattr(self.s_lat, 'to_alipay_dict'):
                params['s_lat'] = self.s_lat.to_alipay_dict()
            else:
                params['s_lat'] = self.s_lat
        if self.s_lon:
            if hasattr(self.s_lon, 'to_alipay_dict'):
                params['s_lon'] = self.s_lon.to_alipay_dict()
            else:
                params['s_lon'] = self.s_lon
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.site_id:
            if hasattr(self.site_id, 'to_alipay_dict'):
                params['site_id'] = self.site_id.to_alipay_dict()
            else:
                params['site_id'] = self.site_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SiteItem()
        if 'lat_1' in d:
            o.lat_1 = d['lat_1']
        if 'lat_2' in d:
            o.lat_2 = d['lat_2']
        if 'lat_3' in d:
            o.lat_3 = d['lat_3']
        if 'lat_4' in d:
            o.lat_4 = d['lat_4']
        if 'lon_1' in d:
            o.lon_1 = d['lon_1']
        if 'lon_2' in d:
            o.lon_2 = d['lon_2']
        if 'lon_3' in d:
            o.lon_3 = d['lon_3']
        if 'lon_4' in d:
            o.lon_4 = d['lon_4']
        if 'name' in d:
            o.name = d['name']
        if 's_lat' in d:
            o.s_lat = d['s_lat']
        if 's_lon' in d:
            o.s_lon = d['s_lon']
        if 'score' in d:
            o.score = d['score']
        if 'site_id' in d:
            o.site_id = d['site_id']
        return o


