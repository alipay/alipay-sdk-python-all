#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiServindustryPromoIntelligentguideOrderModel(object):

    def __init__(self):
        self._range_type = None
        self._shop_id = None

    @property
    def range_type(self):
        return self._range_type

    @range_type.setter
    def range_type(self, value):
        self._range_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        if isinstance(value, list):
            self._shop_id = list()
            for i in value:
                self._shop_id.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.range_type:
            if hasattr(self.range_type, 'to_alipay_dict'):
                params['range_type'] = self.range_type.to_alipay_dict()
            else:
                params['range_type'] = self.range_type
        if self.shop_id:
            if isinstance(self.shop_id, list):
                for i in range(0, len(self.shop_id)):
                    element = self.shop_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_id[i] = element.to_alipay_dict()
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiServindustryPromoIntelligentguideOrderModel()
        if 'range_type' in d:
            o.range_type = d['range_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


