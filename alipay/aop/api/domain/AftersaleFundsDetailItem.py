#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AftersaleFundsDetailItem(object):

    def __init__(self):
        self._asset_code = None
        self._asset_name = None
        self._asset_value = None

    @property
    def asset_code(self):
        return self._asset_code

    @asset_code.setter
    def asset_code(self, value):
        self._asset_code = value
    @property
    def asset_name(self):
        return self._asset_name

    @asset_name.setter
    def asset_name(self, value):
        self._asset_name = value
    @property
    def asset_value(self):
        return self._asset_value

    @asset_value.setter
    def asset_value(self, value):
        self._asset_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_code:
            if hasattr(self.asset_code, 'to_alipay_dict'):
                params['asset_code'] = self.asset_code.to_alipay_dict()
            else:
                params['asset_code'] = self.asset_code
        if self.asset_name:
            if hasattr(self.asset_name, 'to_alipay_dict'):
                params['asset_name'] = self.asset_name.to_alipay_dict()
            else:
                params['asset_name'] = self.asset_name
        if self.asset_value:
            if hasattr(self.asset_value, 'to_alipay_dict'):
                params['asset_value'] = self.asset_value.to_alipay_dict()
            else:
                params['asset_value'] = self.asset_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AftersaleFundsDetailItem()
        if 'asset_code' in d:
            o.asset_code = d['asset_code']
        if 'asset_name' in d:
            o.asset_name = d['asset_name']
        if 'asset_value' in d:
            o.asset_value = d['asset_value']
        return o


