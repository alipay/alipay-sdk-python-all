#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InteopOpAuthProductInfo import InteopOpAuthProductInfo


class AlipayOpenSpInteopOpauthCreateModel(object):

    def __init__(self):
        self._inteop_order_no = None
        self._inteop_product_info = None

    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def inteop_product_info(self):
        return self._inteop_product_info

    @inteop_product_info.setter
    def inteop_product_info(self, value):
        if isinstance(value, list):
            self._inteop_product_info = list()
            for i in value:
                if isinstance(i, InteopOpAuthProductInfo):
                    self._inteop_product_info.append(i)
                else:
                    self._inteop_product_info.append(InteopOpAuthProductInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.inteop_order_no:
            if hasattr(self.inteop_order_no, 'to_alipay_dict'):
                params['inteop_order_no'] = self.inteop_order_no.to_alipay_dict()
            else:
                params['inteop_order_no'] = self.inteop_order_no
        if self.inteop_product_info:
            if isinstance(self.inteop_product_info, list):
                for i in range(0, len(self.inteop_product_info)):
                    element = self.inteop_product_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inteop_product_info[i] = element.to_alipay_dict()
            if hasattr(self.inteop_product_info, 'to_alipay_dict'):
                params['inteop_product_info'] = self.inteop_product_info.to_alipay_dict()
            else:
                params['inteop_product_info'] = self.inteop_product_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopOpauthCreateModel()
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        if 'inteop_product_info' in d:
            o.inteop_product_info = d['inteop_product_info']
        return o


