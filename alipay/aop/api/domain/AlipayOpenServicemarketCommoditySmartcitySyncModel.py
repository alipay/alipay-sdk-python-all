#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommodityBaseInfo import CommodityBaseInfo
from alipay.aop.api.domain.SmartCityCommodityInfo import SmartCityCommodityInfo


class AlipayOpenServicemarketCommoditySmartcitySyncModel(object):

    def __init__(self):
        self._commodity_base_info = None
        self._commodity_id = None
        self._is_pre = None
        self._smart_city_commodity_info = None
        self._user_id = None

    @property
    def commodity_base_info(self):
        return self._commodity_base_info

    @commodity_base_info.setter
    def commodity_base_info(self, value):
        if isinstance(value, CommodityBaseInfo):
            self._commodity_base_info = value
        else:
            self._commodity_base_info = CommodityBaseInfo.from_alipay_dict(value)
    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def is_pre(self):
        return self._is_pre

    @is_pre.setter
    def is_pre(self, value):
        self._is_pre = value
    @property
    def smart_city_commodity_info(self):
        return self._smart_city_commodity_info

    @smart_city_commodity_info.setter
    def smart_city_commodity_info(self, value):
        if isinstance(value, SmartCityCommodityInfo):
            self._smart_city_commodity_info = value
        else:
            self._smart_city_commodity_info = SmartCityCommodityInfo.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_base_info:
            if hasattr(self.commodity_base_info, 'to_alipay_dict'):
                params['commodity_base_info'] = self.commodity_base_info.to_alipay_dict()
            else:
                params['commodity_base_info'] = self.commodity_base_info
        if self.commodity_id:
            if hasattr(self.commodity_id, 'to_alipay_dict'):
                params['commodity_id'] = self.commodity_id.to_alipay_dict()
            else:
                params['commodity_id'] = self.commodity_id
        if self.is_pre:
            if hasattr(self.is_pre, 'to_alipay_dict'):
                params['is_pre'] = self.is_pre.to_alipay_dict()
            else:
                params['is_pre'] = self.is_pre
        if self.smart_city_commodity_info:
            if hasattr(self.smart_city_commodity_info, 'to_alipay_dict'):
                params['smart_city_commodity_info'] = self.smart_city_commodity_info.to_alipay_dict()
            else:
                params['smart_city_commodity_info'] = self.smart_city_commodity_info
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenServicemarketCommoditySmartcitySyncModel()
        if 'commodity_base_info' in d:
            o.commodity_base_info = d['commodity_base_info']
        if 'commodity_id' in d:
            o.commodity_id = d['commodity_id']
        if 'is_pre' in d:
            o.is_pre = d['is_pre']
        if 'smart_city_commodity_info' in d:
            o.smart_city_commodity_info = d['smart_city_commodity_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


