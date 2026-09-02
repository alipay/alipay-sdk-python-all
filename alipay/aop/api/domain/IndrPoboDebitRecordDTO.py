#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrMoneyDTO import IndrMoneyDTO


class IndrPoboDebitRecordDTO(object):

    def __init__(self):
        self._actual_debit_amount = None
        self._back_payment_order_link = None
        self._discrepancy_type = None

    @property
    def actual_debit_amount(self):
        return self._actual_debit_amount

    @actual_debit_amount.setter
    def actual_debit_amount(self, value):
        if isinstance(value, IndrMoneyDTO):
            self._actual_debit_amount = value
        else:
            self._actual_debit_amount = IndrMoneyDTO.from_alipay_dict(value)
    @property
    def back_payment_order_link(self):
        return self._back_payment_order_link

    @back_payment_order_link.setter
    def back_payment_order_link(self, value):
        self._back_payment_order_link = value
    @property
    def discrepancy_type(self):
        return self._discrepancy_type

    @discrepancy_type.setter
    def discrepancy_type(self, value):
        self._discrepancy_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_debit_amount:
            if hasattr(self.actual_debit_amount, 'to_alipay_dict'):
                params['actual_debit_amount'] = self.actual_debit_amount.to_alipay_dict()
            else:
                params['actual_debit_amount'] = self.actual_debit_amount
        if self.back_payment_order_link:
            if hasattr(self.back_payment_order_link, 'to_alipay_dict'):
                params['back_payment_order_link'] = self.back_payment_order_link.to_alipay_dict()
            else:
                params['back_payment_order_link'] = self.back_payment_order_link
        if self.discrepancy_type:
            if hasattr(self.discrepancy_type, 'to_alipay_dict'):
                params['discrepancy_type'] = self.discrepancy_type.to_alipay_dict()
            else:
                params['discrepancy_type'] = self.discrepancy_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrPoboDebitRecordDTO()
        if 'actual_debit_amount' in d:
            o.actual_debit_amount = d['actual_debit_amount']
        if 'back_payment_order_link' in d:
            o.back_payment_order_link = d['back_payment_order_link']
        if 'discrepancy_type' in d:
            o.discrepancy_type = d['discrepancy_type']
        return o


