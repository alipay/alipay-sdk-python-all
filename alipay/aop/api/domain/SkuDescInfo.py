#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkuDescInfo(object):

    def __init__(self):
        self._city = None
        self._out_pv_id = None
        self._out_sku_id = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def out_pv_id(self):
        return self._out_pv_id

    @out_pv_id.setter
    def out_pv_id(self, value):
        self._out_pv_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.out_pv_id:
            if hasattr(self.out_pv_id, 'to_alipay_dict'):
                params['out_pv_id'] = self.out_pv_id.to_alipay_dict()
            else:
                params['out_pv_id'] = self.out_pv_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuDescInfo()
        if 'city' in d:
            o.city = d['city']
        if 'out_pv_id' in d:
            o.out_pv_id = d['out_pv_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        return o


