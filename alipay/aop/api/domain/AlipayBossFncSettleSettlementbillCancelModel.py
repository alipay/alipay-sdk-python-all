#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class AlipayBossFncSettleSettlementbillCancelModel(object):

    def __init__(self):
        self._cancel_amount = None
        self._out_biz_no = None
        self._source = None

    @property
    def cancel_amount(self):
        return self._cancel_amount

    @cancel_amount.setter
    def cancel_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._cancel_amount = value
        else:
            self._cancel_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_amount:
            if hasattr(self.cancel_amount, 'to_alipay_dict'):
                params['cancel_amount'] = self.cancel_amount.to_alipay_dict()
            else:
                params['cancel_amount'] = self.cancel_amount
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncSettleSettlementbillCancelModel()
        if 'cancel_amount' in d:
            o.cancel_amount = d['cancel_amount']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'source' in d:
            o.source = d['source']
        return o


