#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderVoucherAvailableCityCodeModify import OrderVoucherAvailableCityCodeModify
from alipay.aop.api.domain.OrderVoucherAvailableShopModify import OrderVoucherAvailableShopModify


class VoucherAvailableScopeModify(object):

    def __init__(self):
        self._modify_type = None
        self._order_voucher_available_city_code = None
        self._order_voucher_available_shop = None

    @property
    def modify_type(self):
        return self._modify_type

    @modify_type.setter
    def modify_type(self, value):
        self._modify_type = value
    @property
    def order_voucher_available_city_code(self):
        return self._order_voucher_available_city_code

    @order_voucher_available_city_code.setter
    def order_voucher_available_city_code(self, value):
        if isinstance(value, OrderVoucherAvailableCityCodeModify):
            self._order_voucher_available_city_code = value
        else:
            self._order_voucher_available_city_code = OrderVoucherAvailableCityCodeModify.from_alipay_dict(value)
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
        if self.modify_type:
            if hasattr(self.modify_type, 'to_alipay_dict'):
                params['modify_type'] = self.modify_type.to_alipay_dict()
            else:
                params['modify_type'] = self.modify_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableScopeModify()
        if 'modify_type' in d:
            o.modify_type = d['modify_type']
        if 'order_voucher_available_city_code' in d:
            o.order_voucher_available_city_code = d['order_voucher_available_city_code']
        if 'order_voucher_available_shop' in d:
            o.order_voucher_available_shop = d['order_voucher_available_shop']
        return o


