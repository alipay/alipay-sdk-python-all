#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpCreditlinkloanAuthorderInitializeModel(object):

    def __init__(self):
        self._access_type = None
        self._loan_type = None
        self._merchant_biz_no = None
        self._operator_cert_no = None

    @property
    def access_type(self):
        return self._access_type

    @access_type.setter
    def access_type(self, value):
        self._access_type = value
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
    @property
    def operator_cert_no(self):
        return self._operator_cert_no

    @operator_cert_no.setter
    def operator_cert_no(self, value):
        self._operator_cert_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_type:
            if hasattr(self.access_type, 'to_alipay_dict'):
                params['access_type'] = self.access_type.to_alipay_dict()
            else:
                params['access_type'] = self.access_type
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
        if self.operator_cert_no:
            if hasattr(self.operator_cert_no, 'to_alipay_dict'):
                params['operator_cert_no'] = self.operator_cert_no.to_alipay_dict()
            else:
                params['operator_cert_no'] = self.operator_cert_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpCreditlinkloanAuthorderInitializeModel()
        if 'access_type' in d:
            o.access_type = d['access_type']
        if 'loan_type' in d:
            o.loan_type = d['loan_type']
        if 'merchant_biz_no' in d:
            o.merchant_biz_no = d['merchant_biz_no']
        if 'operator_cert_no' in d:
            o.operator_cert_no = d['operator_cert_no']
        return o


