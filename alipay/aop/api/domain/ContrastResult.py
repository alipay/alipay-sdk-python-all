#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContrastResult(object):

    def __init__(self):
        self._goods_count = None
        self._goods_id = None
        self._goods_reduce = None

    @property
    def goods_count(self):
        return self._goods_count

    @goods_count.setter
    def goods_count(self, value):
        self._goods_count = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_reduce(self):
        return self._goods_reduce

    @goods_reduce.setter
    def goods_reduce(self, value):
        self._goods_reduce = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_count:
            if hasattr(self.goods_count, 'to_alipay_dict'):
                params['goods_count'] = self.goods_count.to_alipay_dict()
            else:
                params['goods_count'] = self.goods_count
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_reduce:
            if hasattr(self.goods_reduce, 'to_alipay_dict'):
                params['goods_reduce'] = self.goods_reduce.to_alipay_dict()
            else:
                params['goods_reduce'] = self.goods_reduce
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContrastResult()
        if 'goods_count' in d:
            o.goods_count = d['goods_count']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_reduce' in d:
            o.goods_reduce = d['goods_reduce']
        return o


