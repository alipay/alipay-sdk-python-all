#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityGoodsInfo(object):

    def __init__(self):
        self._goods_id = None
        self._goods_use_type = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_use_type(self):
        return self._goods_use_type

    @goods_use_type.setter
    def goods_use_type(self, value):
        self._goods_use_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_use_type:
            if hasattr(self.goods_use_type, 'to_alipay_dict'):
                params['goods_use_type'] = self.goods_use_type.to_alipay_dict()
            else:
                params['goods_use_type'] = self.goods_use_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityGoodsInfo()
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_use_type' in d:
            o.goods_use_type = d['goods_use_type']
        return o


