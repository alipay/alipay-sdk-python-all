#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceOrderInfo(object):

    def __init__(self):
        self._amount = None
        self._category_code = None
        self._gmt_create = None
        self._gmt_modified = None
        self._gmt_payment = None
        self._gmt_refund = None
        self._memo = None
        self._out_service_id = None
        self._out_sku_id = None
        self._out_sp_id = None
        self._payment_amount = None
        self._price = None
        self._quantity = None
        self._real_amount = None
        self._refund_amount = None
        self._service_id = None
        self._service_order_no = None
        self._sku_id = None
        self._trade_no = None
        self._unit = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_service_id(self):
        return self._out_service_id

    @out_service_id.setter
    def out_service_id(self, value):
        self._out_service_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def out_sp_id(self):
        return self._out_sp_id

    @out_sp_id.setter
    def out_sp_id(self, value):
        if isinstance(value, list):
            self._out_sp_id = list()
            for i in value:
                self._out_sp_id.append(i)
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def service_order_no(self):
        return self._service_order_no

    @service_order_no.setter
    def service_order_no(self, value):
        self._service_order_no = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.gmt_payment:
            if hasattr(self.gmt_payment, 'to_alipay_dict'):
                params['gmt_payment'] = self.gmt_payment.to_alipay_dict()
            else:
                params['gmt_payment'] = self.gmt_payment
        if self.gmt_refund:
            if hasattr(self.gmt_refund, 'to_alipay_dict'):
                params['gmt_refund'] = self.gmt_refund.to_alipay_dict()
            else:
                params['gmt_refund'] = self.gmt_refund
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_service_id:
            if hasattr(self.out_service_id, 'to_alipay_dict'):
                params['out_service_id'] = self.out_service_id.to_alipay_dict()
            else:
                params['out_service_id'] = self.out_service_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.out_sp_id:
            if isinstance(self.out_sp_id, list):
                for i in range(0, len(self.out_sp_id)):
                    element = self.out_sp_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_sp_id[i] = element.to_alipay_dict()
            if hasattr(self.out_sp_id, 'to_alipay_dict'):
                params['out_sp_id'] = self.out_sp_id.to_alipay_dict()
            else:
                params['out_sp_id'] = self.out_sp_id
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.service_order_no:
            if hasattr(self.service_order_no, 'to_alipay_dict'):
                params['service_order_no'] = self.service_order_no.to_alipay_dict()
            else:
                params['service_order_no'] = self.service_order_no
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceOrderInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'gmt_payment' in d:
            o.gmt_payment = d['gmt_payment']
        if 'gmt_refund' in d:
            o.gmt_refund = d['gmt_refund']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_service_id' in d:
            o.out_service_id = d['out_service_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'out_sp_id' in d:
            o.out_sp_id = d['out_sp_id']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'service_order_no' in d:
            o.service_order_no = d['service_order_no']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'unit' in d:
            o.unit = d['unit']
        return o


