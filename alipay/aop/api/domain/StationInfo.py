#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StationInfo(object):

    def __init__(self):
        self._ext_param = None
        self._latitude = None
        self._longitude = None
        self._station_distance = None
        self._station_id = None
        self._station_index = None
        self._station_name = None
        self._station_volume = None

    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
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
    def station_distance(self):
        return self._station_distance

    @station_distance.setter
    def station_distance(self, value):
        self._station_distance = value
    @property
    def station_id(self):
        return self._station_id

    @station_id.setter
    def station_id(self, value):
        self._station_id = value
    @property
    def station_index(self):
        return self._station_index

    @station_index.setter
    def station_index(self, value):
        self._station_index = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value
    @property
    def station_volume(self):
        return self._station_volume

    @station_volume.setter
    def station_volume(self, value):
        self._station_volume = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
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
        if self.station_distance:
            if hasattr(self.station_distance, 'to_alipay_dict'):
                params['station_distance'] = self.station_distance.to_alipay_dict()
            else:
                params['station_distance'] = self.station_distance
        if self.station_id:
            if hasattr(self.station_id, 'to_alipay_dict'):
                params['station_id'] = self.station_id.to_alipay_dict()
            else:
                params['station_id'] = self.station_id
        if self.station_index:
            if hasattr(self.station_index, 'to_alipay_dict'):
                params['station_index'] = self.station_index.to_alipay_dict()
            else:
                params['station_index'] = self.station_index
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
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
        o = StationInfo()
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'station_distance' in d:
            o.station_distance = d['station_distance']
        if 'station_id' in d:
            o.station_id = d['station_id']
        if 'station_index' in d:
            o.station_index = d['station_index']
        if 'station_name' in d:
            o.station_name = d['station_name']
        if 'station_volume' in d:
            o.station_volume = d['station_volume']
        return o


