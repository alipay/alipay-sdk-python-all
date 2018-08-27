#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataIsvShopQueryModel(object):

    def __init__(self):
        self._shop_ids = None

    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        if isinstance(value, list):
            self._shop_ids = list()
            for i in value:
                self._shop_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.shop_ids:
            if isinstance(self.shop_ids, list):
                for i in range(0, len(self.shop_ids)):
                    element = self.shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_ids, 'to_alipay_dict'):
                params['shop_ids'] = self.shop_ids.to_alipay_dict()
            else:
                params['shop_ids'] = self.shop_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataIsvShopQueryModel()
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        return o


