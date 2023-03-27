#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpCreditlinkloanAuthorderSubmitModel(object):

    def __init__(self):
        self._loan_type = None
        self._merchant_biz_no = None

    @property
    def loan_type(self):
        return self._loan_type

    @loan_type.setter
    def loan_type(self, value):
        self._loan_type = value
    @property
    def merchant_biz_no(self):
        return self._merchant_biz_no

    @merchant_biz_no.setter
    def merchant_biz_no(self, value):
        self._merchant_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.loan_type:
            if hasattr(self.loan_type, 'to_alipay_dict'):
                params['loan_type'] = self.loan_type.to_alipay_dict()
            else:
                params['loan_type'] = self.loan_type
        if self.merchant_biz_no:
            if hasattr(self.merchant_biz_no, 'to_alipay_dict'):
                params['merchant_biz_no'] = self.merchant_biz_no.to_alipay_dict()
            else:
                params['merchant_biz_no'] = self.merchant_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpCreditlinkloanAuthorderSubmitModel()
        if 'loan_type' in d:
            o.loan_type = d['loan_type']
        if 'merchant_biz_no' in d:
            o.merchant_biz_no = d['merchant_biz_no']
        return o


