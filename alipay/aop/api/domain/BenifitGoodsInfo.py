#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenifitGoodsInfo(object):

    def __init__(self):
        self._extend = None
        self._goods_id = None
        self._goods_title = None
        self._goods_type = None

    @property
    def extend(self):
        return self._extend

    @extend.setter
    def extend(self, value):
        self._extend = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_title(self):
        return self._goods_title

    @goods_title.setter
    def goods_title(self, value):
        self._goods_title = value
    @property
    def goods_type(self):
        return self._goods_type

    @goods_type.setter
    def goods_type(self, value):
        self._goods_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.extend:
            if hasattr(self.extend, 'to_alipay_dict'):
                params['extend'] = self.extend.to_alipay_dict()
            else:
                params['extend'] = self.extend
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_title:
            if hasattr(self.goods_title, 'to_alipay_dict'):
                params['goods_title'] = self.goods_title.to_alipay_dict()
            else:
                params['goods_title'] = self.goods_title
        if self.goods_type:
            if hasattr(self.goods_type, 'to_alipay_dict'):
                params['goods_type'] = self.goods_type.to_alipay_dict()
            else:
                params['goods_type'] = self.goods_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenifitGoodsInfo()
        if 'extend' in d:
            o.extend = d['extend']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_title' in d:
            o.goods_title = d['goods_title']
        if 'goods_type' in d:
            o.goods_type = d['goods_type']
        return o


