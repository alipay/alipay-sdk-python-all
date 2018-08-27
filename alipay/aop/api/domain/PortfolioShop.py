#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PortfolioShop(object):

    def __init__(self):
        self._display_weight = None
        self._shop_id = None

    @property
    def display_weight(self):
        return self._display_weight

    @display_weight.setter
    def display_weight(self, value):
        self._display_weight = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_weight:
            if hasattr(self.display_weight, 'to_alipay_dict'):
                params['display_weight'] = self.display_weight.to_alipay_dict()
            else:
                params['display_weight'] = self.display_weight
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PortfolioShop()
        if 'display_weight' in d:
            o.display_weight = d['display_weight']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


