#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingPassShopBindModel(object):

    def __init__(self):
        self._is_appending = None
        self._shop_list = None
        self._tpl_id = None

    @property
    def is_appending(self):
        return self._is_appending

    @is_appending.setter
    def is_appending(self, value):
        self._is_appending = value
    @property
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        if isinstance(value, list):
            self._shop_list = list()
            for i in value:
                self._shop_list.append(i)
    @property
    def tpl_id(self):
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, value):
        self._tpl_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_appending:
            if hasattr(self.is_appending, 'to_alipay_dict'):
                params['is_appending'] = self.is_appending.to_alipay_dict()
            else:
                params['is_appending'] = self.is_appending
        if self.shop_list:
            if isinstance(self.shop_list, list):
                for i in range(0, len(self.shop_list)):
                    element = self.shop_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_list, 'to_alipay_dict'):
                params['shop_list'] = self.shop_list.to_alipay_dict()
            else:
                params['shop_list'] = self.shop_list
        if self.tpl_id:
            if hasattr(self.tpl_id, 'to_alipay_dict'):
                params['tpl_id'] = self.tpl_id.to_alipay_dict()
            else:
                params['tpl_id'] = self.tpl_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingPassShopBindModel()
        if 'is_appending' in d:
            o.is_appending = d['is_appending']
        if 'shop_list' in d:
            o.shop_list = d['shop_list']
        if 'tpl_id' in d:
            o.tpl_id = d['tpl_id']
        return o


