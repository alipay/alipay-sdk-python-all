#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SolWifiShopInfo import SolWifiShopInfo


class AlipayCommerceCityfacilitatorWifiShopBatchcreateModel(object):

    def __init__(self):
        self._shop_info_list = None

    @property
    def shop_info_list(self):
        return self._shop_info_list

    @shop_info_list.setter
    def shop_info_list(self, value):
        if isinstance(value, list):
            self._shop_info_list = list()
            for i in value:
                if isinstance(i, SolWifiShopInfo):
                    self._shop_info_list.append(i)
                else:
                    self._shop_info_list.append(SolWifiShopInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.shop_info_list:
            if isinstance(self.shop_info_list, list):
                for i in range(0, len(self.shop_info_list)):
                    element = self.shop_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_info_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_info_list, 'to_alipay_dict'):
                params['shop_info_list'] = self.shop_info_list.to_alipay_dict()
            else:
                params['shop_info_list'] = self.shop_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorWifiShopBatchcreateModel()
        if 'shop_info_list' in d:
            o.shop_info_list = d['shop_info_list']
        return o


