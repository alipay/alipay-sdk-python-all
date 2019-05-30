#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AreaDetail(object):

    def __init__(self):
        self._area_code = None
        self._area_name = None
        self._area_pv = None
        self._area_uv = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def area_name(self):
        return self._area_name

    @area_name.setter
    def area_name(self, value):
        self._area_name = value
    @property
    def area_pv(self):
        return self._area_pv

    @area_pv.setter
    def area_pv(self, value):
        self._area_pv = value
    @property
    def area_uv(self):
        return self._area_uv

    @area_uv.setter
    def area_uv(self, value):
        self._area_uv = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.area_name:
            if hasattr(self.area_name, 'to_alipay_dict'):
                params['area_name'] = self.area_name.to_alipay_dict()
            else:
                params['area_name'] = self.area_name
        if self.area_pv:
            if hasattr(self.area_pv, 'to_alipay_dict'):
                params['area_pv'] = self.area_pv.to_alipay_dict()
            else:
                params['area_pv'] = self.area_pv
        if self.area_uv:
            if hasattr(self.area_uv, 'to_alipay_dict'):
                params['area_uv'] = self.area_uv.to_alipay_dict()
            else:
                params['area_uv'] = self.area_uv
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AreaDetail()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'area_name' in d:
            o.area_name = d['area_name']
        if 'area_pv' in d:
            o.area_pv = d['area_pv']
        if 'area_uv' in d:
            o.area_uv = d['area_uv']
        return o


