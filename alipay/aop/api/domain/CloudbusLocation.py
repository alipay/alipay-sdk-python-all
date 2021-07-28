#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudbusLocation(object):

    def __init__(self):
        self._lat = None
        self._lng = None

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value
    @property
    def lng(self):
        return self._lng

    @lng.setter
    def lng(self, value):
        self._lng = value


    def to_alipay_dict(self):
        params = dict()
        if self.lat:
            if hasattr(self.lat, 'to_alipay_dict'):
                params['lat'] = self.lat.to_alipay_dict()
            else:
                params['lat'] = self.lat
        if self.lng:
            if hasattr(self.lng, 'to_alipay_dict'):
                params['lng'] = self.lng.to_alipay_dict()
            else:
                params['lng'] = self.lng
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudbusLocation()
        if 'lat' in d:
            o.lat = d['lat']
        if 'lng' in d:
            o.lng = d['lng']
        return o


