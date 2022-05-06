#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderVoucherAvailableCityCode import OrderVoucherAvailableCityCode
from alipay.aop.api.domain.OrderVoucherAvailableShop import OrderVoucherAvailableShop


class VoucherAvailableScope(object):

    def __init__(self):
        self._order_voucher_available_city_code = None
        self._order_voucher_available_shop = None
        self._voucher_available_type = None

    @property
    def order_voucher_available_city_code(self):
        return self._order_voucher_available_city_code

    @order_voucher_available_city_code.setter
    def order_voucher_available_city_code(self, value):
        if isinstance(value, OrderVoucherAvailableCityCode):
            self._order_voucher_available_city_code = value
        else:
            self._order_voucher_available_city_code = OrderVoucherAvailableCityCode.from_alipay_dict(value)
    @property
    def order_voucher_available_shop(self):
        return self._order_voucher_available_shop

    @order_voucher_available_shop.setter
    def order_voucher_available_shop(self, value):
        if isinstance(value, OrderVoucherAvailableShop):
            self._order_voucher_available_shop = value
        else:
            self._order_voucher_available_shop = OrderVoucherAvailableShop.from_alipay_dict(value)
    @property
    def voucher_available_type(self):
        return self._voucher_available_type

    @voucher_available_type.setter
    def voucher_available_type(self, value):
        self._voucher_available_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_voucher_available_city_code:
            if hasattr(self.order_voucher_available_city_code, 'to_alipay_dict'):
                params['order_voucher_available_city_code'] = self.order_voucher_available_city_code.to_alipay_dict()
            else:
                params['order_voucher_available_city_code'] = self.order_voucher_available_city_code
        if self.order_voucher_available_shop:
            if hasattr(self.order_voucher_available_shop, 'to_alipay_dict'):
                params['order_voucher_available_shop'] = self.order_voucher_available_shop.to_alipay_dict()
            else:
                params['order_voucher_available_shop'] = self.order_voucher_available_shop
        if self.voucher_available_type:
            if hasattr(self.voucher_available_type, 'to_alipay_dict'):
                params['voucher_available_type'] = self.voucher_available_type.to_alipay_dict()
            else:
                params['voucher_available_type'] = self.voucher_available_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableScope()
        if 'order_voucher_available_city_code' in d:
            o.order_voucher_available_city_code = d['order_voucher_available_city_code']
        if 'order_voucher_available_shop' in d:
            o.order_voucher_available_shop = d['order_voucher_available_shop']
        if 'voucher_available_type' in d:
            o.voucher_available_type = d['voucher_available_type']
        return o


