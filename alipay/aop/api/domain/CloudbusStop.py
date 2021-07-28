#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudbusStop(object):

    def __init__(self):
        self._latitude = None
        self._longitude = None
        self._station_id = None
        self._station_name = None
        self._station_num = None
        self._station_space = None
        self._station_volume = None

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def station_id(self):
        return self._station_id

    @station_id.setter
    def station_id(self, value):
        self._station_id = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value
    @property
    def station_num(self):
        return self._station_num

    @station_num.setter
    def station_num(self, value):
        self._station_num = value
    @property
    def station_space(self):
        return self._station_space

    @station_space.setter
    def station_space(self, value):
        self._station_space = value
    @property
    def station_volume(self):
        return self._station_volume

    @station_volume.setter
    def station_volume(self, value):
        self._station_volume = value


    def to_alipay_dict(self):
        params = dict()
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.station_id:
            if hasattr(self.station_id, 'to_alipay_dict'):
                params['station_id'] = self.station_id.to_alipay_dict()
            else:
                params['station_id'] = self.station_id
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        if self.station_num:
            if hasattr(self.station_num, 'to_alipay_dict'):
                params['station_num'] = self.station_num.to_alipay_dict()
            else:
                params['station_num'] = self.station_num
        if self.station_space:
            if hasattr(self.station_space, 'to_alipay_dict'):
                params['station_space'] = self.station_space.to_alipay_dict()
            else:
                params['station_space'] = self.station_space
        if self.station_volume:
            if hasattr(self.station_volume, 'to_alipay_dict'):
                params['station_volume'] = self.station_volume.to_alipay_dict()
            else:
                params['station_volume'] = self.station_volume
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudbusStop()
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'station_id' in d:
            o.station_id = d['station_id']
        if 'station_name' in d:
            o.station_name = d['station_name']
        if 'station_num' in d:
            o.station_num = d['station_num']
        if 'station_space' in d:
            o.station_space = d['station_space']
        if 'station_volume' in d:
            o.station_volume = d['station_volume']
        return o


