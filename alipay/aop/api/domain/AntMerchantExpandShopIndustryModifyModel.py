#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantShopIndustryInfo import MerchantShopIndustryInfo


class AntMerchantExpandShopIndustryModifyModel(object):

    def __init__(self):
        self._industry_info = None
        self._ip_role_id = None
        self._shop_id = None
        self._store_id = None

    @property
    def industry_info(self):
        return self._industry_info

    @industry_info.setter
    def industry_info(self, value):
        if isinstance(value, list):
            self._industry_info = list()
            for i in value:
                if isinstance(i, MerchantShopIndustryInfo):
                    self._industry_info.append(i)
                else:
                    self._industry_info.append(MerchantShopIndustryInfo.from_alipay_dict(i))
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.industry_info:
            if isinstance(self.industry_info, list):
                for i in range(0, len(self.industry_info)):
                    element = self.industry_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.industry_info[i] = element.to_alipay_dict()
            if hasattr(self.industry_info, 'to_alipay_dict'):
                params['industry_info'] = self.industry_info.to_alipay_dict()
            else:
                params['industry_info'] = self.industry_info
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandShopIndustryModifyModel()
        if 'industry_info' in d:
            o.industry_info = d['industry_info']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


