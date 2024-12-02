#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnifiedSettleExtendParams(object):

    def __init__(self):
        self._memo = None
        self._refund_reason = None
        self._second_merchant_no = None
        self._second_merchant_type = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def second_merchant_no(self):
        return self._second_merchant_no

    @second_merchant_no.setter
    def second_merchant_no(self, value):
        self._second_merchant_no = value
    @property
    def second_merchant_type(self):
        return self._second_merchant_type

    @second_merchant_type.setter
    def second_merchant_type(self, value):
        self._second_merchant_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.second_merchant_no:
            if hasattr(self.second_merchant_no, 'to_alipay_dict'):
                params['second_merchant_no'] = self.second_merchant_no.to_alipay_dict()
            else:
                params['second_merchant_no'] = self.second_merchant_no
        if self.second_merchant_type:
            if hasattr(self.second_merchant_type, 'to_alipay_dict'):
                params['second_merchant_type'] = self.second_merchant_type.to_alipay_dict()
            else:
                params['second_merchant_type'] = self.second_merchant_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnifiedSettleExtendParams()
        if 'memo' in d:
            o.memo = d['memo']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'second_merchant_no' in d:
            o.second_merchant_no = d['second_merchant_no']
        if 'second_merchant_type' in d:
            o.second_merchant_type = d['second_merchant_type']
        return o


