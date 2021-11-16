#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarbonTranDetail(object):

    def __init__(self):
        self._carbon_type = None
        self._carbon_value = None

    @property
    def carbon_type(self):
        return self._carbon_type

    @carbon_type.setter
    def carbon_type(self, value):
        self._carbon_type = value
    @property
    def carbon_value(self):
        return self._carbon_value

    @carbon_value.setter
    def carbon_value(self, value):
        self._carbon_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.carbon_type:
            if hasattr(self.carbon_type, 'to_alipay_dict'):
                params['carbon_type'] = self.carbon_type.to_alipay_dict()
            else:
                params['carbon_type'] = self.carbon_type
        if self.carbon_value:
            if hasattr(self.carbon_value, 'to_alipay_dict'):
                params['carbon_value'] = self.carbon_value.to_alipay_dict()
            else:
                params['carbon_value'] = self.carbon_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarbonTranDetail()
        if 'carbon_type' in d:
            o.carbon_type = d['carbon_type']
        if 'carbon_value' in d:
            o.carbon_value = d['carbon_value']
        return o


