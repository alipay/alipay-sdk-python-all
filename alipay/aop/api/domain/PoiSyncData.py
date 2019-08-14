#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PoiSyncData(object):

    def __init__(self):
        self._mini_app_id = None
        self._poi_codes = None
        self._type = None

    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def poi_codes(self):
        return self._poi_codes

    @poi_codes.setter
    def poi_codes(self, value):
        if isinstance(value, list):
            self._poi_codes = list()
            for i in value:
                self._poi_codes.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.poi_codes:
            if isinstance(self.poi_codes, list):
                for i in range(0, len(self.poi_codes)):
                    element = self.poi_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.poi_codes[i] = element.to_alipay_dict()
            if hasattr(self.poi_codes, 'to_alipay_dict'):
                params['poi_codes'] = self.poi_codes.to_alipay_dict()
            else:
                params['poi_codes'] = self.poi_codes
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PoiSyncData()
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'poi_codes' in d:
            o.poi_codes = d['poi_codes']
        if 'type' in d:
            o.type = d['type']
        return o


