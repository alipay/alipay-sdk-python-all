#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubPromoInfoVO(object):

    def __init__(self):
        self._cost_count = None
        self._sub_type_name = None

    @property
    def cost_count(self):
        return self._cost_count

    @cost_count.setter
    def cost_count(self, value):
        self._cost_count = value
    @property
    def sub_type_name(self):
        return self._sub_type_name

    @sub_type_name.setter
    def sub_type_name(self, value):
        self._sub_type_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cost_count:
            if hasattr(self.cost_count, 'to_alipay_dict'):
                params['cost_count'] = self.cost_count.to_alipay_dict()
            else:
                params['cost_count'] = self.cost_count
        if self.sub_type_name:
            if hasattr(self.sub_type_name, 'to_alipay_dict'):
                params['sub_type_name'] = self.sub_type_name.to_alipay_dict()
            else:
                params['sub_type_name'] = self.sub_type_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubPromoInfoVO()
        if 'cost_count' in d:
            o.cost_count = d['cost_count']
        if 'sub_type_name' in d:
            o.sub_type_name = d['sub_type_name']
        return o


