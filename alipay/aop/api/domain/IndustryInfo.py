#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OilProductInfo import OilProductInfo


class IndustryInfo(object):

    def __init__(self):
        self._oil_product_list = None

    @property
    def oil_product_list(self):
        return self._oil_product_list

    @oil_product_list.setter
    def oil_product_list(self, value):
        if isinstance(value, list):
            self._oil_product_list = list()
            for i in value:
                if isinstance(i, OilProductInfo):
                    self._oil_product_list.append(i)
                else:
                    self._oil_product_list.append(OilProductInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.oil_product_list:
            if isinstance(self.oil_product_list, list):
                for i in range(0, len(self.oil_product_list)):
                    element = self.oil_product_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.oil_product_list[i] = element.to_alipay_dict()
            if hasattr(self.oil_product_list, 'to_alipay_dict'):
                params['oil_product_list'] = self.oil_product_list.to_alipay_dict()
            else:
                params['oil_product_list'] = self.oil_product_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryInfo()
        if 'oil_product_list' in d:
            o.oil_product_list = d['oil_product_list']
        return o


