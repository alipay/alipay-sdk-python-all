#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSaasAccountQueryModel(object):

    def __init__(self):
        self._customer_id = None
        self._out_merchant_no = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def out_merchant_no(self):
        return self._out_merchant_no

    @out_merchant_no.setter
    def out_merchant_no(self, value):
        self._out_merchant_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.out_merchant_no:
            if hasattr(self.out_merchant_no, 'to_alipay_dict'):
                params['out_merchant_no'] = self.out_merchant_no.to_alipay_dict()
            else:
                params['out_merchant_no'] = self.out_merchant_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSaasAccountQueryModel()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'out_merchant_no' in d:
            o.out_merchant_no = d['out_merchant_no']
        return o


