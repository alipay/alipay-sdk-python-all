#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnifiedSettleExtendParams(object):

    def __init__(self):
        self._bank_memo = None
        self._inst_order_id = None
        self._memo = None
        self._original_order_amount = None
        self._refund_reason = None
        self._settle_mode = None
        self._trans_memo = None

    @property
    def bank_memo(self):
        return self._bank_memo

    @bank_memo.setter
    def bank_memo(self, value):
        self._bank_memo = value
    @property
    def inst_order_id(self):
        return self._inst_order_id

    @inst_order_id.setter
    def inst_order_id(self, value):
        self._inst_order_id = value
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
    @property
    def settle_mode(self):
        return self._settle_mode

    @settle_mode.setter
    def settle_mode(self, value):
        self._settle_mode = value
    @property
    def trans_memo(self):
        return self._trans_memo

    @trans_memo.setter
    def trans_memo(self, value):
        self._trans_memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_memo:
            if hasattr(self.bank_memo, 'to_alipay_dict'):
                params['bank_memo'] = self.bank_memo.to_alipay_dict()
            else:
                params['bank_memo'] = self.bank_memo
        if self.inst_order_id:
            if hasattr(self.inst_order_id, 'to_alipay_dict'):
                params['inst_order_id'] = self.inst_order_id.to_alipay_dict()
            else:
                params['inst_order_id'] = self.inst_order_id
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
        if self.settle_mode:
            if hasattr(self.settle_mode, 'to_alipay_dict'):
                params['settle_mode'] = self.settle_mode.to_alipay_dict()
            else:
                params['settle_mode'] = self.settle_mode
        if self.trans_memo:
            if hasattr(self.trans_memo, 'to_alipay_dict'):
                params['trans_memo'] = self.trans_memo.to_alipay_dict()
            else:
                params['trans_memo'] = self.trans_memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnifiedSettleExtendParams()
        if 'bank_memo' in d:
            o.bank_memo = d['bank_memo']
        if 'inst_order_id' in d:
            o.inst_order_id = d['inst_order_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'original_order_amount' in d:
            o.original_order_amount = d['original_order_amount']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'settle_mode' in d:
            o.settle_mode = d['settle_mode']
        if 'trans_memo' in d:
            o.trans_memo = d['trans_memo']
        return o


