#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PhoneItemInfo(object):

    def __init__(self):
        self._face = None
        self._final_price = None
        self._item_id = None
        self._price = None
        self._source = None

    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, value):
        self._face = value
    @property
    def final_price(self):
        return self._final_price

    @final_price.setter
    def final_price(self, value):
        self._final_price = value
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
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.face:
            if hasattr(self.face, 'to_alipay_dict'):
                params['face'] = self.face.to_alipay_dict()
            else:
                params['face'] = self.face
        if self.final_price:
            if hasattr(self.final_price, 'to_alipay_dict'):
                params['final_price'] = self.final_price.to_alipay_dict()
            else:
                params['final_price'] = self.final_price
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
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PhoneItemInfo()
        if 'face' in d:
            o.face = d['face']
        if 'final_price' in d:
            o.final_price = d['final_price']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'price' in d:
            o.price = d['price']
        if 'source' in d:
            o.source = d['source']
        return o


