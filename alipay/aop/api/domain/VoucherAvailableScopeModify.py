#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderVoucherAvailableShopModify import OrderVoucherAvailableShopModify


class VoucherAvailableScopeModify(object):

    def __init__(self):
        self._order_voucher_available_shop = None

    @property
    def order_voucher_available_shop(self):
        return self._order_voucher_available_shop

    @order_voucher_available_shop.setter
    def order_voucher_available_shop(self, value):
        if isinstance(value, OrderVoucherAvailableShopModify):
            self._order_voucher_available_shop = value
        else:
            self._order_voucher_available_shop = OrderVoucherAvailableShopModify.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.order_voucher_available_shop:
            if hasattr(self.order_voucher_available_shop, 'to_alipay_dict'):
                params['order_voucher_available_shop'] = self.order_voucher_available_shop.to_alipay_dict()
            else:
                params['order_voucher_available_shop'] = self.order_voucher_available_shop
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableScopeModify()
        if 'order_voucher_available_shop' in d:
            o.order_voucher_available_shop = d['order_voucher_available_shop']
        return o


