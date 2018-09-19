#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetPointOrderQueryModel(object):

    def __init__(self):
        self._merchant_order_no = None

    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetPointOrderQueryModel()
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        return o


