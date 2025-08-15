#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ObcInvoiceObjectRequest(object):

    def __init__(self):
        self._biz_no = None
        self._biz_type = None
        self._invoicing_amount = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def invoicing_amount(self):
        return self._invoicing_amount

    @invoicing_amount.setter
    def invoicing_amount(self, value):
        self._invoicing_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.invoicing_amount:
            if hasattr(self.invoicing_amount, 'to_alipay_dict'):
                params['invoicing_amount'] = self.invoicing_amount.to_alipay_dict()
            else:
                params['invoicing_amount'] = self.invoicing_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObcInvoiceObjectRequest()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'invoicing_amount' in d:
            o.invoicing_amount = d['invoicing_amount']
        return o


