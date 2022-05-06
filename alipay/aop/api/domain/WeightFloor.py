#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodsPos import GoodsPos


class WeightFloor(object):

    def __init__(self):
        self._floor_id = None
        self._goods_list = None

    @property
    def floor_id(self):
        return self._floor_id

    @floor_id.setter
    def floor_id(self, value):
        self._floor_id = value
    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, list):
            self._goods_list = list()
            for i in value:
                if isinstance(i, GoodsPos):
                    self._goods_list.append(i)
                else:
                    self._goods_list.append(GoodsPos.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.floor_id:
            if hasattr(self.floor_id, 'to_alipay_dict'):
                params['floor_id'] = self.floor_id.to_alipay_dict()
            else:
                params['floor_id'] = self.floor_id
        if self.goods_list:
            if isinstance(self.goods_list, list):
                for i in range(0, len(self.goods_list)):
                    element = self.goods_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_list, 'to_alipay_dict'):
                params['goods_list'] = self.goods_list.to_alipay_dict()
            else:
                params['goods_list'] = self.goods_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WeightFloor()
        if 'floor_id' in d:
            o.floor_id = d['floor_id']
        if 'goods_list' in d:
            o.goods_list = d['goods_list']
        return o


