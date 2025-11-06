#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertBillDetail(object):

    def __init__(self):
        self._certificate_id = None
        self._merchant_discount = None
        self._origin_price = None
        self._platform_discount = None
        self._real_pay = None
        self._sale_price = None
        self._settle_amount = None
        self._settle_time = None
        self._settle_type = None
        self._total_alloc_amount = None
        self._total_commission_amount = None
        self._trade_time = None
        self._use_shop_id = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def merchant_discount(self):
        return self._merchant_discount

    @merchant_discount.setter
    def merchant_discount(self, value):
        self._merchant_discount = value
    @property
    def origin_price(self):
        return self._origin_price

    @origin_price.setter
    def origin_price(self, value):
        self._origin_price = value
    @property
    def platform_discount(self):
        return self._platform_discount

    @platform_discount.setter
    def platform_discount(self, value):
        self._platform_discount = value
    @property
    def real_pay(self):
        return self._real_pay

    @real_pay.setter
    def real_pay(self, value):
        self._real_pay = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def settle_time(self):
        return self._settle_time

    @settle_time.setter
    def settle_time(self, value):
        self._settle_time = value
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value
    @property
    def total_alloc_amount(self):
        return self._total_alloc_amount

    @total_alloc_amount.setter
    def total_alloc_amount(self, value):
        self._total_alloc_amount = value
    @property
    def total_commission_amount(self):
        return self._total_commission_amount

    @total_commission_amount.setter
    def total_commission_amount(self, value):
        self._total_commission_amount = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value
    @property
    def use_shop_id(self):
        return self._use_shop_id

    @use_shop_id.setter
    def use_shop_id(self, value):
        self._use_shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.merchant_discount:
            if hasattr(self.merchant_discount, 'to_alipay_dict'):
                params['merchant_discount'] = self.merchant_discount.to_alipay_dict()
            else:
                params['merchant_discount'] = self.merchant_discount
        if self.origin_price:
            if hasattr(self.origin_price, 'to_alipay_dict'):
                params['origin_price'] = self.origin_price.to_alipay_dict()
            else:
                params['origin_price'] = self.origin_price
        if self.platform_discount:
            if hasattr(self.platform_discount, 'to_alipay_dict'):
                params['platform_discount'] = self.platform_discount.to_alipay_dict()
            else:
                params['platform_discount'] = self.platform_discount
        if self.real_pay:
            if hasattr(self.real_pay, 'to_alipay_dict'):
                params['real_pay'] = self.real_pay.to_alipay_dict()
            else:
                params['real_pay'] = self.real_pay
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.settle_time:
            if hasattr(self.settle_time, 'to_alipay_dict'):
                params['settle_time'] = self.settle_time.to_alipay_dict()
            else:
                params['settle_time'] = self.settle_time
        if self.settle_type:
            if hasattr(self.settle_type, 'to_alipay_dict'):
                params['settle_type'] = self.settle_type.to_alipay_dict()
            else:
                params['settle_type'] = self.settle_type
        if self.total_alloc_amount:
            if hasattr(self.total_alloc_amount, 'to_alipay_dict'):
                params['total_alloc_amount'] = self.total_alloc_amount.to_alipay_dict()
            else:
                params['total_alloc_amount'] = self.total_alloc_amount
        if self.total_commission_amount:
            if hasattr(self.total_commission_amount, 'to_alipay_dict'):
                params['total_commission_amount'] = self.total_commission_amount.to_alipay_dict()
            else:
                params['total_commission_amount'] = self.total_commission_amount
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        if self.use_shop_id:
            if hasattr(self.use_shop_id, 'to_alipay_dict'):
                params['use_shop_id'] = self.use_shop_id.to_alipay_dict()
            else:
                params['use_shop_id'] = self.use_shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertBillDetail()
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'merchant_discount' in d:
            o.merchant_discount = d['merchant_discount']
        if 'origin_price' in d:
            o.origin_price = d['origin_price']
        if 'platform_discount' in d:
            o.platform_discount = d['platform_discount']
        if 'real_pay' in d:
            o.real_pay = d['real_pay']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settle_time' in d:
            o.settle_time = d['settle_time']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        if 'total_alloc_amount' in d:
            o.total_alloc_amount = d['total_alloc_amount']
        if 'total_commission_amount' in d:
            o.total_commission_amount = d['total_commission_amount']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        if 'use_shop_id' in d:
            o.use_shop_id = d['use_shop_id']
        return o


