#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantComplainReconciliationCreateModel(object):

    def __init__(self):
        self._merchant_cert_no = None

    @property
    def merchant_cert_no(self):
        return self._merchant_cert_no

    @merchant_cert_no.setter
    def merchant_cert_no(self, value):
        self._merchant_cert_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_cert_no:
            if hasattr(self.merchant_cert_no, 'to_alipay_dict'):
                params['merchant_cert_no'] = self.merchant_cert_no.to_alipay_dict()
            else:
                params['merchant_cert_no'] = self.merchant_cert_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantComplainReconciliationCreateModel()
        if 'merchant_cert_no' in d:
            o.merchant_cert_no = d['merchant_cert_no']
        return o


