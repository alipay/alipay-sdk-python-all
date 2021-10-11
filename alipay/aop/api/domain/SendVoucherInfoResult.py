#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SendVoucherInfoResult(object):

    def __init__(self):
        self._merchant_order_url = None
        self._voucher_code = None

    @property
    def merchant_order_url(self):
        return self._merchant_order_url

    @merchant_order_url.setter
    def merchant_order_url(self, value):
        self._merchant_order_url = value
    @property
    def voucher_code(self):
        return self._voucher_code

    @voucher_code.setter
    def voucher_code(self, value):
        self._voucher_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_order_url:
            if hasattr(self.merchant_order_url, 'to_alipay_dict'):
                params['merchant_order_url'] = self.merchant_order_url.to_alipay_dict()
            else:
                params['merchant_order_url'] = self.merchant_order_url
        if self.voucher_code:
            if hasattr(self.voucher_code, 'to_alipay_dict'):
                params['voucher_code'] = self.voucher_code.to_alipay_dict()
            else:
                params['voucher_code'] = self.voucher_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SendVoucherInfoResult()
        if 'merchant_order_url' in d:
            o.merchant_order_url = d['merchant_order_url']
        if 'voucher_code' in d:
            o.voucher_code = d['voucher_code']
        return o


