#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderVoucherMerchantAllShopModify(object):

    def __init__(self):
        self._exclude_shop_ids = None

    @property
    def exclude_shop_ids(self):
        return self._exclude_shop_ids

    @exclude_shop_ids.setter
    def exclude_shop_ids(self, value):
        if isinstance(value, list):
            self._exclude_shop_ids = list()
            for i in value:
                self._exclude_shop_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.exclude_shop_ids:
            if isinstance(self.exclude_shop_ids, list):
                for i in range(0, len(self.exclude_shop_ids)):
                    element = self.exclude_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exclude_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.exclude_shop_ids, 'to_alipay_dict'):
                params['exclude_shop_ids'] = self.exclude_shop_ids.to_alipay_dict()
            else:
                params['exclude_shop_ids'] = self.exclude_shop_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderVoucherMerchantAllShopModify()
        if 'exclude_shop_ids' in d:
            o.exclude_shop_ids = d['exclude_shop_ids']
        return o


