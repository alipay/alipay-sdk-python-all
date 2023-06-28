#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantComplainReconciliationSubmitModel(object):

    def __init__(self):
        self._merchant_cert_no = None
        self._trade_no = None

    @property
    def merchant_cert_no(self):
        return self._merchant_cert_no

    @merchant_cert_no.setter
    def merchant_cert_no(self, value):
        self._merchant_cert_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_cert_no:
            if hasattr(self.merchant_cert_no, 'to_alipay_dict'):
                params['merchant_cert_no'] = self.merchant_cert_no.to_alipay_dict()
            else:
                params['merchant_cert_no'] = self.merchant_cert_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantComplainReconciliationSubmitModel()
        if 'merchant_cert_no' in d:
            o.merchant_cert_no = d['merchant_cert_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


