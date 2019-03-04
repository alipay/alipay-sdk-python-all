#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopOrderConfigInfo import ShopOrderConfigInfo


class KoubeiCateringConfigModifyModel(object):

    def __init__(self):
        self._request_id = None
        self._shop_config_list = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def shop_config_list(self):
        return self._shop_config_list

    @shop_config_list.setter
    def shop_config_list(self, value):
        if isinstance(value, list):
            self._shop_config_list = list()
            for i in value:
                if isinstance(i, ShopOrderConfigInfo):
                    self._shop_config_list.append(i)
                else:
                    self._shop_config_list.append(ShopOrderConfigInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.shop_config_list:
            if isinstance(self.shop_config_list, list):
                for i in range(0, len(self.shop_config_list)):
                    element = self.shop_config_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_config_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_config_list, 'to_alipay_dict'):
                params['shop_config_list'] = self.shop_config_list.to_alipay_dict()
            else:
                params['shop_config_list'] = self.shop_config_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringConfigModifyModel()
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'shop_config_list' in d:
            o.shop_config_list = d['shop_config_list']
        return o


