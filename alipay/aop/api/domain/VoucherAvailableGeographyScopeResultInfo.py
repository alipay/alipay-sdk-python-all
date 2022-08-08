#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherAvailableGeographyShopResultInfo import VoucherAvailableGeographyShopResultInfo


class VoucherAvailableGeographyScopeResultInfo(object):

    def __init__(self):
        self._available_geography_shop_result_info = None

    @property
    def available_geography_shop_result_info(self):
        return self._available_geography_shop_result_info

    @available_geography_shop_result_info.setter
    def available_geography_shop_result_info(self, value):
        if isinstance(value, VoucherAvailableGeographyShopResultInfo):
            self._available_geography_shop_result_info = value
        else:
            self._available_geography_shop_result_info = VoucherAvailableGeographyShopResultInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.available_geography_shop_result_info:
            if hasattr(self.available_geography_shop_result_info, 'to_alipay_dict'):
                params['available_geography_shop_result_info'] = self.available_geography_shop_result_info.to_alipay_dict()
            else:
                params['available_geography_shop_result_info'] = self.available_geography_shop_result_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableGeographyScopeResultInfo()
        if 'available_geography_shop_result_info' in d:
            o.available_geography_shop_result_info = d['available_geography_shop_result_info']
        return o


