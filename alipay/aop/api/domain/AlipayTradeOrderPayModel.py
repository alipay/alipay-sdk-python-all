#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BuyerPayDetail import BuyerPayDetail


class AlipayTradeOrderPayModel(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_pay_detail = None
        self._product_code = None
        self._total_amount = None
        self._trade_no = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_pay_detail(self):
        return self._buyer_pay_detail

    @buyer_pay_detail.setter
    def buyer_pay_detail(self, value):
        if isinstance(value, list):
            self._buyer_pay_detail = list()
            for i in value:
                if isinstance(i, BuyerPayDetail):
                    self._buyer_pay_detail.append(i)
                else:
                    self._buyer_pay_detail.append(BuyerPayDetail.from_alipay_dict(i))
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_pay_detail:
            if isinstance(self.buyer_pay_detail, list):
                for i in range(0, len(self.buyer_pay_detail)):
                    element = self.buyer_pay_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.buyer_pay_detail[i] = element.to_alipay_dict()
            if hasattr(self.buyer_pay_detail, 'to_alipay_dict'):
                params['buyer_pay_detail'] = self.buyer_pay_detail.to_alipay_dict()
            else:
                params['buyer_pay_detail'] = self.buyer_pay_detail
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeOrderPayModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_pay_detail' in d:
            o.buyer_pay_detail = d['buyer_pay_detail']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


