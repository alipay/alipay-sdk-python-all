#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderVoucherAvailableShopResult import OrderVoucherAvailableShopResult


class OrderVoucherAvailableScopeResult(object):

    def __init__(self):
        self._order_voucher_available_shop_result = None
        self._voucher_available_type = None

    @property
    def order_voucher_available_shop_result(self):
        return self._order_voucher_available_shop_result

    @order_voucher_available_shop_result.setter
    def order_voucher_available_shop_result(self, value):
        if isinstance(value, OrderVoucherAvailableShopResult):
            self._order_voucher_available_shop_result = value
        else:
            self._order_voucher_available_shop_result = OrderVoucherAvailableShopResult.from_alipay_dict(value)
    @property
    def voucher_available_type(self):
        return self._voucher_available_type

    @voucher_available_type.setter
    def voucher_available_type(self, value):
        self._voucher_available_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_voucher_available_shop_result:
            if hasattr(self.order_voucher_available_shop_result, 'to_alipay_dict'):
                params['order_voucher_available_shop_result'] = self.order_voucher_available_shop_result.to_alipay_dict()
            else:
                params['order_voucher_available_shop_result'] = self.order_voucher_available_shop_result
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
        o = OrderVoucherAvailableScopeResult()
        if 'order_voucher_available_shop_result' in d:
            o.order_voucher_available_shop_result = d['order_voucher_available_shop_result']
        if 'voucher_available_type' in d:
            o.voucher_available_type = d['voucher_available_type']
        return o


