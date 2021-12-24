#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandInfoQueryModel(object):

    def __init__(self):
        self._merchant_no = None

    @property
    def merchant_no(self):
        return self._merchant_no

    @merchant_no.setter
    def merchant_no(self, value):
        self._merchant_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_no:
            if hasattr(self.merchant_no, 'to_alipay_dict'):
                params['merchant_no'] = self.merchant_no.to_alipay_dict()
            else:
                params['merchant_no'] = self.merchant_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandInfoQueryModel()
        if 'merchant_no' in d:
            o.merchant_no = d['merchant_no']
        return o


