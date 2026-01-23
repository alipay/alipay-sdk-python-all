#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BillFeeItemReq import BillFeeItemReq


class OrderBillReq(object):

    def __init__(self):
        self._discount_amount = None
        self._fee_item_list = None
        self._pay_amount = None
        self._pay_time = None
        self._total_amount = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def fee_item_list(self):
        return self._fee_item_list

    @fee_item_list.setter
    def fee_item_list(self, value):
        if isinstance(value, list):
            self._fee_item_list = list()
            for i in value:
                if isinstance(i, BillFeeItemReq):
                    self._fee_item_list.append(i)
                else:
                    self._fee_item_list.append(BillFeeItemReq.from_alipay_dict(i))
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.fee_item_list:
            if isinstance(self.fee_item_list, list):
                for i in range(0, len(self.fee_item_list)):
                    element = self.fee_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fee_item_list[i] = element.to_alipay_dict()
            if hasattr(self.fee_item_list, 'to_alipay_dict'):
                params['fee_item_list'] = self.fee_item_list.to_alipay_dict()
            else:
                params['fee_item_list'] = self.fee_item_list
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderBillReq()
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'fee_item_list' in d:
            o.fee_item_list = d['fee_item_list']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


