#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class ApBillAmtOpenApiResponse(object):

    def __init__(self):
        self._bill_no = None
        self._share_amt = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def share_amt(self):
        return self._share_amt

    @share_amt.setter
    def share_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._share_amt = value
        else:
            self._share_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.share_amt:
            if hasattr(self.share_amt, 'to_alipay_dict'):
                params['share_amt'] = self.share_amt.to_alipay_dict()
            else:
                params['share_amt'] = self.share_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApBillAmtOpenApiResponse()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'share_amt' in d:
            o.share_amt = d['share_amt']
        return o


