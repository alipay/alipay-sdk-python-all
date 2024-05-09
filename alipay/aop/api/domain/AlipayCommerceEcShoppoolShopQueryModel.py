#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdressInfo import AdressInfo
from alipay.aop.api.domain.ConditionInfo import ConditionInfo
from alipay.aop.api.domain.FenceInfo import FenceInfo


class AlipayCommerceEcShoppoolShopQueryModel(object):

    def __init__(self):
        self._address_info = None
        self._condition_list = None
        self._enterprise_id = None
        self._fence_info = None
        self._shop_type = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, AdressInfo):
            self._address_info = value
        else:
            self._address_info = AdressInfo.from_alipay_dict(value)
    @property
    def condition_list(self):
        return self._condition_list

    @condition_list.setter
    def condition_list(self, value):
        if isinstance(value, list):
            self._condition_list = list()
            for i in value:
                if isinstance(i, ConditionInfo):
                    self._condition_list.append(i)
                else:
                    self._condition_list.append(ConditionInfo.from_alipay_dict(i))
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def fence_info(self):
        return self._fence_info

    @fence_info.setter
    def fence_info(self, value):
        if isinstance(value, FenceInfo):
            self._fence_info = value
        else:
            self._fence_info = FenceInfo.from_alipay_dict(value)
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.condition_list:
            if isinstance(self.condition_list, list):
                for i in range(0, len(self.condition_list)):
                    element = self.condition_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.condition_list[i] = element.to_alipay_dict()
            if hasattr(self.condition_list, 'to_alipay_dict'):
                params['condition_list'] = self.condition_list.to_alipay_dict()
            else:
                params['condition_list'] = self.condition_list
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.fence_info:
            if hasattr(self.fence_info, 'to_alipay_dict'):
                params['fence_info'] = self.fence_info.to_alipay_dict()
            else:
                params['fence_info'] = self.fence_info
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcShoppoolShopQueryModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'condition_list' in d:
            o.condition_list = d['condition_list']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'fence_info' in d:
            o.fence_info = d['fence_info']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        return o


