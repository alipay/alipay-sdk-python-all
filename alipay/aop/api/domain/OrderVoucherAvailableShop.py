#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderVoucherMerchantAllShop import OrderVoucherMerchantAllShop


class OrderVoucherAvailableShop(object):

    def __init__(self):
        self._order_voucher_merchant_all_shop = None
        self._real_shop_ids = None
        self._shop_ids = None

    @property
    def order_voucher_merchant_all_shop(self):
        return self._order_voucher_merchant_all_shop

    @order_voucher_merchant_all_shop.setter
    def order_voucher_merchant_all_shop(self, value):
        if isinstance(value, OrderVoucherMerchantAllShop):
            self._order_voucher_merchant_all_shop = value
        else:
            self._order_voucher_merchant_all_shop = OrderVoucherMerchantAllShop.from_alipay_dict(value)
    @property
    def real_shop_ids(self):
        return self._real_shop_ids

    @real_shop_ids.setter
    def real_shop_ids(self, value):
        if isinstance(value, list):
            self._real_shop_ids = list()
            for i in value:
                self._real_shop_ids.append(i)
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        if isinstance(value, list):
            self._shop_ids = list()
            for i in value:
                self._shop_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.order_voucher_merchant_all_shop:
            if hasattr(self.order_voucher_merchant_all_shop, 'to_alipay_dict'):
                params['order_voucher_merchant_all_shop'] = self.order_voucher_merchant_all_shop.to_alipay_dict()
            else:
                params['order_voucher_merchant_all_shop'] = self.order_voucher_merchant_all_shop
        if self.real_shop_ids:
            if isinstance(self.real_shop_ids, list):
                for i in range(0, len(self.real_shop_ids)):
                    element = self.real_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.real_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.real_shop_ids, 'to_alipay_dict'):
                params['real_shop_ids'] = self.real_shop_ids.to_alipay_dict()
            else:
                params['real_shop_ids'] = self.real_shop_ids
        if self.shop_ids:
            if isinstance(self.shop_ids, list):
                for i in range(0, len(self.shop_ids)):
                    element = self.shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_ids, 'to_alipay_dict'):
                params['shop_ids'] = self.shop_ids.to_alipay_dict()
            else:
                params['shop_ids'] = self.shop_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderVoucherAvailableShop()
        if 'order_voucher_merchant_all_shop' in d:
            o.order_voucher_merchant_all_shop = d['order_voucher_merchant_all_shop']
        if 'real_shop_ids' in d:
            o.real_shop_ids = d['real_shop_ids']
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        return o


