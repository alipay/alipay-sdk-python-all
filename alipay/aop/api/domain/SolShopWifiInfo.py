#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SolWifiInfo import SolWifiInfo


class SolShopWifiInfo(object):

    def __init__(self):
        self._shop_id = None
        self._wifi_list = None

    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def wifi_list(self):
        return self._wifi_list

    @wifi_list.setter
    def wifi_list(self, value):
        if isinstance(value, list):
            self._wifi_list = list()
            for i in value:
                if isinstance(i, SolWifiInfo):
                    self._wifi_list.append(i)
                else:
                    self._wifi_list.append(SolWifiInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.wifi_list:
            if isinstance(self.wifi_list, list):
                for i in range(0, len(self.wifi_list)):
                    element = self.wifi_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.wifi_list[i] = element.to_alipay_dict()
            if hasattr(self.wifi_list, 'to_alipay_dict'):
                params['wifi_list'] = self.wifi_list.to_alipay_dict()
            else:
                params['wifi_list'] = self.wifi_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SolShopWifiInfo()
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'wifi_list' in d:
            o.wifi_list = d['wifi_list']
        return o


