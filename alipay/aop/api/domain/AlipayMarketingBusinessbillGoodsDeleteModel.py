#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingBusinessbillGoodsDeleteModel(object):

    def __init__(self):
        self._activity_scene = None
        self._goods_id = None
        self._open_id = None
        self._user_id = None

    @property
    def activity_scene(self):
        return self._activity_scene

    @activity_scene.setter
    def activity_scene(self, value):
        self._activity_scene = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_scene:
            if hasattr(self.activity_scene, 'to_alipay_dict'):
                params['activity_scene'] = self.activity_scene.to_alipay_dict()
            else:
                params['activity_scene'] = self.activity_scene
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingBusinessbillGoodsDeleteModel()
        if 'activity_scene' in d:
            o.activity_scene = d['activity_scene']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


