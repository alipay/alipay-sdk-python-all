#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NDeviceWorkPosition(object):

    def __init__(self):
        self._latitude = None
        self._leads_id = None
        self._longitude = None
        self._out_store_id = None

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def out_store_id(self):
        return self._out_store_id

    @out_store_id.setter
    def out_store_id(self, value):
        self._out_store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.out_store_id:
            if hasattr(self.out_store_id, 'to_alipay_dict'):
                params['out_store_id'] = self.out_store_id.to_alipay_dict()
            else:
                params['out_store_id'] = self.out_store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NDeviceWorkPosition()
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'out_store_id' in d:
            o.out_store_id = d['out_store_id']
        return o


