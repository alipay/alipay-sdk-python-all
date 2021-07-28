#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class SettlementbillOpenApiDTO(object):

    def __init__(self):
        self._out_biz_no = None
        self._settle_amount = None
        self._settlement_bill_no = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._settle_amount = value
        else:
            self._settle_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def settlement_bill_no(self):
        return self._settlement_bill_no

    @settlement_bill_no.setter
    def settlement_bill_no(self, value):
        self._settlement_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.settlement_bill_no:
            if hasattr(self.settlement_bill_no, 'to_alipay_dict'):
                params['settlement_bill_no'] = self.settlement_bill_no.to_alipay_dict()
            else:
                params['settlement_bill_no'] = self.settlement_bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettlementbillOpenApiDTO()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settlement_bill_no' in d:
            o.settlement_bill_no = d['settlement_bill_no']
        return o


