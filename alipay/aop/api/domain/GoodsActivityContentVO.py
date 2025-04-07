#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsActivityContentVO(object):

    def __init__(self):
        self._goods_id = None
        self._related_app_id = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def related_app_id(self):
        return self._related_app_id

    @related_app_id.setter
    def related_app_id(self, value):
        self._related_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.related_app_id:
            if hasattr(self.related_app_id, 'to_alipay_dict'):
                params['related_app_id'] = self.related_app_id.to_alipay_dict()
            else:
                params['related_app_id'] = self.related_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsActivityContentVO()
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'related_app_id' in d:
            o.related_app_id = d['related_app_id']
        return o


