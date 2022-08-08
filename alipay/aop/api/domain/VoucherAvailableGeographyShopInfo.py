#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherAvailableGeographyAllShopInfo import VoucherAvailableGeographyAllShopInfo


class VoucherAvailableGeographyShopInfo(object):

    def __init__(self):
        self._available_geography_all_shop = None
        self._available_real_shop_ids = None
        self._available_shop_ids = None

    @property
    def available_geography_all_shop(self):
        return self._available_geography_all_shop

    @available_geography_all_shop.setter
    def available_geography_all_shop(self, value):
        if isinstance(value, VoucherAvailableGeographyAllShopInfo):
            self._available_geography_all_shop = value
        else:
            self._available_geography_all_shop = VoucherAvailableGeographyAllShopInfo.from_alipay_dict(value)
    @property
    def available_real_shop_ids(self):
        return self._available_real_shop_ids

    @available_real_shop_ids.setter
    def available_real_shop_ids(self, value):
        if isinstance(value, list):
            self._available_real_shop_ids = list()
            for i in value:
                self._available_real_shop_ids.append(i)
    @property
    def available_shop_ids(self):
        return self._available_shop_ids

    @available_shop_ids.setter
    def available_shop_ids(self, value):
        if isinstance(value, list):
            self._available_shop_ids = list()
            for i in value:
                self._available_shop_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.available_geography_all_shop:
            if hasattr(self.available_geography_all_shop, 'to_alipay_dict'):
                params['available_geography_all_shop'] = self.available_geography_all_shop.to_alipay_dict()
            else:
                params['available_geography_all_shop'] = self.available_geography_all_shop
        if self.available_real_shop_ids:
            if isinstance(self.available_real_shop_ids, list):
                for i in range(0, len(self.available_real_shop_ids)):
                    element = self.available_real_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_real_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.available_real_shop_ids, 'to_alipay_dict'):
                params['available_real_shop_ids'] = self.available_real_shop_ids.to_alipay_dict()
            else:
                params['available_real_shop_ids'] = self.available_real_shop_ids
        if self.available_shop_ids:
            if isinstance(self.available_shop_ids, list):
                for i in range(0, len(self.available_shop_ids)):
                    element = self.available_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.available_shop_ids, 'to_alipay_dict'):
                params['available_shop_ids'] = self.available_shop_ids.to_alipay_dict()
            else:
                params['available_shop_ids'] = self.available_shop_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableGeographyShopInfo()
        if 'available_geography_all_shop' in d:
            o.available_geography_all_shop = d['available_geography_all_shop']
        if 'available_real_shop_ids' in d:
            o.available_real_shop_ids = d['available_real_shop_ids']
        if 'available_shop_ids' in d:
            o.available_shop_ids = d['available_shop_ids']
        return o


