#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnterprisePayInfo(object):

    def __init__(self):
        self._biz_info = None
        self._invoice_amount = None
        self._is_use_enterprise_pay = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def is_use_enterprise_pay(self):
        return self._is_use_enterprise_pay

    @is_use_enterprise_pay.setter
    def is_use_enterprise_pay(self, value):
        self._is_use_enterprise_pay = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.is_use_enterprise_pay:
            if hasattr(self.is_use_enterprise_pay, 'to_alipay_dict'):
                params['is_use_enterprise_pay'] = self.is_use_enterprise_pay.to_alipay_dict()
            else:
                params['is_use_enterprise_pay'] = self.is_use_enterprise_pay
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterprisePayInfo()
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'is_use_enterprise_pay' in d:
            o.is_use_enterprise_pay = d['is_use_enterprise_pay']
        return o


