#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentProcurementPayItemInfoVO import RentProcurementPayItemInfoVO
from alipay.aop.api.domain.RentProcurementPayItemInfoVO import RentProcurementPayItemInfoVO


class RentProcurementRefundInfoVO(object):

    def __init__(self):
        self._pay_items = None
        self._refund_amount = None
        self._refund_items = None

    @property
    def pay_items(self):
        return self._pay_items

    @pay_items.setter
    def pay_items(self, value):
        if isinstance(value, list):
            self._pay_items = list()
            for i in value:
                if isinstance(i, RentProcurementPayItemInfoVO):
                    self._pay_items.append(i)
                else:
                    self._pay_items.append(RentProcurementPayItemInfoVO.from_alipay_dict(i))
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_items(self):
        return self._refund_items

    @refund_items.setter
    def refund_items(self, value):
        if isinstance(value, list):
            self._refund_items = list()
            for i in value:
                if isinstance(i, RentProcurementPayItemInfoVO):
                    self._refund_items.append(i)
                else:
                    self._refund_items.append(RentProcurementPayItemInfoVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.pay_items:
            if isinstance(self.pay_items, list):
                for i in range(0, len(self.pay_items)):
                    element = self.pay_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_items[i] = element.to_alipay_dict()
            if hasattr(self.pay_items, 'to_alipay_dict'):
                params['pay_items'] = self.pay_items.to_alipay_dict()
            else:
                params['pay_items'] = self.pay_items
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_items:
            if isinstance(self.refund_items, list):
                for i in range(0, len(self.refund_items)):
                    element = self.refund_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_items[i] = element.to_alipay_dict()
            if hasattr(self.refund_items, 'to_alipay_dict'):
                params['refund_items'] = self.refund_items.to_alipay_dict()
            else:
                params['refund_items'] = self.refund_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentProcurementRefundInfoVO()
        if 'pay_items' in d:
            o.pay_items = d['pay_items']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_items' in d:
            o.refund_items = d['refund_items']
        return o


