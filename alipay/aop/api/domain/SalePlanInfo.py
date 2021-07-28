#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SalePlanInfo(object):

    def __init__(self):
        self._custom_price_desc = None
        self._main_ps_id = None
        self._price_desc = None
        self._price_type = None
        self._ps_id = None

    @property
    def custom_price_desc(self):
        return self._custom_price_desc

    @custom_price_desc.setter
    def custom_price_desc(self, value):
        self._custom_price_desc = value
    @property
    def main_ps_id(self):
        return self._main_ps_id

    @main_ps_id.setter
    def main_ps_id(self, value):
        self._main_ps_id = value
    @property
    def price_desc(self):
        return self._price_desc

    @price_desc.setter
    def price_desc(self, value):
        self._price_desc = value
    @property
    def price_type(self):
        return self._price_type

    @price_type.setter
    def price_type(self, value):
        self._price_type = value
    @property
    def ps_id(self):
        return self._ps_id

    @ps_id.setter
    def ps_id(self, value):
        self._ps_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.custom_price_desc:
            if hasattr(self.custom_price_desc, 'to_alipay_dict'):
                params['custom_price_desc'] = self.custom_price_desc.to_alipay_dict()
            else:
                params['custom_price_desc'] = self.custom_price_desc
        if self.main_ps_id:
            if hasattr(self.main_ps_id, 'to_alipay_dict'):
                params['main_ps_id'] = self.main_ps_id.to_alipay_dict()
            else:
                params['main_ps_id'] = self.main_ps_id
        if self.price_desc:
            if hasattr(self.price_desc, 'to_alipay_dict'):
                params['price_desc'] = self.price_desc.to_alipay_dict()
            else:
                params['price_desc'] = self.price_desc
        if self.price_type:
            if hasattr(self.price_type, 'to_alipay_dict'):
                params['price_type'] = self.price_type.to_alipay_dict()
            else:
                params['price_type'] = self.price_type
        if self.ps_id:
            if hasattr(self.ps_id, 'to_alipay_dict'):
                params['ps_id'] = self.ps_id.to_alipay_dict()
            else:
                params['ps_id'] = self.ps_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SalePlanInfo()
        if 'custom_price_desc' in d:
            o.custom_price_desc = d['custom_price_desc']
        if 'main_ps_id' in d:
            o.main_ps_id = d['main_ps_id']
        if 'price_desc' in d:
            o.price_desc = d['price_desc']
        if 'price_type' in d:
            o.price_type = d['price_type']
        if 'ps_id' in d:
            o.ps_id = d['ps_id']
        return o


