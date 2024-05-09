#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LitePredictGoodsResult(object):

    def __init__(self):
        self._conf = None
        self._goods_id = None

    @property
    def conf(self):
        return self._conf

    @conf.setter
    def conf(self, value):
        self._conf = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.conf:
            if hasattr(self.conf, 'to_alipay_dict'):
                params['conf'] = self.conf.to_alipay_dict()
            else:
                params['conf'] = self.conf
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LitePredictGoodsResult()
        if 'conf' in d:
            o.conf = d['conf']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        return o


