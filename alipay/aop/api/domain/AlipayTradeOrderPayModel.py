#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BuyerPayDetail import BuyerPayDetail


class AlipayTradeOrderPayModel(object):

    def __init__(self):
        self._advance_payment_type = None
        self._buyer_id = None
        self._buyer_pay_detail = None
        self._fulfillment_amount = None
        self._is_async_pay = None
        self._order_pay_mode = None
        self._out_request_no = None
        self._product_code = None
        self._total_amount = None
        self._trade_no = None

    @property
    def advance_payment_type(self):
        return self._advance_payment_type

    @advance_payment_type.setter
    def advance_payment_type(self, value):
        self._advance_payment_type = value
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
    def fulfillment_amount(self):
        return self._fulfillment_amount

    @fulfillment_amount.setter
    def fulfillment_amount(self, value):
        self._fulfillment_amount = value
    @property
    def is_async_pay(self):
        return self._is_async_pay

    @is_async_pay.setter
    def is_async_pay(self, value):
        self._is_async_pay = value
    @property
    def order_pay_mode(self):
        return self._order_pay_mode

    @order_pay_mode.setter
    def order_pay_mode(self, value):
        self._order_pay_mode = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
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
        if self.advance_payment_type:
            if hasattr(self.advance_payment_type, 'to_alipay_dict'):
                params['advance_payment_type'] = self.advance_payment_type.to_alipay_dict()
            else:
                params['advance_payment_type'] = self.advance_payment_type
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
        if self.fulfillment_amount:
            if hasattr(self.fulfillment_amount, 'to_alipay_dict'):
                params['fulfillment_amount'] = self.fulfillment_amount.to_alipay_dict()
            else:
                params['fulfillment_amount'] = self.fulfillment_amount
        if self.is_async_pay:
            if hasattr(self.is_async_pay, 'to_alipay_dict'):
                params['is_async_pay'] = self.is_async_pay.to_alipay_dict()
            else:
                params['is_async_pay'] = self.is_async_pay
        if self.order_pay_mode:
            if hasattr(self.order_pay_mode, 'to_alipay_dict'):
                params['order_pay_mode'] = self.order_pay_mode.to_alipay_dict()
            else:
                params['order_pay_mode'] = self.order_pay_mode
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
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
        if 'advance_payment_type' in d:
            o.advance_payment_type = d['advance_payment_type']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_pay_detail' in d:
            o.buyer_pay_detail = d['buyer_pay_detail']
        if 'fulfillment_amount' in d:
            o.fulfillment_amount = d['fulfillment_amount']
        if 'is_async_pay' in d:
            o.is_async_pay = d['is_async_pay']
        if 'order_pay_mode' in d:
            o.order_pay_mode = d['order_pay_mode']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


