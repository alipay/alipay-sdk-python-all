#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpAssistantProductConfig(object):

    def __init__(self):
        self._duration_quantity = None
        self._duration_unit = None
        self._license_num = None

    @property
    def duration_quantity(self):
        return self._duration_quantity

    @duration_quantity.setter
    def duration_quantity(self, value):
        self._duration_quantity = value
    @property
    def duration_unit(self):
        return self._duration_unit

    @duration_unit.setter
    def duration_unit(self, value):
        self._duration_unit = value
    @property
    def license_num(self):
        return self._license_num

    @license_num.setter
    def license_num(self, value):
        self._license_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration_quantity:
            if hasattr(self.duration_quantity, 'to_alipay_dict'):
                params['duration_quantity'] = self.duration_quantity.to_alipay_dict()
            else:
                params['duration_quantity'] = self.duration_quantity
        if self.duration_unit:
            if hasattr(self.duration_unit, 'to_alipay_dict'):
                params['duration_unit'] = self.duration_unit.to_alipay_dict()
            else:
                params['duration_unit'] = self.duration_unit
        if self.license_num:
            if hasattr(self.license_num, 'to_alipay_dict'):
                params['license_num'] = self.license_num.to_alipay_dict()
            else:
                params['license_num'] = self.license_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpAssistantProductConfig()
        if 'duration_quantity' in d:
            o.duration_quantity = d['duration_quantity']
        if 'duration_unit' in d:
            o.duration_unit = d['duration_unit']
        if 'license_num' in d:
            o.license_num = d['license_num']
        return o


