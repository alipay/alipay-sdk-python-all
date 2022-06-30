#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderVoucherMerchantAllShopResult import OrderVoucherMerchantAllShopResult
from alipay.aop.api.domain.OrderVoucherRealShopFailInfo import OrderVoucherRealShopFailInfo
from alipay.aop.api.domain.OrderVoucherShopFailInfo import OrderVoucherShopFailInfo


class OrderVoucherAvailableShopResult(object):

    def __init__(self):
        self._order_voucher_merchant_all_shop_result = None
        self._real_shop_fail_infos = None
        self._shop_fail_infos = None
        self._success_real_shop_ids = None
        self._success_shop_ids = None

    @property
    def order_voucher_merchant_all_shop_result(self):
        return self._order_voucher_merchant_all_shop_result

    @order_voucher_merchant_all_shop_result.setter
    def order_voucher_merchant_all_shop_result(self, value):
        if isinstance(value, OrderVoucherMerchantAllShopResult):
            self._order_voucher_merchant_all_shop_result = value
        else:
            self._order_voucher_merchant_all_shop_result = OrderVoucherMerchantAllShopResult.from_alipay_dict(value)
    @property
    def real_shop_fail_infos(self):
        return self._real_shop_fail_infos

    @real_shop_fail_infos.setter
    def real_shop_fail_infos(self, value):
        if isinstance(value, list):
            self._real_shop_fail_infos = list()
            for i in value:
                if isinstance(i, OrderVoucherRealShopFailInfo):
                    self._real_shop_fail_infos.append(i)
                else:
                    self._real_shop_fail_infos.append(OrderVoucherRealShopFailInfo.from_alipay_dict(i))
    @property
    def shop_fail_infos(self):
        return self._shop_fail_infos

    @shop_fail_infos.setter
    def shop_fail_infos(self, value):
        if isinstance(value, list):
            self._shop_fail_infos = list()
            for i in value:
                if isinstance(i, OrderVoucherShopFailInfo):
                    self._shop_fail_infos.append(i)
                else:
                    self._shop_fail_infos.append(OrderVoucherShopFailInfo.from_alipay_dict(i))
    @property
    def success_real_shop_ids(self):
        return self._success_real_shop_ids

    @success_real_shop_ids.setter
    def success_real_shop_ids(self, value):
        if isinstance(value, list):
            self._success_real_shop_ids = list()
            for i in value:
                self._success_real_shop_ids.append(i)
    @property
    def success_shop_ids(self):
        return self._success_shop_ids

    @success_shop_ids.setter
    def success_shop_ids(self, value):
        if isinstance(value, list):
            self._success_shop_ids = list()
            for i in value:
                self._success_shop_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.order_voucher_merchant_all_shop_result:
            if hasattr(self.order_voucher_merchant_all_shop_result, 'to_alipay_dict'):
                params['order_voucher_merchant_all_shop_result'] = self.order_voucher_merchant_all_shop_result.to_alipay_dict()
            else:
                params['order_voucher_merchant_all_shop_result'] = self.order_voucher_merchant_all_shop_result
        if self.real_shop_fail_infos:
            if isinstance(self.real_shop_fail_infos, list):
                for i in range(0, len(self.real_shop_fail_infos)):
                    element = self.real_shop_fail_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.real_shop_fail_infos[i] = element.to_alipay_dict()
            if hasattr(self.real_shop_fail_infos, 'to_alipay_dict'):
                params['real_shop_fail_infos'] = self.real_shop_fail_infos.to_alipay_dict()
            else:
                params['real_shop_fail_infos'] = self.real_shop_fail_infos
        if self.shop_fail_infos:
            if isinstance(self.shop_fail_infos, list):
                for i in range(0, len(self.shop_fail_infos)):
                    element = self.shop_fail_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_fail_infos[i] = element.to_alipay_dict()
            if hasattr(self.shop_fail_infos, 'to_alipay_dict'):
                params['shop_fail_infos'] = self.shop_fail_infos.to_alipay_dict()
            else:
                params['shop_fail_infos'] = self.shop_fail_infos
        if self.success_real_shop_ids:
            if isinstance(self.success_real_shop_ids, list):
                for i in range(0, len(self.success_real_shop_ids)):
                    element = self.success_real_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.success_real_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.success_real_shop_ids, 'to_alipay_dict'):
                params['success_real_shop_ids'] = self.success_real_shop_ids.to_alipay_dict()
            else:
                params['success_real_shop_ids'] = self.success_real_shop_ids
        if self.success_shop_ids:
            if isinstance(self.success_shop_ids, list):
                for i in range(0, len(self.success_shop_ids)):
                    element = self.success_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.success_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.success_shop_ids, 'to_alipay_dict'):
                params['success_shop_ids'] = self.success_shop_ids.to_alipay_dict()
            else:
                params['success_shop_ids'] = self.success_shop_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderVoucherAvailableShopResult()
        if 'order_voucher_merchant_all_shop_result' in d:
            o.order_voucher_merchant_all_shop_result = d['order_voucher_merchant_all_shop_result']
        if 'real_shop_fail_infos' in d:
            o.real_shop_fail_infos = d['real_shop_fail_infos']
        if 'shop_fail_infos' in d:
            o.shop_fail_infos = d['shop_fail_infos']
        if 'success_real_shop_ids' in d:
            o.success_real_shop_ids = d['success_real_shop_ids']
        if 'success_shop_ids' in d:
            o.success_shop_ids = d['success_shop_ids']
        return o


