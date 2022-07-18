#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportData(object):

    def __init__(self):
        self._city_code = None
        self._line_code = None
        self._position_id = None
        self._pv = None
        self._uv = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def line_code(self):
        return self._line_code

    @line_code.setter
    def line_code(self, value):
        self._line_code = value
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, value):
        self._position_id = value
    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, value):
        self._pv = value
    @property
    def uv(self):
        return self._uv

    @uv.setter
    def uv(self, value):
        self._uv = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.line_code:
            if hasattr(self.line_code, 'to_alipay_dict'):
                params['line_code'] = self.line_code.to_alipay_dict()
            else:
                params['line_code'] = self.line_code
        if self.position_id:
            if hasattr(self.position_id, 'to_alipay_dict'):
                params['position_id'] = self.position_id.to_alipay_dict()
            else:
                params['position_id'] = self.position_id
        if self.pv:
            if hasattr(self.pv, 'to_alipay_dict'):
                params['pv'] = self.pv.to_alipay_dict()
            else:
                params['pv'] = self.pv
        if self.uv:
            if hasattr(self.uv, 'to_alipay_dict'):
                params['uv'] = self.uv.to_alipay_dict()
            else:
                params['uv'] = self.uv
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportData()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'line_code' in d:
            o.line_code = d['line_code']
        if 'position_id' in d:
            o.position_id = d['position_id']
        if 'pv' in d:
            o.pv = d['pv']
        if 'uv' in d:
            o.uv = d['uv']
        return o


