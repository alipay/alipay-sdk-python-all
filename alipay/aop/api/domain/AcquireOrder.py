#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReferenceId import ReferenceId
from alipay.aop.api.domain.PaymentGoods import PaymentGoods
from alipay.aop.api.domain.ReferenceId import ReferenceId
from alipay.aop.api.domain.Shipping import Shipping


class AcquireOrder(object):

    def __init__(self):
        self._buyer_out_member_id = None
        self._goods = None
        self._order_amount = None
        self._order_create_time = None
        self._order_currency = None
        self._order_expiry_time = None
        self._out_order_id = None
        self._remark = None
        self._seller_out_member_id = None
        self._shipping = None

    @property
    def buyer_out_member_id(self):
        return self._buyer_out_member_id

    @buyer_out_member_id.setter
    def buyer_out_member_id(self, value):
        if isinstance(value, ReferenceId):
            self._buyer_out_member_id = value
        else:
            self._buyer_out_member_id = ReferenceId.from_alipay_dict(value)
    @property
    def goods(self):
        return self._goods

    @goods.setter
    def goods(self, value):
        if isinstance(value, list):
            self._goods = list()
            for i in value:
                if isinstance(i, PaymentGoods):
                    self._goods.append(i)
                else:
                    self._goods.append(PaymentGoods.from_alipay_dict(i))
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_currency(self):
        return self._order_currency

    @order_currency.setter
    def order_currency(self, value):
        self._order_currency = value
    @property
    def order_expiry_time(self):
        return self._order_expiry_time

    @order_expiry_time.setter
    def order_expiry_time(self, value):
        self._order_expiry_time = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def seller_out_member_id(self):
        return self._seller_out_member_id

    @seller_out_member_id.setter
    def seller_out_member_id(self, value):
        if isinstance(value, ReferenceId):
            self._seller_out_member_id = value
        else:
            self._seller_out_member_id = ReferenceId.from_alipay_dict(value)
    @property
    def shipping(self):
        return self._shipping

    @shipping.setter
    def shipping(self, value):
        if isinstance(value, Shipping):
            self._shipping = value
        else:
            self._shipping = Shipping.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_out_member_id:
            if hasattr(self.buyer_out_member_id, 'to_alipay_dict'):
                params['buyer_out_member_id'] = self.buyer_out_member_id.to_alipay_dict()
            else:
                params['buyer_out_member_id'] = self.buyer_out_member_id
        if self.goods:
            if isinstance(self.goods, list):
                for i in range(0, len(self.goods)):
                    element = self.goods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods[i] = element.to_alipay_dict()
            if hasattr(self.goods, 'to_alipay_dict'):
                params['goods'] = self.goods.to_alipay_dict()
            else:
                params['goods'] = self.goods
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_currency:
            if hasattr(self.order_currency, 'to_alipay_dict'):
                params['order_currency'] = self.order_currency.to_alipay_dict()
            else:
                params['order_currency'] = self.order_currency
        if self.order_expiry_time:
            if hasattr(self.order_expiry_time, 'to_alipay_dict'):
                params['order_expiry_time'] = self.order_expiry_time.to_alipay_dict()
            else:
                params['order_expiry_time'] = self.order_expiry_time
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.seller_out_member_id:
            if hasattr(self.seller_out_member_id, 'to_alipay_dict'):
                params['seller_out_member_id'] = self.seller_out_member_id.to_alipay_dict()
            else:
                params['seller_out_member_id'] = self.seller_out_member_id
        if self.shipping:
            if hasattr(self.shipping, 'to_alipay_dict'):
                params['shipping'] = self.shipping.to_alipay_dict()
            else:
                params['shipping'] = self.shipping
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AcquireOrder()
        if 'buyer_out_member_id' in d:
            o.buyer_out_member_id = d['buyer_out_member_id']
        if 'goods' in d:
            o.goods = d['goods']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_currency' in d:
            o.order_currency = d['order_currency']
        if 'order_expiry_time' in d:
            o.order_expiry_time = d['order_expiry_time']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'remark' in d:
            o.remark = d['remark']
        if 'seller_out_member_id' in d:
            o.seller_out_member_id = d['seller_out_member_id']
        if 'shipping' in d:
            o.shipping = d['shipping']
        return o


