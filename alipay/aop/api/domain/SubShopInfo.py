#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Shop import Shop


class SubShopInfo(object):

    def __init__(self):
        self._shop_list = None

    @property
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        if isinstance(value, list):
            self._shop_list = list()
            for i in value:
                if isinstance(i, Shop):
                    self._shop_list.append(i)
                else:
                    self._shop_list.append(Shop.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubShopInfo()
        if 'shop_list' in d:
            o.shop_list = d['shop_list']
        return o


