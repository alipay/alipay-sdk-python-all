#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherAvailableGeographyAllShopInfo(object):

    def __init__(self):
        self._available_brand_id = None
        self._exclude_shop_ids = None
        self._merchant_ids = None

    @property
    def available_brand_id(self):
        return self._available_brand_id

    @available_brand_id.setter
    def available_brand_id(self, value):
        self._available_brand_id = value
    @property
    def exclude_shop_ids(self):
        return self._exclude_shop_ids

    @exclude_shop_ids.setter
    def exclude_shop_ids(self, value):
        if isinstance(value, list):
            self._exclude_shop_ids = list()
            for i in value:
                self._exclude_shop_ids.append(i)
    @property
    def merchant_ids(self):
        return self._merchant_ids

    @merchant_ids.setter
    def merchant_ids(self, value):
        if isinstance(value, list):
            self._merchant_ids = list()
            for i in value:
                self._merchant_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.available_brand_id:
            if hasattr(self.available_brand_id, 'to_alipay_dict'):
                params['available_brand_id'] = self.available_brand_id.to_alipay_dict()
            else:
                params['available_brand_id'] = self.available_brand_id
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
        if self.merchant_ids:
            if isinstance(self.merchant_ids, list):
                for i in range(0, len(self.merchant_ids)):
                    element = self.merchant_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_ids[i] = element.to_alipay_dict()
            if hasattr(self.merchant_ids, 'to_alipay_dict'):
                params['merchant_ids'] = self.merchant_ids.to_alipay_dict()
            else:
                params['merchant_ids'] = self.merchant_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableGeographyAllShopInfo()
        if 'available_brand_id' in d:
            o.available_brand_id = d['available_brand_id']
        if 'exclude_shop_ids' in d:
            o.exclude_shop_ids = d['exclude_shop_ids']
        if 'merchant_ids' in d:
            o.merchant_ids = d['merchant_ids']
        return o


