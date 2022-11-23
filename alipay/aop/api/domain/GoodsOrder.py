#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsOrder(object):

    def __init__(self):
        self._goods_name = None
        self._goods_picture_id = None

    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_picture_id(self):
        return self._goods_picture_id

    @goods_picture_id.setter
    def goods_picture_id(self, value):
        self._goods_picture_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_picture_id:
            if hasattr(self.goods_picture_id, 'to_alipay_dict'):
                params['goods_picture_id'] = self.goods_picture_id.to_alipay_dict()
            else:
                params['goods_picture_id'] = self.goods_picture_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsOrder()
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_picture_id' in d:
            o.goods_picture_id = d['goods_picture_id']
        return o


