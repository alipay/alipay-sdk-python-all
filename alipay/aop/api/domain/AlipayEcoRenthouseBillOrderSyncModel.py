#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayEcoRenthouseBill import AlipayEcoRenthouseBill


class AlipayEcoRenthouseBillOrderSyncModel(object):

    def __init__(self):
        self._bill_number = None
        self._bills = None
        self._trade_id = None

    @property
    def bill_number(self):
        return self._bill_number

    @bill_number.setter
    def bill_number(self, value):
        self._bill_number = value
    @property
    def bills(self):
        return self._bills

    @bills.setter
    def bills(self, value):
        if isinstance(value, list):
            self._bills = list()
            for i in value:
                if isinstance(i, AlipayEcoRenthouseBill):
                    self._bills.append(i)
                else:
                    self._bills.append(AlipayEcoRenthouseBill.from_alipay_dict(i))
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_number:
            if hasattr(self.bill_number, 'to_alipay_dict'):
                params['bill_number'] = self.bill_number.to_alipay_dict()
            else:
                params['bill_number'] = self.bill_number
        if self.bills:
            if isinstance(self.bills, list):
                for i in range(0, len(self.bills)):
                    element = self.bills[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bills[i] = element.to_alipay_dict()
            if hasattr(self.bills, 'to_alipay_dict'):
                params['bills'] = self.bills.to_alipay_dict()
            else:
                params['bills'] = self.bills
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseBillOrderSyncModel()
        if 'bill_number' in d:
            o.bill_number = d['bill_number']
        if 'bills' in d:
            o.bills = d['bills']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        return o


