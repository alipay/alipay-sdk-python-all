#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExaminationPackageItem(object):

    def __init__(self):
        self._indicators = None
        self._name = None
        self._spu_id = None
        self._vendor_code = None

    @property
    def indicators(self):
        return self._indicators

    @indicators.setter
    def indicators(self, value):
        self._indicators = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def vendor_code(self):
        return self._vendor_code

    @vendor_code.setter
    def vendor_code(self, value):
        self._vendor_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.indicators:
            if hasattr(self.indicators, 'to_alipay_dict'):
                params['indicators'] = self.indicators.to_alipay_dict()
            else:
                params['indicators'] = self.indicators
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.vendor_code:
            if hasattr(self.vendor_code, 'to_alipay_dict'):
                params['vendor_code'] = self.vendor_code.to_alipay_dict()
            else:
                params['vendor_code'] = self.vendor_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationPackageItem()
        if 'indicators' in d:
            o.indicators = d['indicators']
        if 'name' in d:
            o.name = d['name']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'vendor_code' in d:
            o.vendor_code = d['vendor_code']
        return o


