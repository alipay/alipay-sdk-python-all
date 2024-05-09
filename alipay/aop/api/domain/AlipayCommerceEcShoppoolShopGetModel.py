#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcShoppoolShopGetModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._shop_group_id = None
        self._shop_id_list = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def shop_group_id(self):
        return self._shop_group_id

    @shop_group_id.setter
    def shop_group_id(self, value):
        self._shop_group_id = value
    @property
    def shop_id_list(self):
        return self._shop_id_list

    @shop_id_list.setter
    def shop_id_list(self, value):
        if isinstance(value, list):
            self._shop_id_list = list()
            for i in value:
                self._shop_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.shop_group_id:
            if hasattr(self.shop_group_id, 'to_alipay_dict'):
                params['shop_group_id'] = self.shop_group_id.to_alipay_dict()
            else:
                params['shop_group_id'] = self.shop_group_id
        if self.shop_id_list:
            if isinstance(self.shop_id_list, list):
                for i in range(0, len(self.shop_id_list)):
                    element = self.shop_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_id_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_id_list, 'to_alipay_dict'):
                params['shop_id_list'] = self.shop_id_list.to_alipay_dict()
            else:
                params['shop_id_list'] = self.shop_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcShoppoolShopGetModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'shop_group_id' in d:
            o.shop_group_id = d['shop_group_id']
        if 'shop_id_list' in d:
            o.shop_id_list = d['shop_id_list']
        return o


