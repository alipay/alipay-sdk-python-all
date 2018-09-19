#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpFreedepositApplyModel(object):

    def __init__(self):
        self._merchant_order_no = None
        self._merchant_url = None
        self._order_no = None

    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def merchant_url(self):
        return self._merchant_url

    @merchant_url.setter
    def merchant_url(self, value):
        self._merchant_url = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.merchant_url:
            if hasattr(self.merchant_url, 'to_alipay_dict'):
                params['merchant_url'] = self.merchant_url.to_alipay_dict()
            else:
                params['merchant_url'] = self.merchant_url
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpFreedepositApplyModel()
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'merchant_url' in d:
            o.merchant_url = d['merchant_url']
        if 'order_no' in d:
            o.order_no = d['order_no']
        return o


