#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnifiedSettleExtendParams(object):

    def __init__(self):
        self._bank_memo = None
        self._memo = None
        self._original_order_amount = None
        self._refund_reason = None

    @property
    def bank_memo(self):
        return self._bank_memo

    @bank_memo.setter
    def bank_memo(self, value):
        self._bank_memo = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def original_order_amount(self):
        return self._original_order_amount

    @original_order_amount.setter
    def original_order_amount(self, value):
        self._original_order_amount = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_memo:
            if hasattr(self.bank_memo, 'to_alipay_dict'):
                params['bank_memo'] = self.bank_memo.to_alipay_dict()
            else:
                params['bank_memo'] = self.bank_memo
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.original_order_amount:
            if hasattr(self.original_order_amount, 'to_alipay_dict'):
                params['original_order_amount'] = self.original_order_amount.to_alipay_dict()
            else:
                params['original_order_amount'] = self.original_order_amount
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnifiedSettleExtendParams()
        if 'bank_memo' in d:
            o.bank_memo = d['bank_memo']
        if 'memo' in d:
            o.memo = d['memo']
        if 'original_order_amount' in d:
            o.original_order_amount = d['original_order_amount']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        return o


