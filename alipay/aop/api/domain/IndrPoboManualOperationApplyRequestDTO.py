#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionMoneyDTO import TuitionMoneyDTO


class IndrPoboManualOperationApplyRequestDTO(object):

    def __init__(self):
        self._memo = None
        self._refund_amount = None
        self._required_operation_type = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        if isinstance(value, TuitionMoneyDTO):
            self._refund_amount = value
        else:
            self._refund_amount = TuitionMoneyDTO.from_alipay_dict(value)
    @property
    def required_operation_type(self):
        return self._required_operation_type

    @required_operation_type.setter
    def required_operation_type(self, value):
        self._required_operation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.required_operation_type:
            if hasattr(self.required_operation_type, 'to_alipay_dict'):
                params['required_operation_type'] = self.required_operation_type.to_alipay_dict()
            else:
                params['required_operation_type'] = self.required_operation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrPoboManualOperationApplyRequestDTO()
        if 'memo' in d:
            o.memo = d['memo']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'required_operation_type' in d:
            o.required_operation_type = d['required_operation_type']
        return o


