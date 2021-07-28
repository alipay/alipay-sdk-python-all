#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettlementBillCreateOrder import SettlementBillCreateOrder


class AlipayBossFncSettleSettlementbillCreateModel(object):

    def __init__(self):
        self._settlement_bill_create_order = None

    @property
    def settlement_bill_create_order(self):
        return self._settlement_bill_create_order

    @settlement_bill_create_order.setter
    def settlement_bill_create_order(self, value):
        if isinstance(value, list):
            self._settlement_bill_create_order = list()
            for i in value:
                if isinstance(i, SettlementBillCreateOrder):
                    self._settlement_bill_create_order.append(i)
                else:
                    self._settlement_bill_create_order.append(SettlementBillCreateOrder.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.settlement_bill_create_order:
            if isinstance(self.settlement_bill_create_order, list):
                for i in range(0, len(self.settlement_bill_create_order)):
                    element = self.settlement_bill_create_order[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settlement_bill_create_order[i] = element.to_alipay_dict()
            if hasattr(self.settlement_bill_create_order, 'to_alipay_dict'):
                params['settlement_bill_create_order'] = self.settlement_bill_create_order.to_alipay_dict()
            else:
                params['settlement_bill_create_order'] = self.settlement_bill_create_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncSettleSettlementbillCreateModel()
        if 'settlement_bill_create_order' in d:
            o.settlement_bill_create_order = d['settlement_bill_create_order']
        return o


