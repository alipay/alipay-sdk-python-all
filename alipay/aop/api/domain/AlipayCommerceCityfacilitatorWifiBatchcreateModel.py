#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SolShopWifiInfo import SolShopWifiInfo


class AlipayCommerceCityfacilitatorWifiBatchcreateModel(object):

    def __init__(self):
        self._shop_wifi_list = None

    @property
    def shop_wifi_list(self):
        return self._shop_wifi_list

    @shop_wifi_list.setter
    def shop_wifi_list(self, value):
        if isinstance(value, list):
            self._shop_wifi_list = list()
            for i in value:
                if isinstance(i, SolShopWifiInfo):
                    self._shop_wifi_list.append(i)
                else:
                    self._shop_wifi_list.append(SolShopWifiInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.shop_wifi_list:
            if isinstance(self.shop_wifi_list, list):
                for i in range(0, len(self.shop_wifi_list)):
                    element = self.shop_wifi_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_wifi_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_wifi_list, 'to_alipay_dict'):
                params['shop_wifi_list'] = self.shop_wifi_list.to_alipay_dict()
            else:
                params['shop_wifi_list'] = self.shop_wifi_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorWifiBatchcreateModel()
        if 'shop_wifi_list' in d:
            o.shop_wifi_list = d['shop_wifi_list']
        return o


