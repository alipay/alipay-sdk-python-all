#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsPos(object):

    def __init__(self):
        self._goods_id = None
        self._pos = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.pos:
            if hasattr(self.pos, 'to_alipay_dict'):
                params['pos'] = self.pos.to_alipay_dict()
            else:
                params['pos'] = self.pos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsPos()
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'pos' in d:
            o.pos = d['pos']
        return o


