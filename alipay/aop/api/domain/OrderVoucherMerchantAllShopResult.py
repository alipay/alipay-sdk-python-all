#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderVoucherShopFailInfo import OrderVoucherShopFailInfo


class OrderVoucherMerchantAllShopResult(object):

    def __init__(self):
        self._exclude_shop_fail_infos = None
        self._success_exclude_shop_ids = None

    @property
    def exclude_shop_fail_infos(self):
        return self._exclude_shop_fail_infos

    @exclude_shop_fail_infos.setter
    def exclude_shop_fail_infos(self, value):
        if isinstance(value, list):
            self._exclude_shop_fail_infos = list()
            for i in value:
                if isinstance(i, OrderVoucherShopFailInfo):
                    self._exclude_shop_fail_infos.append(i)
                else:
                    self._exclude_shop_fail_infos.append(OrderVoucherShopFailInfo.from_alipay_dict(i))
    @property
    def success_exclude_shop_ids(self):
        return self._success_exclude_shop_ids

    @success_exclude_shop_ids.setter
    def success_exclude_shop_ids(self, value):
        if isinstance(value, list):
            self._success_exclude_shop_ids = list()
            for i in value:
                self._success_exclude_shop_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.exclude_shop_fail_infos:
            if isinstance(self.exclude_shop_fail_infos, list):
                for i in range(0, len(self.exclude_shop_fail_infos)):
                    element = self.exclude_shop_fail_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exclude_shop_fail_infos[i] = element.to_alipay_dict()
            if hasattr(self.exclude_shop_fail_infos, 'to_alipay_dict'):
                params['exclude_shop_fail_infos'] = self.exclude_shop_fail_infos.to_alipay_dict()
            else:
                params['exclude_shop_fail_infos'] = self.exclude_shop_fail_infos
        if self.success_exclude_shop_ids:
            if isinstance(self.success_exclude_shop_ids, list):
                for i in range(0, len(self.success_exclude_shop_ids)):
                    element = self.success_exclude_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.success_exclude_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.success_exclude_shop_ids, 'to_alipay_dict'):
                params['success_exclude_shop_ids'] = self.success_exclude_shop_ids.to_alipay_dict()
            else:
                params['success_exclude_shop_ids'] = self.success_exclude_shop_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderVoucherMerchantAllShopResult()
        if 'exclude_shop_fail_infos' in d:
            o.exclude_shop_fail_infos = d['exclude_shop_fail_infos']
        if 'success_exclude_shop_ids' in d:
            o.success_exclude_shop_ids = d['success_exclude_shop_ids']
        return o


