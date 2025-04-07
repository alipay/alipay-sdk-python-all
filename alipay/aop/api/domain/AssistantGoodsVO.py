#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssistantGoodsVO(object):

    def __init__(self):
        self._crowd_code = None
        self._goods_item_id = None
        self._related_app_id = None

    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def goods_item_id(self):
        return self._goods_item_id

    @goods_item_id.setter
    def goods_item_id(self, value):
        self._goods_item_id = value
    @property
    def related_app_id(self):
        return self._related_app_id

    @related_app_id.setter
    def related_app_id(self, value):
        self._related_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.goods_item_id:
            if hasattr(self.goods_item_id, 'to_alipay_dict'):
                params['goods_item_id'] = self.goods_item_id.to_alipay_dict()
            else:
                params['goods_item_id'] = self.goods_item_id
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
        o = AssistantGoodsVO()
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'goods_item_id' in d:
            o.goods_item_id = d['goods_item_id']
        if 'related_app_id' in d:
            o.related_app_id = d['related_app_id']
        return o


