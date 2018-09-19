#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CraftsmanShopRelationOpenModel(object):

    def __init__(self):
        self._recommend_weight = None
        self._shop_id = None

    @property
    def recommend_weight(self):
        return self._recommend_weight

    @recommend_weight.setter
    def recommend_weight(self, value):
        self._recommend_weight = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.recommend_weight:
            if hasattr(self.recommend_weight, 'to_alipay_dict'):
                params['recommend_weight'] = self.recommend_weight.to_alipay_dict()
            else:
                params['recommend_weight'] = self.recommend_weight
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
        o = CraftsmanShopRelationOpenModel()
        if 'recommend_weight' in d:
            o.recommend_weight = d['recommend_weight']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


