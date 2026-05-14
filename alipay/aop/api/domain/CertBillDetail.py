#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertBillDetail(object):

    def __init__(self):
        self._alipay_verify_time = None
        self._certificate_id = None
        self._code = None
        self._et_settle_time = None
        self._item_id = None
        self._item_type = None
        self._m_item_id = None
        self._m_shop_id = None
        self._m_use_order_id = None
        self._merchant_discount = None
        self._net_income = None
        self._order_id = None
        self._origin_price = None
        self._platform_discount = None
        self._real_pay = None
        self._sale_price = None
        self._scene_name = None
        self._settle_account = None
        self._settle_amount = None
        self._settle_time = None
        self._settle_type = None
        self._status = None
        self._total_alloc_amount = None
        self._total_commission_amount = None
        self._trade_time = None
        self._use_shop_id = None
        self._use_shop_name = None
        self._verify_op = None
        self._verify_op_name = None
        self._verify_point_id = None
        self._verify_point_name = None
        self._verify_time = None

    @property
    def alipay_verify_time(self):
        return self._alipay_verify_time

    @alipay_verify_time.setter
    def alipay_verify_time(self, value):
        self._alipay_verify_time = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def et_settle_time(self):
        return self._et_settle_time

    @et_settle_time.setter
    def et_settle_time(self, value):
        self._et_settle_time = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def m_item_id(self):
        return self._m_item_id

    @m_item_id.setter
    def m_item_id(self, value):
        self._m_item_id = value
    @property
    def m_shop_id(self):
        return self._m_shop_id

    @m_shop_id.setter
    def m_shop_id(self, value):
        self._m_shop_id = value
    @property
    def m_use_order_id(self):
        return self._m_use_order_id

    @m_use_order_id.setter
    def m_use_order_id(self, value):
        self._m_use_order_id = value
    @property
    def merchant_discount(self):
        return self._merchant_discount

    @merchant_discount.setter
    def merchant_discount(self, value):
        self._merchant_discount = value
    @property
    def net_income(self):
        return self._net_income

    @net_income.setter
    def net_income(self, value):
        self._net_income = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
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
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value
    @property
    def settle_account(self):
        return self._settle_account

    @settle_account.setter
    def settle_account(self, value):
        self._settle_account = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
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
    @property
    def use_shop_name(self):
        return self._use_shop_name

    @use_shop_name.setter
    def use_shop_name(self, value):
        self._use_shop_name = value
    @property
    def verify_op(self):
        return self._verify_op

    @verify_op.setter
    def verify_op(self, value):
        self._verify_op = value
    @property
    def verify_op_name(self):
        return self._verify_op_name

    @verify_op_name.setter
    def verify_op_name(self, value):
        self._verify_op_name = value
    @property
    def verify_point_id(self):
        return self._verify_point_id

    @verify_point_id.setter
    def verify_point_id(self, value):
        self._verify_point_id = value
    @property
    def verify_point_name(self):
        return self._verify_point_name

    @verify_point_name.setter
    def verify_point_name(self, value):
        self._verify_point_name = value
    @property
    def verify_time(self):
        return self._verify_time

    @verify_time.setter
    def verify_time(self, value):
        self._verify_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_verify_time:
            if hasattr(self.alipay_verify_time, 'to_alipay_dict'):
                params['alipay_verify_time'] = self.alipay_verify_time.to_alipay_dict()
            else:
                params['alipay_verify_time'] = self.alipay_verify_time
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.et_settle_time:
            if hasattr(self.et_settle_time, 'to_alipay_dict'):
                params['et_settle_time'] = self.et_settle_time.to_alipay_dict()
            else:
                params['et_settle_time'] = self.et_settle_time
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.m_item_id:
            if hasattr(self.m_item_id, 'to_alipay_dict'):
                params['m_item_id'] = self.m_item_id.to_alipay_dict()
            else:
                params['m_item_id'] = self.m_item_id
        if self.m_shop_id:
            if hasattr(self.m_shop_id, 'to_alipay_dict'):
                params['m_shop_id'] = self.m_shop_id.to_alipay_dict()
            else:
                params['m_shop_id'] = self.m_shop_id
        if self.m_use_order_id:
            if hasattr(self.m_use_order_id, 'to_alipay_dict'):
                params['m_use_order_id'] = self.m_use_order_id.to_alipay_dict()
            else:
                params['m_use_order_id'] = self.m_use_order_id
        if self.merchant_discount:
            if hasattr(self.merchant_discount, 'to_alipay_dict'):
                params['merchant_discount'] = self.merchant_discount.to_alipay_dict()
            else:
                params['merchant_discount'] = self.merchant_discount
        if self.net_income:
            if hasattr(self.net_income, 'to_alipay_dict'):
                params['net_income'] = self.net_income.to_alipay_dict()
            else:
                params['net_income'] = self.net_income
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
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
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        if self.settle_account:
            if hasattr(self.settle_account, 'to_alipay_dict'):
                params['settle_account'] = self.settle_account.to_alipay_dict()
            else:
                params['settle_account'] = self.settle_account
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        if self.use_shop_name:
            if hasattr(self.use_shop_name, 'to_alipay_dict'):
                params['use_shop_name'] = self.use_shop_name.to_alipay_dict()
            else:
                params['use_shop_name'] = self.use_shop_name
        if self.verify_op:
            if hasattr(self.verify_op, 'to_alipay_dict'):
                params['verify_op'] = self.verify_op.to_alipay_dict()
            else:
                params['verify_op'] = self.verify_op
        if self.verify_op_name:
            if hasattr(self.verify_op_name, 'to_alipay_dict'):
                params['verify_op_name'] = self.verify_op_name.to_alipay_dict()
            else:
                params['verify_op_name'] = self.verify_op_name
        if self.verify_point_id:
            if hasattr(self.verify_point_id, 'to_alipay_dict'):
                params['verify_point_id'] = self.verify_point_id.to_alipay_dict()
            else:
                params['verify_point_id'] = self.verify_point_id
        if self.verify_point_name:
            if hasattr(self.verify_point_name, 'to_alipay_dict'):
                params['verify_point_name'] = self.verify_point_name.to_alipay_dict()
            else:
                params['verify_point_name'] = self.verify_point_name
        if self.verify_time:
            if hasattr(self.verify_time, 'to_alipay_dict'):
                params['verify_time'] = self.verify_time.to_alipay_dict()
            else:
                params['verify_time'] = self.verify_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertBillDetail()
        if 'alipay_verify_time' in d:
            o.alipay_verify_time = d['alipay_verify_time']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'code' in d:
            o.code = d['code']
        if 'et_settle_time' in d:
            o.et_settle_time = d['et_settle_time']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'm_item_id' in d:
            o.m_item_id = d['m_item_id']
        if 'm_shop_id' in d:
            o.m_shop_id = d['m_shop_id']
        if 'm_use_order_id' in d:
            o.m_use_order_id = d['m_use_order_id']
        if 'merchant_discount' in d:
            o.merchant_discount = d['merchant_discount']
        if 'net_income' in d:
            o.net_income = d['net_income']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'origin_price' in d:
            o.origin_price = d['origin_price']
        if 'platform_discount' in d:
            o.platform_discount = d['platform_discount']
        if 'real_pay' in d:
            o.real_pay = d['real_pay']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        if 'settle_account' in d:
            o.settle_account = d['settle_account']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settle_time' in d:
            o.settle_time = d['settle_time']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        if 'status' in d:
            o.status = d['status']
        if 'total_alloc_amount' in d:
            o.total_alloc_amount = d['total_alloc_amount']
        if 'total_commission_amount' in d:
            o.total_commission_amount = d['total_commission_amount']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        if 'use_shop_id' in d:
            o.use_shop_id = d['use_shop_id']
        if 'use_shop_name' in d:
            o.use_shop_name = d['use_shop_name']
        if 'verify_op' in d:
            o.verify_op = d['verify_op']
        if 'verify_op_name' in d:
            o.verify_op_name = d['verify_op_name']
        if 'verify_point_id' in d:
            o.verify_point_id = d['verify_point_id']
        if 'verify_point_name' in d:
            o.verify_point_name = d['verify_point_name']
        if 'verify_time' in d:
            o.verify_time = d['verify_time']
        return o


