#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecommendItemInfo(object):

    def __init__(self):
        self._face = None
        self._item_id = None
        self._price = None

    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, value):
        self._face = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
        if self.face:
            if hasattr(self.face, 'to_alipay_dict'):
                params['face'] = self.face.to_alipay_dict()
            else:
                params['face'] = self.face
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecommendItemInfo()
        if 'face' in d:
            o.face = d['face']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'price' in d:
            o.price = d['price']
        return o


