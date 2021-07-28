#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GrouponRule(object):

    def __init__(self):
        self._group_size = None
        self._groupon_price = None

    @property
    def group_size(self):
        return self._group_size

    @group_size.setter
    def group_size(self, value):
        self._group_size = value
    @property
    def groupon_price(self):
        return self._groupon_price

    @groupon_price.setter
    def groupon_price(self, value):
        self._groupon_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_size:
            if hasattr(self.group_size, 'to_alipay_dict'):
                params['group_size'] = self.group_size.to_alipay_dict()
            else:
                params['group_size'] = self.group_size
        if self.groupon_price:
            if hasattr(self.groupon_price, 'to_alipay_dict'):
                params['groupon_price'] = self.groupon_price.to_alipay_dict()
            else:
                params['groupon_price'] = self.groupon_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GrouponRule()
        if 'group_size' in d:
            o.group_size = d['group_size']
        if 'groupon_price' in d:
            o.groupon_price = d['groupon_price']
        return o


