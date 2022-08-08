#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherAvailableGeographyCityInfo import VoucherAvailableGeographyCityInfo
from alipay.aop.api.domain.VoucherAvailableGeographyShopInfo import VoucherAvailableGeographyShopInfo


class VoucherAvailableGeographyScopeInfo(object):

    def __init__(self):
        self._available_geography_city_info = None
        self._available_geography_scope_type = None
        self._available_geography_shop_info = None

    @property
    def available_geography_city_info(self):
        return self._available_geography_city_info

    @available_geography_city_info.setter
    def available_geography_city_info(self, value):
        if isinstance(value, VoucherAvailableGeographyCityInfo):
            self._available_geography_city_info = value
        else:
            self._available_geography_city_info = VoucherAvailableGeographyCityInfo.from_alipay_dict(value)
    @property
    def available_geography_scope_type(self):
        return self._available_geography_scope_type

    @available_geography_scope_type.setter
    def available_geography_scope_type(self, value):
        self._available_geography_scope_type = value
    @property
    def available_geography_shop_info(self):
        return self._available_geography_shop_info

    @available_geography_shop_info.setter
    def available_geography_shop_info(self, value):
        if isinstance(value, VoucherAvailableGeographyShopInfo):
            self._available_geography_shop_info = value
        else:
            self._available_geography_shop_info = VoucherAvailableGeographyShopInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.available_geography_city_info:
            if hasattr(self.available_geography_city_info, 'to_alipay_dict'):
                params['available_geography_city_info'] = self.available_geography_city_info.to_alipay_dict()
            else:
                params['available_geography_city_info'] = self.available_geography_city_info
        if self.available_geography_scope_type:
            if hasattr(self.available_geography_scope_type, 'to_alipay_dict'):
                params['available_geography_scope_type'] = self.available_geography_scope_type.to_alipay_dict()
            else:
                params['available_geography_scope_type'] = self.available_geography_scope_type
        if self.available_geography_shop_info:
            if hasattr(self.available_geography_shop_info, 'to_alipay_dict'):
                params['available_geography_shop_info'] = self.available_geography_shop_info.to_alipay_dict()
            else:
                params['available_geography_shop_info'] = self.available_geography_shop_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableGeographyScopeInfo()
        if 'available_geography_city_info' in d:
            o.available_geography_city_info = d['available_geography_city_info']
        if 'available_geography_scope_type' in d:
            o.available_geography_scope_type = d['available_geography_scope_type']
        if 'available_geography_shop_info' in d:
            o.available_geography_shop_info = d['available_geography_shop_info']
        return o


