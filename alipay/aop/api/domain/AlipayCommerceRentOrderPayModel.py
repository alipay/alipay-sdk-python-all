#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentPayItemDTO import RentPayItemDTO
from alipay.aop.api.domain.RentSubMerchantDTO import RentSubMerchantDTO


class AlipayCommerceRentOrderPayModel(object):

    def __init__(self):
        self._aftersale_id = None
        self._order_id = None
        self._out_trade_no = None
        self._pay_amount = None
        self._pay_items = None
        self._pay_method = None
        self._pay_notify_url = None
        self._pay_timeout_express = None
        self._reason_code = None
        self._reason_desc = None
        self._sub_merchant = None

    @property
    def aftersale_id(self):
        return self._aftersale_id

    @aftersale_id.setter
    def aftersale_id(self, value):
        self._aftersale_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_items(self):
        return self._pay_items

    @pay_items.setter
    def pay_items(self, value):
        if isinstance(value, list):
            self._pay_items = list()
            for i in value:
                if isinstance(i, RentPayItemDTO):
                    self._pay_items.append(i)
                else:
                    self._pay_items.append(RentPayItemDTO.from_alipay_dict(i))
    @property
    def pay_method(self):
        return self._pay_method

    @pay_method.setter
    def pay_method(self, value):
        self._pay_method = value
    @property
    def pay_notify_url(self):
        return self._pay_notify_url

    @pay_notify_url.setter
    def pay_notify_url(self, value):
        self._pay_notify_url = value
    @property
    def pay_timeout_express(self):
        return self._pay_timeout_express

    @pay_timeout_express.setter
    def pay_timeout_express(self, value):
        self._pay_timeout_express = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def reason_desc(self):
        return self._reason_desc

    @reason_desc.setter
    def reason_desc(self, value):
        self._reason_desc = value
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, RentSubMerchantDTO):
            self._sub_merchant = value
        else:
            self._sub_merchant = RentSubMerchantDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.aftersale_id:
            if hasattr(self.aftersale_id, 'to_alipay_dict'):
                params['aftersale_id'] = self.aftersale_id.to_alipay_dict()
            else:
                params['aftersale_id'] = self.aftersale_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
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
        if self.pay_method:
            if hasattr(self.pay_method, 'to_alipay_dict'):
                params['pay_method'] = self.pay_method.to_alipay_dict()
            else:
                params['pay_method'] = self.pay_method
        if self.pay_notify_url:
            if hasattr(self.pay_notify_url, 'to_alipay_dict'):
                params['pay_notify_url'] = self.pay_notify_url.to_alipay_dict()
            else:
                params['pay_notify_url'] = self.pay_notify_url
        if self.pay_timeout_express:
            if hasattr(self.pay_timeout_express, 'to_alipay_dict'):
                params['pay_timeout_express'] = self.pay_timeout_express.to_alipay_dict()
            else:
                params['pay_timeout_express'] = self.pay_timeout_express
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        if self.reason_desc:
            if hasattr(self.reason_desc, 'to_alipay_dict'):
                params['reason_desc'] = self.reason_desc.to_alipay_dict()
            else:
                params['reason_desc'] = self.reason_desc
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderPayModel()
        if 'aftersale_id' in d:
            o.aftersale_id = d['aftersale_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_items' in d:
            o.pay_items = d['pay_items']
        if 'pay_method' in d:
            o.pay_method = d['pay_method']
        if 'pay_notify_url' in d:
            o.pay_notify_url = d['pay_notify_url']
        if 'pay_timeout_express' in d:
            o.pay_timeout_express = d['pay_timeout_express']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        if 'reason_desc' in d:
            o.reason_desc = d['reason_desc']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        return o


