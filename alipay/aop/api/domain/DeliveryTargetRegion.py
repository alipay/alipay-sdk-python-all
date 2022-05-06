#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryTargetRegion(object):

    def __init__(self):
        self._region_code = None
        self._region_name = None
        self._region_type = None

    @property
    def region_code(self):
        return self._region_code

    @region_code.setter
    def region_code(self, value):
        self._region_code = value
    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, value):
        self._region_name = value
    @property
    def region_type(self):
        return self._region_type

    @region_type.setter
    def region_type(self, value):
        self._region_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.region_code:
            if hasattr(self.region_code, 'to_alipay_dict'):
                params['region_code'] = self.region_code.to_alipay_dict()
            else:
                params['region_code'] = self.region_code
        if self.region_name:
            if hasattr(self.region_name, 'to_alipay_dict'):
                params['region_name'] = self.region_name.to_alipay_dict()
            else:
                params['region_name'] = self.region_name
        if self.region_type:
            if hasattr(self.region_type, 'to_alipay_dict'):
                params['region_type'] = self.region_type.to_alipay_dict()
            else:
                params['region_type'] = self.region_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryTargetRegion()
        if 'region_code' in d:
            o.region_code = d['region_code']
        if 'region_name' in d:
            o.region_name = d['region_name']
        if 'region_type' in d:
            o.region_type = d['region_type']
        return o


