#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsState(object):

    def __init__(self):
        self._algorithm_goods_id = None
        self._floor = None
        self._left_loc = None

    @property
    def algorithm_goods_id(self):
        return self._algorithm_goods_id

    @algorithm_goods_id.setter
    def algorithm_goods_id(self, value):
        self._algorithm_goods_id = value
    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value
    @property
    def left_loc(self):
        return self._left_loc

    @left_loc.setter
    def left_loc(self, value):
        self._left_loc = value


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_goods_id:
            if hasattr(self.algorithm_goods_id, 'to_alipay_dict'):
                params['algorithm_goods_id'] = self.algorithm_goods_id.to_alipay_dict()
            else:
                params['algorithm_goods_id'] = self.algorithm_goods_id
        if self.floor:
            if hasattr(self.floor, 'to_alipay_dict'):
                params['floor'] = self.floor.to_alipay_dict()
            else:
                params['floor'] = self.floor
        if self.left_loc:
            if hasattr(self.left_loc, 'to_alipay_dict'):
                params['left_loc'] = self.left_loc.to_alipay_dict()
            else:
                params['left_loc'] = self.left_loc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsState()
        if 'algorithm_goods_id' in d:
            o.algorithm_goods_id = d['algorithm_goods_id']
        if 'floor' in d:
            o.floor = d['floor']
        if 'left_loc' in d:
            o.left_loc = d['left_loc']
        return o


