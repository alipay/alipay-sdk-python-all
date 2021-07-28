#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RepayTradeDetail import RepayTradeDetail


class AlipayTradeRepaybillCreateModel(object):

    def __init__(self):
        self._bill_amount = None
        self._bill_product = None
        self._out_bill_no = None
        self._repay_expire_date = None
        self._repay_trade_details = None
        self._user_id = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_product(self):
        return self._bill_product

    @bill_product.setter
    def bill_product(self, value):
        self._bill_product = value
    @property
    def out_bill_no(self):
        return self._out_bill_no

    @out_bill_no.setter
    def out_bill_no(self, value):
        self._out_bill_no = value
    @property
    def repay_expire_date(self):
        return self._repay_expire_date

    @repay_expire_date.setter
    def repay_expire_date(self, value):
        self._repay_expire_date = value
    @property
    def repay_trade_details(self):
        return self._repay_trade_details

    @repay_trade_details.setter
    def repay_trade_details(self, value):
        if isinstance(value, list):
            self._repay_trade_details = list()
            for i in value:
                if isinstance(i, RepayTradeDetail):
                    self._repay_trade_details.append(i)
                else:
                    self._repay_trade_details.append(RepayTradeDetail.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.bill_product:
            if hasattr(self.bill_product, 'to_alipay_dict'):
                params['bill_product'] = self.bill_product.to_alipay_dict()
            else:
                params['bill_product'] = self.bill_product
        if self.out_bill_no:
            if hasattr(self.out_bill_no, 'to_alipay_dict'):
                params['out_bill_no'] = self.out_bill_no.to_alipay_dict()
            else:
                params['out_bill_no'] = self.out_bill_no
        if self.repay_expire_date:
            if hasattr(self.repay_expire_date, 'to_alipay_dict'):
                params['repay_expire_date'] = self.repay_expire_date.to_alipay_dict()
            else:
                params['repay_expire_date'] = self.repay_expire_date
        if self.repay_trade_details:
            if isinstance(self.repay_trade_details, list):
                for i in range(0, len(self.repay_trade_details)):
                    element = self.repay_trade_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repay_trade_details[i] = element.to_alipay_dict()
            if hasattr(self.repay_trade_details, 'to_alipay_dict'):
                params['repay_trade_details'] = self.repay_trade_details.to_alipay_dict()
            else:
                params['repay_trade_details'] = self.repay_trade_details
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeRepaybillCreateModel()
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_product' in d:
            o.bill_product = d['bill_product']
        if 'out_bill_no' in d:
            o.out_bill_no = d['out_bill_no']
        if 'repay_expire_date' in d:
            o.repay_expire_date = d['repay_expire_date']
        if 'repay_trade_details' in d:
            o.repay_trade_details = d['repay_trade_details']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


