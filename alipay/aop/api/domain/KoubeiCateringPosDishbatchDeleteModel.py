#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosDishbatchDeleteModel(object):

    def __init__(self):
        self._cook_id = None
        self._dish_ids = None
        self._merchant_id = None
        self._shop_id = None

    @property
    def cook_id(self):
        return self._cook_id

    @cook_id.setter
    def cook_id(self, value):
        self._cook_id = value
    @property
    def dish_ids(self):
        return self._dish_ids

    @dish_ids.setter
    def dish_ids(self, value):
        if isinstance(value, list):
            self._dish_ids = list()
            for i in value:
                self._dish_ids.append(i)
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cook_id:
            if hasattr(self.cook_id, 'to_alipay_dict'):
                params['cook_id'] = self.cook_id.to_alipay_dict()
            else:
                params['cook_id'] = self.cook_id
        if self.dish_ids:
            if isinstance(self.dish_ids, list):
                for i in range(0, len(self.dish_ids)):
                    element = self.dish_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_ids[i] = element.to_alipay_dict()
            if hasattr(self.dish_ids, 'to_alipay_dict'):
                params['dish_ids'] = self.dish_ids.to_alipay_dict()
            else:
                params['dish_ids'] = self.dish_ids
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosDishbatchDeleteModel()
        if 'cook_id' in d:
            o.cook_id = d['cook_id']
        if 'dish_ids' in d:
            o.dish_ids = d['dish_ids']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


